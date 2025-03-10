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
      "/ABSOLUTE/PATH/TO/PARENT/FOLDER/mcp-transcripts/src",
      "run",
      "server.py"
    ]
  }
}
```

## Setup
This project uses [uv](https://docs.astral.sh/uv/) for package/project management. 
To run this project, follow the below setup instructions.

1. Install uv if you haven't already. [Here's](https://docs.astral.sh/uv/getting-started/installation/) the installation instructions.
2. Clone the repo.
   ```sh
   git clone https://github.com/PraveenKishore/mcp-server-youtube.git
   cd mcp-server-youtube
   ```
3. Create virtual env and install dependencies.
   ```sh
   uv sync
   ```
4. Activate the virtual env.
   ```sh
   source .venv/bin/activate  # Activate the virtual environment (Linux/MacOS)
   # OR
   .\.venv\Scripts\activate  # Activate the virtual environment (Windows)
   ```
5. You're all set!

## Testing the MCP Server

### 1. **Testing Only the MCP Server**  
To launch the MCP inspector, run the following command:

```bash
mcp dev src/server.py
```

This will start the server, allowing you to view the list of exposed tools in the **Tools** tab. You can also invoke any of these tools with the appropriate input.

### 2. **Testing with Claude Desktop**  
To test with **Claude Desktop**, add the MCP configuration to the `claude_desktop_config.json` file.  
For more details, refer to [this link](https://modelcontextprotocol.io/quickstart/user). Once configured, you should be able to invoke the tool directly within the **Claude Desktop** interface.

### 3. **Testing with mcp-client-cli**  
The [`mcp-client-cli`](https://github.com/adhikasp/mcp-client-cli) is a simple command-line tool for running LLM prompts and implementing the Model Context Protocol (MCP) client.  
To use this tool, add the MCP configuration to `~/.llm/config.json`. For further setup instructions, check out the [official setup guide](https://github.com/adhikasp/mcp-client-cli?tab=readme-ov-file#setup). After configuration, you’ll be able to invoke the tool within `mcp-client-cli`.