# SyzTrust Mock Fuzzer

This is a **simulated version** of the SYZTRUST fuzzing framework, originally designed for Trusted OSes on IoT devices, adapted for **software-only environments** (e.g., Windows/Linux laptops) with **no hardware**.

## 🔍 Features

- Syscall-based test case generation (simulated GP TEE API)
- Composite feedback (code + state coverage)
- Simulated crash detection
- Looped fuzzing with state/branch tracking
- CLI mode with visualized state coverage graph

## ▶️ How to Run

```bash
python main.py
```

The fuzzer will:
- Run 50 iterations of fuzzing
- Save results in `results/results_log.json`
- Save crashing inputs in `results/crashes/`
- Plot unique state hash growth in `results/state_coverage.png`

## 📂 Structure

- `main.py`: CLI fuzzer
- `mock_runtime/`: Mock syscall executor & feedback generator
- `results/`: Logs, graphs, and crash data

## 📈 Sample Output

```
#00 | Branches: 45 | State: d3c1af6e | Crash: False
#01 | Branches: 10 | State: 9083ff17 | Crash: False
...
Graph saved to: results/state_coverage.png
```

---

## 🎓 Educational Use

This repo is perfect for:
- Operating Systems courses
- Fuzzing framework demos
- Security research prototypes

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).
