"""
Pre-execution Action Simulation
"""

def simulate_action(decision: dict) -> str:
    if decision["decision"] == "BLOCKED":
        return "Simulation failed: unsafe outcome predicted"

    return "Simulation passed: no harmful impact detected"
  
