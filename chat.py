from graph import app

def run_conversation():
    state = {
        "user_goal": None,
        "current_intent": None,
        "missing_information": [],
        "conversation_history": [],
        "agent_actions": [],
        "evaluation_score": None,
        "final_response": None,
    }

    print("=== Conversation avec le système multi-agent (tape 'quit' pour arrêter) ===\n")

    while True:
        user_input = input("Toi : ").strip()
        if user_input.lower() in ("quit", "exit"):
            break

        # Ajoute le message de l'utilisateur à l'historique du state
        state["conversation_history"].append(f"Utilisateur: {user_input}")
        # Réinitialise les champs qui doivent être recalculés à chaque tour
        state["missing_information"] = []
        state["evaluation_score"] = None
        state["final_response"] = None

        # Fait tourner le graphe sur ce tour
        state = app.invoke(state)

        print(f"Système : {state['final_response']}\n")
        state["conversation_history"].append(f"Système: {state['final_response']}")

    print("\n--- LOG COMPLET DES ACTIONS ---")
    for action in state["agent_actions"]:
        print(action)

if __name__ == "__main__":
    run_conversation()
