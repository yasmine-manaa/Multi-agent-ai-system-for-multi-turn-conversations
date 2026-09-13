from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from pydantic import BaseModel, Field

load_dotenv()

# 1. On définit la "forme" attendue de la réponse du LLM
class IntentResult(BaseModel):
    intent: str = Field(description="Intention détectée, ex: learning_support, question_generale, plainte")
    task_type: str = Field(description="Type de tâche demandée, brève description")
    missing_information: list[str] = Field(description="Liste des informations manquantes pour bien répondre, vide si rien ne manque")

# 2. On crée le LLM et on le "force" à répondre selon la structure IntentResult
llm = ChatGoogleGenerativeAI(model="gemini-3.6-flash", temperature=0)
llm_structured = llm.with_structured_output(IntentResult)

def analyze_intent(user_message: str, conversation_history: list[str] = None) -> IntentResult:
    """L'Intent Agent : analyse le message et détecte l'intention + infos manquantes."""
    history_text = "\n".join(conversation_history) if conversation_history else "Aucun historique."
    
    prompt = f"""Tu es un agent d'analyse d'intention dans un système conversationnel.
Historique de la conversation :
{history_text}

Message actuel de l'utilisateur :
"{user_message}"

Analyse ce message et détermine :
1. L'intention principale de l'utilisateur.
2. Le type de tâche demandée.
3. Les informations qui manquent pour pouvoir y répondre correctement (liste vide si tout est clair).
"""
    return llm_structured.invoke(prompt)

if __name__ == "__main__":
    resultat = analyze_intent("Aide-moi avec mon devoir")
    print("Intention :", resultat.intent)
    print("Type de tâche :", resultat.task_type)
    print("Infos manquantes :", resultat.missing_information)
