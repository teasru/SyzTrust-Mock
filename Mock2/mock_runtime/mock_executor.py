import random
from .mock_feedback import get_fake_feedback

def execute_testcase(payload):
    print(f"Executing syscall sequence: {payload}")
    return get_fake_feedback(payload)
