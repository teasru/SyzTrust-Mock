import random
import json
import os
import argparse
import matplotlib.pyplot as plt
from mock_runtime.mock_executor import execute_testcase

parser = argparse.ArgumentParser(description="Run mock SyzTrust fuzzer")
parser.add_argument("--iterations", type=int, default=50, help="Number of fuzzing iterations")
args = parser.parse_args()

NUM_ITERATIONS = args.iterations
LOG_FILE = "results/results_log.json"
CRASH_DIR = "results/crashes"
GRAPH_PATH = "results/state_coverage.png"

os.makedirs("results", exist_ok=True)
os.makedirs(CRASH_DIR, exist_ok=True)

with open("mock_runtime/syscall_templates.json") as f:
    templates = json.load(f)

seen_states = set()
log_data = []
crash_files = []

for i in range(NUM_ITERATIONS):
    testcase = random.sample(templates, 3)
    result = execute_testcase(testcase)

    state = result['state_hash']
    seen_states.add(state)

    # Save crash
    if result['crashed']:
        crash_file = f"{CRASH_DIR}/crash_{state}.json"
        with open(crash_file, "w") as cf:
            json.dump(testcase, cf, indent=2)
        crash_files.append(crash_file)

    log_entry = {
        "iteration": i,
        "state_hash": state,
        "branch_coverage": result['branch_coverage'],
        "crashed": result['crashed']
    }
    log_data.append(log_entry)

    print(f"#{i:02d} | Branches: {result['branch_coverage']:>2} | State: {state} | Crash: {result['crashed']}")

with open(LOG_FILE, "w") as lf:
    json.dump(log_data, lf, indent=2)

plt.figure(figsize=(10, 5))
plt.plot(range(NUM_ITERATIONS), [len(set(d['state_hash'] for d in log_data[:i+1])) for i in range(NUM_ITERATIONS)])
plt.title("Unique State Hashes Over Time")
plt.xlabel("Iteration")
plt.ylabel("Unique States Seen")
plt.grid(True)
plt.tight_layout()
plt.savefig(GRAPH_PATH)
print(f"\n📈 Graph saved to: {GRAPH_PATH}")

if crash_files:
    print(f"\n {len(crash_files)} crash{'es' if len(crash_files) > 1 else ''} found!")
    print("Crash files:")
    for path in crash_files:
        print(f" - {path}")
else:
    print("\n No crashes detected.")
