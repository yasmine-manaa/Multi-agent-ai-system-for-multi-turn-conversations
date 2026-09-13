from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

llm = ChatGoogleGenerativeAI(model="gemini-3.6-flash", temperature=0.3)

def ask_clarification(missing_information: list[str], user_message: str) -> str:
    """Le Clarification Agent : transforme les infos manquantes en une question claire."""
    infos = ", ".join(missing_information)
    
    prompt = f"""Tu es un agent de clarification dans un système conversationnel.
L'utilisateur a écrit : "{user_message}"

Il manque les informations suivantes pour bien répondre : {infos}

Formule UNE SEULE question claire, courte et naturelle à poser à l'utilisateur 
pour obtenir ces informations manquantes. Ne pose pas plusieurs questions séparées, 
regroupe-les en une seule phrase si possible.
"""
    reponse = llm.invoke(prompt)
    
    # Gérer le format de réponse qui peut être une liste
    if isinstance(reponse.content, list) and len(reponse.content) > 0:
        for item in reponse.content:
            if isinstance(item, dict) and 'text' in item:
                return item['text']
    return reponse.content

if __name__ == "__main__":
    question = ask_clarification(
        missing_information=["matiere_ou_sujet_du_devoir", "niveau_scolaire"],
        user_message="Aide-moi avec mon devoir"
    )
    print("Question de clarification :", question)
