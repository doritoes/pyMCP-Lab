# Route one user prompt to an MCP tool call (with validation + optional repair)
def validate_args(schema: dict, args: dict) -> tuple[bool, str]:
    required = schema.get("required", [])
    props = schema.get("properties", {})
    for k in required:
        if k not in args:
            return False, f"Missing required arg: {k}"
        for k, v in args.items():
            if k in props and props[k].get("type") == "integer" and not isinstance(v, int):
                return False, f"Arg {k} must be integer"
            return True, ""

async def route_prompt(prompt: str, functions: list[dict], session: ClientSession):
    tool_calls = call_llm(prompt, functions) # -> [{"name": "...", "args": {...}}]
    for call in tool_calls:
        fn = next(f for f in functions if f["function"]["name"] == call["name"])
        schema = fn["function"]["parameters"]
        ok, err = validate_args(schema, call["args"])
        if not ok:
            # Ask LLM to repair arguments using the same schema
            repair_prompt = f"Fix tool args to match this JSON schema:\n{schema}\nArgs:\n{call['args']}\nError: {err}"
            repaired = call_llm(repair_prompt, functions=[fn])
            if repaired:
                call = repaired[0]
    # Optional approval gate (UI/CLI prompt would go here)
    result = await session.call_tool(call["name"], arguments=call["args"])
    return result.content
