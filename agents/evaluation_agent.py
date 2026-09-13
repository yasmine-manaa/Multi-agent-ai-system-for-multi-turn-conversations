from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from pydantic import BaseModel, Field

load_dotenv()

class EvaluationResult(BaseModel):
    relevance_score: float = Field(description="Score de pertinence entre 0 et 1")
    is_acceptable: bool = Field(description="True si la réponse est acceptable, False sinon")
    justification: str = Field(description="Brève justification du score")

llm = ChatGoogleGenerativeAI(model="gemini-3.6-flash", temperature=0)
llm_structured = llm.with_structured_output(EvaluationResult)

def evaluate_response(user_message: str, response: str) -> EvaluationResult:
    prompt = f"""Tu es un agent d'évaluation. Évalue la réponse suivante par rapport à la demande.
Demande de l'utilisateur : "{user_message}"
Réponse générée : "{response}"

Donne un score de pertinence entre 0 et 1, indique si c'est acceptable (seuil 0.7), 
et justifie brièvement."""
    return llm_structured.invoke(prompt)

if __name__ == "__main__":
    result = evaluate_response("Aide-moi en maths sur les dérivées", "Voici comment dériver...")
    print(result)
