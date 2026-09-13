def mock_analyze_intent(user_message: str, conversation_history: list[str] = None):
    """Simulation de l'Intent Agent"""
    if "devoir" in user_message.lower() and "maths" not in user_message.lower():
        return {
            "intent": "learning_support",
            "task_type": "aide aux devoirs",
            "missing_information": ["matière", "niveau scolaire", "sujet précis"]
        }
    elif "maths" in user_message.lower() or "dérivées" in user_message.lower():
        return {
            "intent": "learning_support",
            "task_type": "explication mathématique",
            "missing_information": []
        }
    else:
        return {
            "intent": "question_generale",
            "task_type": "question générale",
            "missing_information": []
        }

def mock_ask_clarification(missing_information: list[str], user_message: str):
    """Simulation du Clarification Agent"""
    if missing_information:
        return f"Pourrais-tu me préciser : {', '.join(missing_information)} ?"
    return ""

def mock_generate_response(user_message: str, intent: str, conversation_history: list[str] = None):
    """Simulation du Response Agent"""
    if "dérivées" in user_message.lower():
        return "Les dérivées mesurent comment une fonction change. Par exemple, la dérivée de x² est 2x. Elles sont utiles pour trouver les pentes et optimiser des fonctions."
    elif "maths" in user_message.lower():
        return "Je peux t'aider en maths ! Quel chapitre te pose problème ?"
    else:
        return "Je suis là pour t'aider. Peux-tu me donner plus de détails sur ce que tu souhaites ?"

def run_demo_conversation():
    """Simulation d'une conversation multi-tours avec human-in-the-loop"""
    state = {
        "user_goal": None,
        "current_intent": None,
        "missing_information": [],
        "conversation_history": [],
        "agent_actions": [],
        "evaluation_score": None,
        "final_response": None,
    }

    print("=== DÉMO CONVERSATION MULTI-TOURS (SIMULATION) ===\n")

    # Tour 1: Message vague qui déclenche clarification
    user_input = "Aide-moi avec mon devoir"
    print(f"Toi : {user_input}")
    
    state["conversation_history"].append(f"Utilisateur: {user_input}")
    
    # Intent Agent (simulé)
    intent_result = mock_analyze_intent(user_input, state["conversation_history"])
    state["current_intent"] = intent_result["intent"]
    state["missing_information"] = intent_result["missing_information"]
    state["agent_actions"].append(f"Intent Agent -> intent={intent_result['intent']}, missing={intent_result['missing_information']}")
    
    # Router: vers clarification ou response
    if state["missing_information"]:
        # Clarification Agent (simulé)
        question = mock_ask_clarification(state["missing_information"], user_input)
        state["final_response"] = question
        state["agent_actions"].append("Clarification Agent -> question posée")
    else:
        # Response Agent (simulé)
        response = mock_generate_response(user_input, state["current_intent"], state["conversation_history"])
        state["final_response"] = response
        state["agent_actions"].append("Response Agent -> réponse générée")
    
    print(f"Système : {state['final_response']}\n")
    state["conversation_history"].append(f"Système: {state['final_response']}")

    # Tour 2: Réponse de l'utilisateur avec les infos manquantes
    user_input = "C'est en maths, niveau lycée, sur les dérivées"
    print(f"Toi : {user_input}")
    
    state["conversation_history"].append(f"Utilisateur: {user_input}")
    
    # Intent Agent (simulé) avec historique complet
    intent_result = mock_analyze_intent(user_input, state["conversation_history"])
    state["current_intent"] = intent_result["intent"]
    state["missing_information"] = intent_result["missing_information"]
    state["agent_actions"].append(f"Intent Agent -> intent={intent_result['intent']}, missing={intent_result['missing_information']}")
    
    # Router: vers clarification ou response
    if state["missing_information"]:
        # Clarification Agent (simulé)
        question = mock_ask_clarification(state["missing_information"], user_input)
        state["final_response"] = question
        state["agent_actions"].append("Clarification Agent -> question posée")
    else:
        # Response Agent (simulé)
        response = mock_generate_response(user_input, state["current_intent"], state["conversation_history"])
        state["final_response"] = response
        state["agent_actions"].append("Response Agent -> réponse générée")
    
    print(f"Système : {state['final_response']}\n")
    state["conversation_history"].append(f"Système: {state['final_response']}")

    print("--- LOG COMPLET DES ACTIONS ---")
    for action in state["agent_actions"]:
        print(action)

if __name__ == "__main__":
    run_demo_conversation()
