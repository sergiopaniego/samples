from smolagents import CodeAgent, HfApiModel
from smolagents.mcp_client import MCPClient
from mcp import StdioServerParameters
import os

# Login to HF using: huggingface-cli login
model = HfApiModel()

# Install nodejs and npm (https://nodejs.org/en/download)
server_parameters = StdioServerParameters(
    command="npx",
    args=["-y", "@peng-shawn/mermaid-mcp-server"],
)

with MCPClient(server_parameters) as tools:    
    agent = CodeAgent(tools=tools, model=model, add_base_tools=False)
    agent.run("Can you generate a diagram for a simple flowchart with three nodes: Start, Process, End and save it to a PNG file?")