"""
Runtime Policy Enforcement Engine
"""

import json

def load_policies():
    with open("policies.json", "r") as file:
        return json.load(file)

def evaluate_policy(intent: str, risk: dict, policies: dict) -> dict:
    if risk["risk_level"] == "HIGH" and policies["block_high_risk"]:
        return {
            "decision": "BLOCKED",
            "reason": "High-risk intent blocked by runtime security policy"
        }

    return {
        "decision": "ALLOWED",
        "reason": "Intent approved under active policy rules"
    }

