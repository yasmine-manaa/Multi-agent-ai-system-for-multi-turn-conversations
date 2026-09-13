from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

llm = ChatGoogleGenerativeAI(model="gemini-3.6-flash", temperature=0.4)

def generate_response(user_message: str, intent: str, conversation_history: list[str] = None) -> str:
    """Le Response/Tutor Agent : génère la réponse finale à l'utilisateur."""
    history_text = "\n".join(conversation_history) if conversation_history else "Aucun historique."
    
    prompt = f"""Tu es un agent qui répond aux demandes de l'utilisateur de façon claire et utile.
Intention détectée : {intent}

Historique de la conversation :
{history_text}

Message de l'utilisateur :
"{user_message}"

Réponds directement et clairement à la demande de l'utilisateur.
"""
    reponse = llm.invoke(prompt)
    
    # Gérer le format de réponse qui peut être une liste
    if isinstance(reponse.content, list) and len(reponse.content) > 0:
        for item in reponse.content:
            if isinstance(item, dict) and 'text' in item:
                return item['text']
    return reponse.content

if __name__ == "__main__":
    reponse = generate_response(
        user_message="Aide-moi en maths, niveau lycée, sur les dérivées",
        intent="learning_support",
        conversation_history=["Utilisateur: Aide-moi avec mon devoir", "Système: Quelle matière et quel niveau ?"]
    )
    print("Réponse générée :\n", reponse)
