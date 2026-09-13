def decide_next_step(missing_information: list[str], evaluation_score: float = None) -> str:
    """Retourne : 'clarification', 'response', ou 'end'"""
    if missing_information:
        return "clarification"
    if evaluation_score is not None and evaluation_score < 0.7:
        return "response"  # on regénère une réponse
    return "response" if evaluation_score is None else "end"
