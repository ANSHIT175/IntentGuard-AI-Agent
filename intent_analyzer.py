"""
Intent Analyzer
Classifies user intent before execution
"""

def analyze_intent(user_input: str) -> str:
    dangerous_keywords = [
        "transfer", "send money", "bank", "otp",
        "password", "hack", "steal", "bypass",
        "fraud", "account"
    ]

    user_input = user_input.lower()

    for keyword in dangerous_keywords:
        if keyword in user_input:
            return "SENSITIVE"

    return "SAFE"

