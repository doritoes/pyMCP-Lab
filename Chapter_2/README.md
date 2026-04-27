# Chapter 2
We are using Python (python3) in Windows WSL Ubuntu.

1. Set up the environment
~~~
sudo apt update && sudo apt install -y python3-venv
python3 -m venv venv
source ./venv/bin/activate
pip install "mcp[cli]" requests
~~~

2. Create the project
~~~
mkdir mcp-lab
cd mcp-lab
touch server.py
~~~

3. Edit server.py to match [server.py](server.py)
