# Chapter 3
Testing what happens in unexepected cases.

1. Example wrong variable type
    - `npx @modelcontextprotocol/inspector --cli python3 server.py --method tools/call --tool-name add --tool-arg a=18 --tool-arg b=2`
    - `npx @modelcontextprotocol/inspector --cli python3 server.py --method tools/call --tool-name add --tool-arg a="18" --tool-arg b=2`
    - `npx @modelcontextprotocol/inspector --cli python3 server.py --method tools/call --tool-name add --tool-arg a=eighteen --tool-arg b=2`
    - `npx @modelcontextprotocol/inspector --cli python3 server.py --method tools/call --tool-name joke --tool-arg topic=cats`
    - `npx @modelcontextprotocol/inspector --cli python3 server.py --method tools/call --tool-name joke --tool-arg topic=18`
    - `npx @modelcontextprotocol/inspector --cli python3 server.py --method tools/call --tool-name joke --tool-arg topic="18"`
2. Example wrong method
    - `npx @modelcontextprotocol/inspector --cli python3 server.py --method tools/list`
    - `npx @modelcontextprotocol/inspector --cli python3 server.py --method tools/list --tool-name joke`
