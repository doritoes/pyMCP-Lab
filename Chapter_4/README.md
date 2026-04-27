# Chapter 4
Integrate with Hosts With mcp.json

1. Create mcp.json
~~~
mkdir .vscode
touch .vscode/mcp.json
~~~
2. Update mcp.json for local stdio server: [mcp-stdio.json](mcp-stdio.json)
3. Example of for an SSE server on Windows (you will need to modify and create server.js): [mcp-sse-windows.json](mcp-sse-windows.json)
4. If you are doing the Claude Desktop demo, here is the code to add to Claude Desktop’s claude_desktop_config.json under mcpServers (note "python" on Windows, not "python3"):
~~~
"mcpServers": {
  "demo-server": {
    "type": "stdio",
    "command": "python",
    "args": ["server.py"]
  }
}
~~~
**NOT WORKING YET**

**IMPORTANT** To actually run with Claude Desktop on a Windows machine, you have some work to do
1. Set up Python to run this server
2. Install Claude Code desktop app
3. Create a new project (e.g., "mcp-lab")
4. Files > + Add Files > add server.py
    - make user on local system, not OneDrive
5. Hamburger menu > File > Settings > Developer > Local MCP servers > **Edit Config**
6. A folder will open to the **claude_desktop_config.json** file
7. Edit the file
8. Add the mcpServers section
    - At the end of the "preferences" stanza, add a comma, then paste the content (above)
    - Example of the full file below
~~~
{
  "preferences": {
    "coworkWebSearchEnabled": true,
    "sidebarMode": "task",
    "coworkScheduledTasksEnabled": true,
    "ccdScheduledTasksEnabled": true
  },
  "mcpServers": {
    "demo-server": {
      "type": "stdio",
      "command": "python",
      "args": ["server.py"]
    }
  }
}
~~~
8. Restart Claude app
