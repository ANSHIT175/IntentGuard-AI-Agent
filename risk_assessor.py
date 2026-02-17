"""
Risk Assessor
Assigns risk score based on intent
"""

def assess_risk(intent: str) -> dict:
    if intent == "SENSITIVE":
        return {
            "risk_level": "HIGH",
            "risk_score": 85
        }

    return {
        "risk_level": "LOW",
        "risk_score": 10
    }

