# Chapter 2
We are using Python (python3) in Windows WSL Ubuntu 24.04

1. Set up the environment
~~~
sudo apt update && sudo apt install -y python3-venv
python3 -m venv venv
source ./venv/bin/activate
pip install "mcp[cli]" requests
~~~

2. Ubuntu has old nodejs version, update it
    - `node -v`
    - `curl -fsSL https://deb.nodesource.com/setup_20.x | sudo -E bash -`
    - `sudo apt install -y nodejs`
    - `node -v`

3. Create the project
~~~
mkdir mcp-lab
cd mcp-lab
touch server.py
~~~

4. Edit server.py to match [server.py](server.py)
5. Run the server
    - `mcp dev server.py`
    - The first time, you will be prompted to install the inspector, choose **y**
    - It will stay running in the background, press control-c to stop it
6. The Inspector will launch in a web page on localhost port 6274
    - Change command to **python3**
    - Change arguments to **server.py**
    - Click **Connect**
7. Click **Tools** then **List Tools**
    - the tools work (try adding 10 and 5; try a joke, then a joke about cats)
8. Click Resources panel
    - **List Resources** shows readme (click to view contents)
9. Click Prompts panel
    - **List Prompts** and then **Get Prompt**, expand content to see the prompt
10. Use Inspector in CLI mode (headless, works without "mcp dev server.py")
    - `npx @modelcontextprotocol/inspector --cli python3 server.py --method tools/list`
    - `npx @modelcontextprotocol/inspector --cli python3 server.py --method tools/call --tool-name add --tool-arg a=18 --tool-arg b=2`
    - `npx @modelcontextprotocol/inspector --cli python3 server.py --method tools/call --tool-name joke --tool-arg topic=cats`
    - `npx @modelcontextprotocol/inspector --cli python3 server.py --method tools/call --tool-name joke`
