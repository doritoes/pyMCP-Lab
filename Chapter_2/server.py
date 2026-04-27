import random
import requests
from mcp.server.fastmcp import FastMCP
mcp = FastMCP("First server")
# --- Tools ---
@mcp.tool()
def add(a: int, b: int) -> int:
    """ Add two integers """
    return a + b
@mcp.tool()
def joke(topic: str | None = None) -> str:
    """Return a Chuck Norris joke; optionally filter by topic."""
    if topic:
        res = requests.get("https://api.chucknorris.io/jokes/search", params={"query": topic})
        data = res.json()
        results = data.get("result", [])
        if results:
            return random.choice(results).get("value", "No joke found.")
    res = requests.get("https://api.chucknorris.io/jokes/random")
    data = res.json()
    return data.get("value", "No joke found.")
# --- Resource ---
@mcp.resource("reference://readme")
def readme() -> str:
    """How to use this server and sample calls."""
    return (
        "Reference MCP Server\n\n"
        "Tools:\n"
        "- add(a:int, b:int) -> int\n"
        "- joke(topic?:str) -> str\n\n"
        "Use this server to test tool selection, argument passing, and basic MCP wiring.\n"
    )
# --- Prompt ---
@mcp.prompt(name="math_add_prompt", description="Recipe for using add/joke reliably with this server.")
def math_add_prompt() -> str:
    return (
        "You are using the Reference MCP server.\n\n"
        "When the user asks to add numbers:\n"
        "1) Call the add tool with integers a and b.\n"
        "2) Confirm inputs before executing.\n"
        "3) Reply with just the numeric result.\n\n"
        "If the user asks for a joke:\n"
        "1) If they provide a topic, call joke with that topic. Otherwise call joke with no topic.\n"
        "2) Reply with the joke text only.\n"
    )

if __name__ == "__main__":
    mcp.run()
