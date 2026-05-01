servers = {
    "local": {"transport": "stdio", "start": ["uv","run","mcp","run","server.py"]},
    "prod": {"transport": "http", "url": "https://example.com/mcp"},
}

tool_index = {
    "local": ["add", "joke"],
    "prod": ["search", "summarize"],
}

def route_tool_call(tool_name, args, chosen_server_id, sessions):
    session = sessions[chosen_server_id]
    return session.call_tool(tool_name, arguments=args)
