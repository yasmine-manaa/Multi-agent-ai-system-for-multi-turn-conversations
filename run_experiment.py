import csv
from scenarios import SCENARIOS
from baseline import baseline_answer
from graph import app

def run_multi_agent(message: str):
    state = {
        "user_goal": None,
        "current_intent": None,
        "missing_information": [],
        "conversation_history": [message],
        "agent_actions": [],
        "evaluation_score": None,
        "final_response": None,
    }
    result = app.invoke(state)
    return result

def main():
    rows = []
    for scenario in SCENARIOS:
        msg = scenario["message"]
        print(f"--- Scénario {scenario['id']}: {msg} ---")

        # Baseline
        baseline_resp = baseline_answer(msg)

        # Multi-agent
        ma_result = run_multi_agent(msg)

        rows.append({
            "id": scenario["id"],
            "message": msg,
            "baseline_response": baseline_resp,
            "multi_agent_response": ma_result["final_response"],
            "multi_agent_intent": ma_result["current_intent"],
            "missing_information": ";".join(ma_result["missing_information"]),
            "evaluation_score": ma_result["evaluation_score"],
            "agent_actions": " | ".join(ma_result["agent_actions"]),
        })

    with open("results.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)

    print("\nTerminé. Résultats sauvegardés dans results.csv")

if __name__ == "__main__":
    main()
