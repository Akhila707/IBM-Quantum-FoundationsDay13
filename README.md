# Quantum Portfolio Optimizer — Project 2

<div align="center">

![IBM Quantum](https://img.shields.io/badge/IBM%20Quantum-052FAD?style=flat-square&logo=ibm&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat-square&logo=streamlit&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly-3F4F75?style=flat-square&logo=plotly&logoColor=white)
![Yahoo Finance](https://img.shields.io/badge/Yahoo%20Finance-720E9E?style=flat-square&logoColor=white)
![Python 3.10](https://img.shields.io/badge/Python%203.10-1a1a2e?style=flat-square&logo=python&logoColor=4fc3f7)
![Day 13](https://img.shields.io/badge/Day%2013-Complete-4fc3f7?style=flat-square)
![Live](https://img.shields.io/badge/Live-Streamlit%20App-00ff88?style=flat-square)

</div>

<br/>

<div align="center">

### 🚀 [Live Demo → quantum-portfolio-optimizer.streamlit.app](https://quantum-portfolio-optimizer.streamlit.app)

<i>Project 2 of 3 · IBM Quantum 20-Day Learning Sprint · VIT Chennai</i>

</div>

---

## Overview

**Project 2** polishes the Day 12 Quantum Portfolio Optimizer into a fully deployed, interactive web application. Users can select stocks, adjust risk parameters, and compare Classical Markowitz vs QAOA results in real time — all powered by live Yahoo Finance data.

| Feature | Day 12 | Day 13 |
|---------|--------|--------|
| Notebook | ✅ | ✅ |
| Matplotlib plots | ✅ | ✅ |
| Plotly interactive charts | ❌ | ✅ |
| Streamlit web app | ❌ | ✅ |
| Live deployment | ❌ | ✅ |
| Stock selector | ❌ | ✅ |
| Risk slider | ❌ | ✅ |

---

## Live App

```
URL   : https://quantum-portfolio-optimizer.streamlit.app
Stocks: AAPL · GOOGL · MSFT · AMZN · TSLA · NVDA · META
Data  : Live from Yahoo Finance
```

Features:
- Select any combination of 7 major stocks
- Adjust date range and risk aversion parameter
- View normalized price history (interactive)
- Get Classical Markowitz optimal weights instantly
- See QAOA top portfolio selections with scores

---

## The Problem

Portfolio optimization: given a set of assets, find the allocation that maximizes risk-adjusted returns.

```
Classical (Markowitz, 1952):
  maximize  w^T·μ - q·w^T·Σ·w
  subject to: Σwᵢ = 1,  wᵢ ≥ 0

QAOA (quantum):
  binary selection — buy or skip each stock
  |1⟩ = include · |0⟩ = exclude
  2^N combinations explored simultaneously
```

---

## Results (AAPL · GOOGL · MSFT · AMZN · 2023)

### Classical Markowitz

```
AAPL  :  60.39%  ← largest allocation
GOOGL :  21.82%
MSFT  :   0.00%  ← excluded
AMZN  :  17.79%

Expected return :  50.57%
Sharpe ratio    :   2.3079
```

### QAOA Top Portfolios

```
Portfolio              Score
──────────────────────────────
GOOGL                  0.5784  ← best score
GOOGL+AMZN             0.5314
GOOGL+MSFT             0.5269
AAPL+GOOGL             0.5218
GOOGL+MSFT+AMZN        0.5127
```

---

## Why Quantum Finance?

```
Classical portfolio optimization:
  N assets → exact solution polynomial for small N
  N = 50+  → computationally intensive
  N = 1000+ → approximation required

QAOA:
  N assets → N qubits
  Explores 2^N combinations in superposition
  Scales naturally with quantum hardware
  Current hardware: NISQ era (noisy, small scale)
  Future hardware: potential exponential advantage
```

Goldman Sachs, JPMorgan, and Fidelity have active quantum finance research programs. This project demonstrates the core algorithm behind their work.

---

## Tech Stack

```python
streamlit           # web app framework
yfinance            # real stock data
plotly              # interactive visualizations
scipy               # classical optimization (SLSQP)
numpy               # numerical operations
pandas              # data manipulation
qiskit              >= 2.0.0
qiskit-aer          >= 0.17.2
```

---

## Run Locally

```bash
git clone https://github.com/Akhila707/IBM-Quantum-FoundationsDay13.git
cd IBM-Quantum-FoundationsDay13
pip install -r requirements.txt
streamlit run app.py
```

Open `http://localhost:8501` in your browser.

---

## Project Structure

| Path | Description |
|------|-------------|
| `app.py` | Streamlit web application |
| `notebooks/01_quantum_portfolio.ipynb` | Research notebook |
| `results/stock_performance.png` | Static performance plots |
| `results/portfolio_comparison.png` | Comparison plots |
| `requirements.txt` | Dependencies |

---

## Sprint Progress

```
Day 01  ──  ✅  Qiskit setup · Hello Quantum
Day 02  ──  ✅  Superposition · Entanglement
Day 03  ──  ✅  Gates deep-dive · Grover's
Day 04  ──  ✅  VQE · COBYLA optimizer
Day 05  ──  ✅  QAOA · MaxCut
Day 06  ──  ✅  Quantum Error Mitigation · ZNE
Day 07  ──  ✅  Real IBM hardware · ibm_torino
Day 08  ──  ✅  QSVM · ZZFeatureMap
Day 09  ──  ✅  VQC · Variational Classifier
Day 10  ──  ✅  Project 1 · QML Classifier · MNIST · v1.0
Day 11  ──  ✅  Quantum-Safe Cryptography · LWE · NIST PQC
Day 12  ──  ✅  Quantum Portfolio · QAOA · real stock data
Day 13  ──  ✅  Project 2 · Streamlit deployed · live demo
Day 14  ──   ✅Quantum Harmonic Oscillator — Ground State Energy via VQE
·
·
Day 20  ──  ·   Final push
```

---

## Security

- No API keys required
- Yahoo Finance is publicly accessible
- No user data stored or transmitted

---

<div align="center">

[![Live Demo](https://img.shields.io/badge/Live%20Demo-quantum--portfolio--optimizer.streamlit.app-FF4B4B?style=flat-square&logo=streamlit)](https://quantum-portfolio-optimizer.streamlit.app)

[![GitHub](https://img.shields.io/badge/Akhila707-181717?style=flat-square&logo=github)](https://github.com/Akhila707)
&nbsp;·&nbsp;
[![IBM Quantum](https://img.shields.io/badge/IBM%20Quantum-052FAD?style=flat-square&logo=ibm&logoColor=white)](https://quantum.ibm.com)

</div>
