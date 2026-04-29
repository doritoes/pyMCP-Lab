# Chapter 7
We are using Python (python3) in Windows WSL Ubuntu 24.04

1. Don't forget to activate your virtual environment (venv)
~~~
source ./venv/bin/activate
~~~

2. Edit client.py to match [client.py](client.py)
3. Run the client
    - `python3 client.py`

Example output:
~~~
(venv) linux@LT-L4880X:~/mcp-lab$ python3 client.py
LISTING RESOURCES
[04/29/26 16:40:51] INFO     Processing request of type ListResourcesRequest                     server.py:727
Resource: ('meta', None)

LISTING TOOLS
                    INFO     Processing request of type ListToolsRequest                         server.py:727
Tool: add
Tool: joke
Resource: ('nextCursor', None)

LISTING TOOLS
                    INFO     Processing request of type ListToolsRequest                         server.py:727
Tool: add
Tool: joke
Resource: ('resources', [Resource(name='readme', title=None, uri=AnyUrl('reference://readme'), description='How to use this server and sample calls.', mimeType='text/plain', size=None, icons=None, annotations=None, meta=None)])

LISTING TOOLS
                    INFO     Processing request of type ListToolsRequest                         server.py:727
Tool: add
Tool: joke
READING RESOURCE
                    INFO     Processing request of type ReadResourceRequest                      server.py:727
MIME TYPE: ('contents', [TextResourceContents(uri=AnyUrl('reference://readme'), mimeType='text/plain', meta=None, text='Reference MCP Server\n\nTools:\n- add(a:int, b:int) -> int\n- joke(topic?:str) -> str\n\nUse this server to test tool selection, argument passing, and basic MCP wiring.\n')])
('meta', None)

CALL TOOL: add(a=1, b=7)
                    INFO     Processing request of type CallToolRequest                          server.py:727
RESULT: [TextContent(type='text', text='8', annotations=None, meta=None)]
(venv) linux@LT-L4880X:~/mcp-lab$
~~~
