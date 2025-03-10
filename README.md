# YouTube Transcript MCP Server

This project implements a Model Context Protocol (MCP) server that provides a tool for fetching YouTube video transcripts in various formats. Leveraging the `youtube-transcript-api`, the server allows Large Language Models (LLMs) to access YouTube transcripts securely and efficiently.

## Overview

The server exposes a tool, `fetch_youtube_transcript`, which retrieves transcripts for YouTube videos based on the provided video ID, language code, and desired format. This functionality enables LLMs to access and process YouTube video transcripts seamlessly.

## Features

- **YouTube Transcript Retrieval:** Fetch transcripts for YouTube videos in multiple languages.
- **Flexible Output Formats:** Obtain transcripts in either plain text or JSON format.
- **MCP Integration:** Designed to work seamlessly with MCP-compatible clients and tools.

## Configuration with MCP Client

```
"mcpServers": {
  "youtube-transcripts": {
    "command": "uv",
    "args": [
      "--directory",
      "/ABSOLUTE/PATH/TO/PARENT/FOLDER/mcp-transcripts",
      "run",
      "server.py"
    ]
  }
}
```

## Testing

### Testing only the MCP server

Run this command - `mcp dev server.py` to launch an mcp inspector. You can view the tools list exposed in the tools tab and also invoke the tool with any input.

### Testing with Claude Desktop

Add the above mcp config in `claude_desktop_config.json`. More info [here](https://modelcontextprotocol.io/quickstart/user). You should be able to invoke the tool within Claude for desktop.

### Testing with mcp-client-cli

[`mcp-client-cli`](https://github.com/adhikasp/mcp-client-cli) is a simple CLI program to run LLM prompt and implement Model Context Protocol (MCP) client.
Paste the above config in the `~/.llm/config.json` to be able to use the tool within mcp-client-cli. More info in their [setup instructions](https://github.com/adhikasp/mcp-client-cli?tab=readme-ov-file#setup)
