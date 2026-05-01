# Chapter 5
Strangely enough, sections stop matching Chapter numbers.

## Section 7 - Starting and negotiating
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

## Section 8

### Converting tools for the LLM
1. `pip install azure-ai-inference`
2. Create llm.py from (llm.py)[llm.py]
3. Get a GitHub personal access token
    - Create the Token on GitHub
      - Go to GitHub Settings → [Developer settings](https://github.com/settings/tokens)
      - Select Personal access tokens and then Tokens (classic)
      - Click Generate new token → Generate new token (classic)
        - Note: Give it a name like "MCP Lab Token"
        - Default expiration is 30 days
        - Scopes (Important): For this specific lab using GitHub Models, you don't need to check anything
        - Click Generate token and copy it immediately. You won't see it again!
4. Set the environment variable with your GitHub personal access token:
    - `export GITHUB_TOKEN=your_personal_access_token`
    - Note: If your token contains special characters, use the single quotes ' ' to ensure the terminal handles it correctly.
5. `python3 llm.py`

Example output:
~~~
(venv) linux@LT-L4880X:~/mcp-lab$ python3 llm.py
[04/29/26 18:11:43] INFO     Processing request of type ListResourcesRequest                     server.py:727
LISTING RESOURCES
Resource:  ('meta', None)
                    INFO     Processing request of type ListToolsRequest                         server.py:727
LISTING TOOLS
Tool:  add
Tool {'a': {'title': 'A', 'type': 'integer'}, 'b': {'title': 'B', 'type': 'integer'}}
Tool:  joke
Tool {'topic': {'anyOf': [{'type': 'string'}, {'type': 'null'}], 'default': None, 'title': 'Topic'}}
Resource:  ('nextCursor', None)
                    INFO     Processing request of type ListToolsRequest                         server.py:727
LISTING TOOLS
Tool:  add
Tool {'a': {'title': 'A', 'type': 'integer'}, 'b': {'title': 'B', 'type': 'integer'}}
Tool:  joke
Tool {'topic': {'anyOf': [{'type': 'string'}, {'type': 'null'}], 'default': None, 'title': 'Topic'}}
Resource:  ('resources', [Resource(name='readme', title=None, uri=AnyUrl('reference://readme'), description='How to use this server and sample calls.', mimeType='text/plain', size=None, icons=None, annotations=None, meta=None)])
                    INFO     Processing request of type ListToolsRequest                         server.py:727
LISTING TOOLS
Tool:  add
Tool {'a': {'title': 'A', 'type': 'integer'}, 'b': {'title': 'B', 'type': 'integer'}}
Tool:  joke
Tool {'topic': {'anyOf': [{'type': 'string'}, {'type': 'null'}], 'default': None, 'title': 'Topic'}}
CALLING LLM
TOOL:  {'function': {'arguments': '{"a":2,"b":20}', 'name': 'add'}, 'id': 'call_HUIO69xe5H0Pbd62LUyZYqOe', 'type': 'function'}
[04/29/26 18:11:44] INFO     Processing request of type CallToolRequest                          server.py:727
TOOLS result:  [TextContent(type='text', text='22', annotations=None, meta=None)]
(venv) linux@LT-L4880X:~/mcp-lab$
~~~
### Rule prompts to tools
The book's code is saved to [routeprompts.py](routeprompts.py)

It looks like it goes into client.py, but not sure how to activate it.

### Handle responses
Nothing to note

### Runtimes and composition
The book's code is saved to [multipleservers.py](multipleservers.py)
