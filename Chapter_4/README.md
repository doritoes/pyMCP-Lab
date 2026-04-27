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
    "command": "uv",
    "args": ["run", "mcp", "run", "server.py"]
  }
}
~~~
**NOT WORKING YET**

**IMPORTANT** To actually run with Claude Desktop on a Windows machine, you have some work to do

To upgrade Python from 3.9 on Windows 11, download the latest installer (e.g., 3.12 or 3.13) from python.org, run it, and check "Add Python to PATH" before clicking "Install Now". 

1. Set up the environment
    - Install `uv1`
      - `powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"`
      - Follow instructions to add to the path
      - $env:Path = "C:\Users\sethh\.local\bin;$env:Path"
    - Create project directory
      - Change directory to where the proejct belongs (e.e., `cd \projects\`)
      - `uv init mcp-lab`
      - `cd mcp-lab`
    - Set up virtual environment
      - `uv venv`
      - `Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass`
      - `.venv\Scripts\activate`
    - Install dependencies
      - `uv add mcp[cli] httpx`
    - `new-item server.py`
2. Modify the server.py file with the contents of [server.py](server.py)
3. Install Claude Code desktop app
4. Create a new project (e.g., "mcp-lab-testing")
5. Hamburger menu > File > Settings > Developer > Local MCP servers > **Edit Config**
7. A folder will open to the **claude_desktop_config.json** file
8. Edit the file
9. Add the mcpServers section
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
      "command": "uv",
      "args": ["run", "mcp", "run", "server.py"]
    }
  }
}
~~~
8. Restart Claude app
9. Check if MCP server is connected ?????
10. Ask questions
