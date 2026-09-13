from langgraph.graph import StateGraph, END
from state import ConversationState
from agents.intent_agent import analyze_intent
from agents.clarification_agent import ask_clarification
from agents.response_agent import generate_response
from agents.evaluation_agent import evaluate_response

def intent_node(state: ConversationState) -> ConversationState:
    result = analyze_intent(state["conversation_history"][-1], state["conversation_history"])
    state["current_intent"] = result.intent
    state["missing_information"] = result.missing_information
    state["agent_actions"].append(f"Intent Agent -> intent={result.intent}, missing={result.missing_information}")
    return state

def clarification_node(state: ConversationState) -> ConversationState:
    question = ask_clarification(state["missing_information"], state["conversation_history"][-1])
    state["final_response"] = question
    state["agent_actions"].append("Clarification Agent -> question posée")
    return state

def response_node(state: ConversationState) -> ConversationState:
    answer = generate_response(state["conversation_history"][-1], state["current_intent"], state["conversation_history"])
    state["final_response"] = answer
    state["agent_actions"].append("Response Agent -> réponse générée")
    return state

def evaluation_node(state: ConversationState) -> ConversationState:
    result = evaluate_response(state["conversation_history"][-1], state["final_response"])
    state["evaluation_score"] = result.relevance_score
    state["agent_actions"].append(f"Evaluation Agent -> score={result.relevance_score}")
    return state

def supervisor_router(state: ConversationState) -> str:
    if state["missing_information"]:
        return "clarification"
    return "response"

# Construction du graphe
workflow = StateGraph(ConversationState)
workflow.add_node("intent", intent_node)
workflow.add_node("clarification", clarification_node)
workflow.add_node("response", response_node)
workflow.add_node("evaluation", evaluation_node)

workflow.set_entry_point("intent")
workflow.add_conditional_edges("intent", supervisor_router, {
    "clarification": "clarification",
    "response": "response"
})
workflow.add_edge("clarification", END)   # on attend la réponse de l'utilisateur au tour suivant
workflow.add_edge("response", "evaluation")
workflow.add_edge("evaluation", END)

app = workflow.compile()

if __name__ == "__main__":
    initial_state: ConversationState = {
        "user_goal": None,
        "current_intent": None,
        "missing_information": [],
        "conversation_history": ["Aide-moi avec mon devoir"],
        "agent_actions": [],
        "evaluation_score": None,
        "final_response": None,
    }
    final_state = app.invoke(initial_state)
    print("--- LOG D'ACTIONS ---")
    for action in final_state["agent_actions"]:
        print(action)
    print("--- RÉPONSE FINALE ---")
    print(final_state["final_response"])
