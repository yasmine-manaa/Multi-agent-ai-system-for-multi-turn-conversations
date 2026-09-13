from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()
llm = ChatGoogleGenerativeAI(model="gemini-3.6-flash", temperature=0.3)

def baseline_answer(user_message: str) -> str:
    """Baseline : un seul LLM répond directement, sans agents ni state."""
    reponse = llm.invoke(user_message)
    
    # Gérer le format de réponse qui peut être une liste
    if isinstance(reponse.content, list) and len(reponse.content) > 0:
        for item in reponse.content:
            if isinstance(item, dict) and 'text' in item:
                return item['text']
    return reponse.content

if __name__ == "__main__":
    question = "Peux-tu m'aider avec mon devoir de maths ?"
    print(baseline_answer(question))
