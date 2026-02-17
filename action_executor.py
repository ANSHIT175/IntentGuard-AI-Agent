"""
Controlled Action Executor
"""

def execute_action(decision: dict) -> str:
    """
    Executes action only if policy engine allows it.
    """
    if decision["decision"] == "BLOCKED":
        return "❌ Execution blocked: Unsafe or non-compliant action detected"

    if decision["decision"] == "FLAGGED":
        return "⚠️ Execution flagged: Requires human review"

    return "✅ Execution allowed: Action performed safely"
