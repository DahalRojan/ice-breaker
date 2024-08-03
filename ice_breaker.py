from langchain.prompts.prompt import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama
from langchain_core.output_parsers import StrOutputParser
import os
from dotenv import load_dotenv
from third_parties.linkedin import scrape_linkedin_profile



if __name__ == "__main__":
    load_dotenv()  
    api_key = os.getenv('OPENAI_API_KEY')
    print("Hello Langchain")

    summary_template = """
        given the information {information} about a person from I want you to create:
        1. a short summary
        2. two interesting facts about them
"""

    summary_prompt_template = PromptTemplate(input_variables="information", template=summary_template)

    # llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo")
    llm = ChatOllama(model="llama3")
    chain = summary_prompt_template | llm 
    linkedin_data = scrape_linkedin_profile(linkedin_profile_url="https://www.linkedin.com/in/rojandahal/")
    res = chain.invoke({"information": linkedin_data})

    print(res)