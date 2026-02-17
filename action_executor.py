"""
Controlled Action Executor
"""

def execute_action(decision: dict) -> str:
    if decision["decision"] == "BLOCKED":
        return "❌ Execution stopped to prevent unsafe action"

    return "✅ Action executed successfully"

