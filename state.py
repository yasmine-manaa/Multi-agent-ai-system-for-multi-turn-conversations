from typing import TypedDict, List, Optional

class ConversationState(TypedDict):
    user_goal: Optional[str]              # objectif global de l'utilisateur
    current_intent: Optional[str]         # intention détectée au tour actuel
    missing_information: List[str]        # infos qui manquent encore
    conversation_history: List[str]       # historique des messages (utilisateur + système)
    agent_actions: List[str]              # journal des actions des agents (pour l'audit log)
    evaluation_score: Optional[float]     # score donné par l'Evaluation Agent
    final_response: Optional[str]         # réponse finale envoyée à l'utilisateur
