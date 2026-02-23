def allowed_action():
    with open("allowed.txt", "w") as f:
        f.write("This action was allowed by IntentGuard")
    return "ALLOWED: File created"

def blocked_action():
    raise PermissionError("BLOCKED: Policy violation")
