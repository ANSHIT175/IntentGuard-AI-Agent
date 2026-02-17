"""
IntentGuard Main Application
Implements intent-aware, policy-driven AI agent control
"""

from intent_analyzer import analyze_intent
from risk_assessor import assess_risk
from policy_engine import load_policies, evaluate_policy
from action_simulator import simulate_action
from action_executor import execute_action
from audit_logger import log_decision

def main():
    print("=== IntentGuard: Safe Autonomous Agent Execution ===\n")

    user_input = input("Enter autonomous agent instruction: ")

    # Step 1: Intent Understanding
    intent = analyze_intent(user_input)

    # Step 2: Risk Assessment
    risk = assess_risk(intent)

    # Step 3: Policy Enforcement
    policies = load_policies()
    decision = evaluate_policy(intent, risk, policies)

    # Step 4: Pre-execution Simulation
    simulation_result = simulate_action(decision)

    # Step 5: Controlled Execution
    execution_result = execute_action(decision)

    # Step 6: Audit Logging
    log_decision(user_input, intent, risk, decision)

    # Final Output
    print("\n--- IntentGuard Decision Report ---")
    print(f"Intent Detected : {intent}")
    print(f"Risk Level     : {risk['risk_level']} ({risk['risk_score']})")
    print(f"Decision       : {decision['decision']}")
    print(f"Reason         : {decision['reason']}")
    print(f"Simulation     : {simulation_result}")
    print(f"Execution      : {execution_result}")

if __name__ == "__main__":
    main()
  
