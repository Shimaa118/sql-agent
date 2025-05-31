# SQL Agent

A LangChain-powered SQL agent using Google Gemini


## Features

- SQLite database with SalesData and ProductCatalog tables
- Modular SQLAlchemy database setup
- Google Gemini LLM integration
- LangChain SQL agent for natural language querying
- Simple CLI for querying the database with natural language

## Setup

1. Clone the repo:

```bash
git clone https://github.com/yourusername/sql-agent.git
cd sql-agent
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the main script

```bash
python main.py
```

4. Enter your google api key for Gemini LLM

5. Enter your query related to the database. for
example: "What is the total sales amount on 29th September 2023?"