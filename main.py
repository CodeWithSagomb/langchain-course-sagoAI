from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
import os

load_dotenv()

def main():
    print("Hello from langchain-course!")
    informion="""
Elon Musk (prononcé en anglais : /ˈiːlɒn ˈmʌsk/), né le 28 juin 1971 à Pretoria (Afrique du Sud), est un entrepreneur, homme d'affaires international, chef d'entreprise, homme politique et milliardaire sud-africain, canadien et américain. Avec une fortune personnelle estimée à 407,5 milliards de dollars le 18 juillet 2025[1], il est considéré comme la personne la plus riche du monde.

C'est le cofondateur et le président-directeur général de la société astronautique SpaceX ainsi que le directeur général de la société automobile Tesla. En janvier 2021, selon Bloomberg, Elon Musk devient, à 49 ans, l'individu le plus riche du monde avec une fortune estimée à 251,3 milliards de dollars. En octobre 2022, il devient le propriétaire de Twitter par un achat à 44 milliards de dollars, qu'il renomme X l'année suivante.

Il commence sa carrière en affaires comme cofondateur de la société de logiciels Zip2 avec son frère, Kimbal Musk. La start-up est acquise par Compaq pour 307 millions de dollars en 1999. La même année, Musk cofonde la banque en ligne X.com, qui fusionne avec Confinity en 2000 pour former PayPal. eBay rachète PayPal en 2002 pour 1,5 milliard de dollars.

En 2002, Musk fonde SpaceX, un fabricant aérospatial et une société de services de transport spatial, et en est le PDG. En 2004, il investit 6,5 millions de dollars dans le constructeur de véhicules électriques Tesla, en devient le premier actionnaire et intègre son conseil d'administration, avant de prendre le poste de PDG en 2008. En 2006, il participe à la création de SolarCity, une société d'énergie solaire qui est ensuite acquise par Tesla et devient Tesla Energy. En 2015, il cofonde et devient coprésident d'OpenAI, une association de recherche promouvant l'intelligence artificielle amicale, qu'il quitte en 2018. En 2016, il fonde The Boring Company, société de construction de tunnels, et Neuralink, société de neurotechnologie.

En 2018, Elon Musk est l'objet d'une enquête de la Securities and Exchange Commission (SEC) en raison d'annonces faites sur X susceptibles d'influencer le cours de bourse de Tesla. En 2023, il fonde la société xAI dans le domaine de l'intelligence artificielle.

À partir de la fin des années 2010, ses actions et déclarations, dont certaines relèvent de la désinformation et des théories du complot, sont régulièrement médiatisées.

Politiquement, Elon Musk devient un temps conseiller officieux du nouveau président des États-Unis Donald Trump en 2016, jusqu'à ce que le président républicain annonce son intention de se retirer de l'accord de Paris sur le climat. Alors que ses positions s'orientent progressivement vers l'extrême droite et un soutien à plusieurs figures de ce mouvement au cours des années suivantes, il devient l'un des plus importants soutiens de l'ancien président et s'implique dans sa campagne pour l'élection présidentielle de 2024, devenant son deuxième plus gros contributeur financier.

À la suite de la victoire de Donald Trump, il est nommé haut conseiller et prend la tête d'un « ministère de l'Efficacité gouvernementale », officiellement une instance temporaire appelée département de l'Efficacité gouvernementale, qui consiste à procéder à des coupes drastiques de nombreux programmes et agences gouvernementaux et à licencier des dizaines de milliers de salariés fédéraux. Après seulement quatre mois, il quitte la direction du département de l'Efficacité gouvernementale et entre dans un violent conflit avec Donald Trump au sujet de sa politique fiscale.

Dans le cadre d'une critique du bipartisme aux États-Unis, Elon Musk annonce vouloir créer son propre parti politique. Nommé le Parti de l'Amérique, il tente de constituer une troisième voie aux futures élections américaines. Il projette par ailleurs son influence sur les pays européens, apportant publiquement son soutien à des partis d'extrême droite européens.
  """
    summary_template="""
    given the informion {information} about a person I want you to create:
    1  a short summary of this person in French
    2. two interesting facts about him in French
    3. his top 5 skills in French
    """

    summary_prompt_template=PromptTemplate(
        input_variables=["information"],
        template=summary_template
    )

    Api_key = os.getenv("OPENAI_API_KEY")
    llm = ChatOpenAI(openai_api_base="https://openrouter.ai/api/v1",
        openai_api_key=Api_key,
        model="gpt-4o",
        temperature=0.7)
    chain = summary_prompt_template | llm
    response = chain.invoke({"information":informion})
    print(response.content)







if __name__ == "__main__":
    main()




