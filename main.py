from database import setup_database
from llm_setup import get_llm
from agent import create_agent
from query_runner import run_query

def main():
    engine = setup_database()
    llm = get_llm()
    agent = create_agent(engine, llm)

    while True:
        query = input("Enter your query (or type 'exit' to quit): ")
        if query.lower() == 'exit':
            print("Exiting...")
            break
        run_query(agent, query)

if __name__ == "__main__":
    main()



