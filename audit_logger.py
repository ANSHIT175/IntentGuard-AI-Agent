"""
Audit Logger for Compliance & Traceability
"""

from datetime import datetime

def log_decision(user_input, intent, risk, decision):
    with open("logs/audit_log.txt", "a") as log_file:
        log_file.write(
            f"[{datetime.now()}] "
            f"INPUT='{user_input}' | "
            f"INTENT={intent} | "
            f"RISK={risk['risk_level']}({risk['risk_score']}) | "
            f"DECISION={decision['decision']}\n"
        )
      
