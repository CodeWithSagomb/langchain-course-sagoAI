from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
import os
load_dotenv()


def main():
    print("Hello from langchain-course!")
    Api_key = os.getenv("OPENAI_API_KEY")

    llm = ChatOpenAI(openai_api_base="https://openrouter.ai/api/v1",
        openai_api_key=Api_key,
        model="gpt-4o",
        temperature=0.7
    )
    # creation d'un prompt template
    prompt_template = ChatPromptTemplate.from_messages(
        [
            ("system", "Tu es un assistant expert en IA générative. Réponds à toutes les questions en tant que tel."),
            ("human", "Explique ce qu'est LangChain en une phrase."),
        ]
    )

    # 3. Création de la Chaîne
    output_parser = StrOutputParser()
    chain = prompt_template | llm | output_parser

    # 4. Exécution de la Chaîne
    response = chain.invoke({}) # On ne passe rien car le prompt est statique pour le moment
    print(response)





if __name__ == "__main__":
    main()

