# Chapter 4
Integrate with Hosts With mcp.json

1. Create mcp.json
~~~
mkdir .vscode
touch .vscode/mcp.json
~~~
2. Update mcp.json for local stdio server: [mcp-stdio.json](mcp-stdio.json)
3. Example of for an SSE server on Windows (you will need to modify and create server.js): [mcp-sse-windows.json](mcp-sse-windows.json)
4. If you are doing the Claude Desktop demo, here is the example code to add to Claude Desktop’s claude_desktop_config.json under mcpServers (note "python" on Windows, not "python3"):
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

## Preparing Windows 11
**IMPORTANT** To actually run with Claude Desktop on a Windows machine, you have some work to do

1. Upgrade Python as version 3.9 is too old (and it's End of Life!)
    - download the latest installer ("bugfix", currently 3.14)
    - select version, scroll down, and click **Download Pythin install manager**
    - Note the options
      - WinGet: `winget install 9NQ7512CXL7T`
      - Installer (MSIX)
      - MSI package (see documentation before use)
    - Add Python to PATH
    - I found python --version kept showing v.9 by py --version showed 3.14.4
2. Uninstall Python 3.9 from the Microsoft store
3. Set up the environment
    - Install `uv`
      - `powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"`
      - Follow instructions to add to the path
      - $env:Path = "C:\Users\sethh\.local\bin;$env:Path"
      - `uv python install 3.14`
    - Create project directory
      - Change directory to where the proejct belongs (e.e., `cd \projects\`)
      - `uv init mcp-lab`
      - `cd mcp-lab`
    - Set up virtual environment
      - `uv venv --python 3.14`
      - `Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass`
      - `.venv\Scripts\activate`
    - Modify `pyproject.toml`
      - Update version to: `requires-python = ">=3.14"`
    - Install dependencies
      - `uv add mcp[cli] httpx requests`
      - To retry
        - `uv python pin 3.14`
        -  `uv sync`
        -  `uv add mcp[cli] httpx requests`
    - `new-item server.py`
4. Modify the server.py file with the contents of [server.py](server.py)
    - For example, I created `c:\tools\mcp-lab\server.py`
5. Install Claude Code desktop app
6. Create a new project (e.g., "mcp-lab-testing")
7. Hamburger menu > File > Settings > Developer > Local MCP servers > **Edit Config**
8. A folder will open to the **claude_desktop_config.json** file
9. Edit the file
10. Add the mcpServers section
    - At the end of the "preferences" stanza, add a comma, then paste the content (above)
    - Example of the full file below for C:\tools\mcp-lab\server.py utilizing the venv and python3.14
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
      "args": ["run", "--project","C:\\tools\\mcp-lab", "python", "C:\\tools\\mcp-lab\\server.py"]
    }
  }
}
~~~
11. Restart Claude app
    - You will see a brief error message if MCP server failed to connect
    - Check by clicking Hamburger > File > Settings > Developer
    - if demo-server is **running** you are are good
12. Test by asking questions
    - Go back to the chat window
    - Ask: "tell me Chuck Norris Joke"
      - It will ask you to approve using the tool
    - Ask: "tell me Chuck Norris Joke about docs"
    - Ask: "what is 42 plus 58?"
      - It will probably just give you the answer without using the tool
    - Ask: "use the add tool to add 42 and 58"
      - It will ask you to approve using the tool
