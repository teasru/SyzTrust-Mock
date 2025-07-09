import random
import hashlib

def get_fake_feedback(payload):
    branch_coverage = random.randint(0, 50)
    state = hashlib.sha256(str(payload).encode()).hexdigest()[:8]
    crashed = random.random() < 0.1
    return {
        "branch_coverage": branch_coverage,
        "state_hash": state,
        "crashed": crashed
    }
