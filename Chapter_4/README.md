# Chapter 4
Integrate with Hosts With mcp.json

1. Create mcp.json
~~~
mkdir .vscode
touch .vscode/mcp.json
~~~
2. Update mcp.json for local stdio server: [mcp-stdio.json](mcp-stdio.json)
3. Example of for an SSE server on Windows: [mcp-sse-windows.json](mcp-sse-windows.json)
4. If you are doing the Claude Desktop demo, here is the code to add to Claude Desktop’s claude_desktop_config.json under mcpServers:
~~~
"mcpServers": {
  "demo-server": {
    "type": "stdio",
    "command": "python3",
    "args": ["server.py"]
  }
}
~~~
