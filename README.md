# langchain-apiverve

[![PyPI version](https://img.shields.io/pypi/v/langchain-apiverve.svg)](https://pypi.org/project/langchain-apiverve/)
[![Python versions](https://img.shields.io/pypi/pyversions/langchain-apiverve.svg)](https://pypi.org/project/langchain-apiverve/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![LangChain](https://img.shields.io/badge/LangChain-Integration-blue)](https://python.langchain.com/)

**LangChain integration for [APIVerve](https://apiverve.com)** - Access 356+ utility APIs for AI agents and LLM applications.

Build powerful AI agents with access to validation, conversion, generation, analysis, and lookup APIs.

---

## Features

- **356+ APIs** - Email validation, DNS lookup, IP geolocation, QR codes, currency conversion, and more
- **29 Categories** - Text Processing, Data Generation, Games, Entertainment, Calendar, and more
- **LangChain Native** - Works with any LangChain agent or chain
- **Type Safe** - Full Pydantic schemas for inputs and outputs
- **Async Support** - Both sync and async API calls
- **Flexible** - Use individual tools or the "run any" meta-tool

---

## Installation

```bash
pip install langchain-apiverve
```

## Quick Start

```python
from langchain_apiverve import APIVerveToolkit
from langchain_openai import ChatOpenAI
from langchain.agents import create_tool_calling_agent, AgentExecutor
from langchain_core.prompts import ChatPromptTemplate

# Initialize toolkit with your API key
toolkit = APIVerveToolkit(api_key="your-api-key")
# Or set APIVERVE_API_KEY environment variable

# Get tools
tools = toolkit.get_tools()

# Create an agent
llm = ChatOpenAI(model="gpt-4")
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant with access to various utility APIs."),
    ("human", "{input}"),
    ("placeholder", "{agent_scratchpad}"),
])

agent = create_tool_calling_agent(llm, tools, prompt)
executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

# Use the agent
result = executor.invoke({"input": "Is test@example.com a valid email?"})
print(result["output"])
```

---

## Usage Examples

### Using Individual Tools

```python
from langchain_apiverve import APIVerveToolkit

toolkit = APIVerveToolkit(api_key="your-api-key")

# Get specific tools
tools = toolkit.get_tools(include_apis=["emailvalidator", "dnslookup"])

# Use a tool directly
email_tool = tools[0]
result = email_tool.invoke({"email": "user@example.com"})
print(result)
```

### Using the "Run Any" Tool

```python
from langchain_apiverve import APIVerveToolkit

toolkit = APIVerveToolkit(api_key="your-api-key")

# Get the flexible run-any tool
run_any = toolkit.get_run_any_tool()

# Call any API dynamically
result = run_any.invoke({
    "api_id": "qrcodegenerator",
    "parameters": {"value": "https://example.com"}
})
print(result)
```

### Filtering Tools by Category

```python
from langchain_apiverve import APIVerveToolkit

toolkit = APIVerveToolkit(api_key="your-api-key")

# Get only validation tools
validation_tools = toolkit.get_tools(categories=["Validation"])

# Get only lookup tools
lookup_tools = toolkit.get_tools(categories=["Lookup"])
```

### Low-Level Client Usage

```python
from langchain_apiverve import APIVerveClient

client = APIVerveClient(api_key="your-api-key")

# Make API calls directly
result = client.call_api("emailvalidator", {"email": "test@example.com"})
print(result)

# Async usage
import asyncio

async def main():
    result = await client.acall_api("dnslookup", {"domain": "example.com"})
    print(result)

asyncio.run(main())
```

---

## Available APIs

APIVerve provides 356+ APIs across 29 categories:

| Category | APIs | Examples |
|----------|------|----------|
| **Text Processing** | 45 | Acronym Expander, Anagram Detector, Antonym Finder |
| **Data Generation** | 32 | Acronym Generator, Baby Name Generator, Barcode Generator |
| **Games** | 21 | Acrostic Puzzle Generator, Anagram Puzzle Generator, Card Deck Shuffler |
| **Entertainment** | 24 | Advice Generator, Bucket List, Charades Generator |
| **Calendar** | 5 | Age Calculator, Date Calculator, Liturgical Calendar |
| **Transportation** | 5 | Airline Lookup, Airport Code Converter, Airport Distance |
| **Weather** | 8 | Air Quality, Worldwide Earthquakes, Marine Weather |
| **AI/Computer Vision** | 6 | Article Ideas Generator, Code Detector, Image Caption |
| **Data Conversion** | 33 | ASCII85 Encoder, Base64 Encoder/Decoder, Color Converter |
| **Data Lookup** | 17 | ASN Lookup, Bible, Country Calling Code |

[Browse all APIs →](https://apiverve.com/marketplace)

---

## API Response Format

All APIVerve APIs return a consistent response format:

```json
{
  "status": "ok",
  "error": null,
  "data": {
    // API-specific response data
  }
}
```

---

## Configuration

### Environment Variables

| Variable | Description |
|----------|-------------|
| `APIVERVE_API_KEY` | Your APIVerve API key |

### Toolkit Options

```python
toolkit = APIVerveToolkit(
    api_key="...",           # API key (or use env var)
    base_url="...",          # Custom API base URL
)

tools = toolkit.get_tools(
    categories=["..."],      # Filter by category
    include_apis=["..."],    # Only include specific APIs
    exclude_apis=["..."],    # Exclude specific APIs
    include_run_any=True,    # Include the "run any" tool
    include_popular=True,    # Include pre-built popular tools
)
```

---

## Development

### Setup

```bash
# Clone the repository
git clone https://github.com/apiverve/langchain-apiverve.git
cd langchain-apiverve

# Install with Poetry
poetry install

# Or with pip
pip install -e ".[dev]"
```

### Running Tests

```bash
pytest
```

### Linting

```bash
ruff check .
mypy src/
```

---

## Resources

| Resource | Link |
|----------|------|
| APIVerve Website | [apiverve.com](https://apiverve.com) |
| API Documentation | [docs.apiverve.com](https://docs.apiverve.com) |
| API Marketplace | [apiverve.com/marketplace](https://apiverve.com/marketplace) |
| LangChain Docs | [python.langchain.com](https://python.langchain.com) |
| GitHub Issues | [github.com/apiverve/langchain-apiverve/issues](https://github.com/apiverve/langchain-apiverve/issues) |

---

## License

MIT License - see [LICENSE](LICENSE) for details.

Copyright (c) 2026 [APIVerve](https://apiverve.com)
