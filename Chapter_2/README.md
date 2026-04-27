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
4. Run the server
    - `mcp dev server.py`
    - The first time, you will be prompted to install the inspector, choose **y**
5. The Inspector will launch in a web page on localhost port 6274
    - Change command to **python3**
    - Change arguments to **server.py**
    - Click **Connect**
6. Click **Tools** then **List Tools**
    - the tools work (try adding 10 and 5; try a joke, then a joke about cats)
7. Click Resource panel
    - **List Resources** shows readme (click to view contents)
    - **List Templates** does not work yet (it's empty)
