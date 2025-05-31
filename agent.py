from langchain_community.utilities import SQLDatabase
from langchain_community.agent_toolkits.sql.toolkit import SQLDatabaseToolkit
from langchain_community.agent_toolkits.sql.base import create_sql_agent

def create_agent(engine, llm):
    db = SQLDatabase(engine)
    toolkit = SQLDatabaseToolkit(db=db, llm=llm)
    return create_sql_agent(llm=llm, toolkit=toolkit, verbose=True)
