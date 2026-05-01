import asyncio
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
# Launch the MCP server over stdio using uv
server_params = StdioServerParameters(
    command="python",
    args=["server.py"],
    env=None)
async def run():
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            # Initialize the MCP connection (handshake)
            await session.initialize()
            # List available resources
            print("LISTING RESOURCES")
            resources = await session.list_resources()
            for resource in resources:
                print("Resource:", resource)
                # List available tools
                print("\nLISTING TOOLS")
                tools = await session.list_tools()
                for tool in tools.tools:
                    print("Tool:", tool.name)
            # Read a resource
            print("READING RESOURCE")
            content, mime_type = await session.read_resource("reference://readme")
            print("MIME TYPE:", mime_type)
            print(content)
            # Call a tool
            print("\nCALL TOOL: add(a=1, b=7)")
            result = await session.call_tool("add", arguments={"a": 1, "b": 7})
            print("RESULT:", result.content)
if __name__ == "__main__":
    asyncio.run(run())
