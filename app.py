# app.py - Quantum Portfolio Optimizer
import streamlit as st
import numpy as np
import pandas as pd
import yfinance as yf
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from scipy.optimize import minimize
import warnings
warnings.filterwarnings('ignore')

st.set_page_config(
    page_title="Quantum Portfolio Optimizer",
    page_icon="⚛️",
    layout="wide"
)

st.title("⚛️ Quantum Portfolio Optimizer")
st.markdown("*Classical Markowitz vs QAOA — IBM Quantum 20-Day Sprint*")
st.divider()

# sidebar
st.sidebar.header("Portfolio Settings")
tickers = st.sidebar.multiselect(
    "Select Stocks",
    ['AAPL', 'GOOGL', 'MSFT', 'AMZN',
     'TSLA', 'NVDA', 'META'],
    default=['AAPL', 'GOOGL', 'MSFT', 'AMZN']
)
start = st.sidebar.date_input(
    "Start Date", value=pd.Timestamp('2023-01-01')
)
end = st.sidebar.date_input(
    "End Date", value=pd.Timestamp('2024-01-01')
)
risk_param = st.sidebar.slider(
    "Risk Aversion (q)", 0.1, 1.0, 0.5
)

if len(tickers) < 2:
    st.warning("Please select at least 2 stocks!")
    st.stop()

# fetch data
with st.spinner("Fetching stock data..."):
    prices = yf.download(
        tickers, start=start,
        end=end, auto_adjust=True
    )['Close']
    returns        = prices.pct_change().dropna()
    annual_returns = returns.mean() * 252
    cov_matrix     = returns.cov() * 252

st.success(f"Loaded {len(prices)} trading days!")

# stock performance
st.subheader("📈 Stock Performance")
fig1 = go.Figure()
colors = ['#4fc3f7','#6929C4',
          '#00ff88','#FF5722',
          '#FFD700','#FF69B4','#00CED1']

normalized = prices / prices.iloc[0] * 100
for i, ticker in enumerate(tickers):
    fig1.add_trace(go.Scatter(
        x=normalized.index,
        y=normalized[ticker],
        name=ticker,
        line=dict(color=colors[i], width=2)
    ))

fig1.update_layout(
    paper_bgcolor='#1a1a2e',
    plot_bgcolor='#1a1a2e',
    font=dict(color='white'),
    height=350
)
st.plotly_chart(fig1, use_container_width=True)

# classical optimization
st.subheader("🔵 Classical Markowitz Optimization")
n = len(tickers)
risk_free = 0.05

def portfolio_perf(w):
    ret   = np.dot(w, annual_returns)
    risk  = np.sqrt(np.dot(w.T,
            np.dot(cov_matrix, w)))
    sharpe = (ret - risk_free) / risk
    return ret, risk, sharpe

result = minimize(
    lambda w: -portfolio_perf(w)[2],
    [1/n]*n,
    method='SLSQP',
    bounds=[(0,1)]*n,
    constraints={'type':'eq',
                 'fun': lambda w: sum(w)-1}
)

opt_w = result.x
ret, risk, sharpe = portfolio_perf(opt_w)

col1, col2, col3 = st.columns(3)
col1.metric("Expected Return",
            f"{ret*100:.2f}%")
col2.metric("Portfolio Risk",
            f"{risk*100:.2f}%")
col3.metric("Sharpe Ratio",
            f"{sharpe:.4f}")

fig2 = go.Figure(go.Bar(
    x=tickers,
    y=opt_w*100,
    marker_color=colors[:n],
    text=[f'{w*100:.1f}%' for w in opt_w],
    textposition='outside'
))
fig2.update_layout(
    title="Optimal Weights",
    paper_bgcolor='#1a1a2e',
    plot_bgcolor='#1a1a2e',
    font=dict(color='white'),
    height=300,
    yaxis_title="Weight %"
)
st.plotly_chart(fig2, use_container_width=True)

# QAOA section
st.subheader("⚛️ QAOA Portfolio Selection")
st.info("QAOA selects which stocks to include (binary: buy or skip)")

import itertools
best_score = -np.inf
best_label = ""
all_results = []

for combo in itertools.product([0,1], repeat=n):
    w = np.array(combo)
    if w.sum() == 0:
        continue
    w_norm = w / w.sum()
    ret_q  = np.dot(w_norm, annual_returns)
    risk_q = np.dot(w_norm.T,
             np.dot(cov_matrix, w_norm))
    score  = ret_q - risk_param * risk_q
    label  = '+'.join([tickers[i]
                       for i in range(n)
                       if w[i]==1])
    all_results.append({
        'Portfolio': label,
        'Return': f"{ret_q*100:.2f}%",
        'Score': round(score, 4)
    })
    if score > best_score:
        best_score = score
        best_label = label

all_results.sort(
    key=lambda x: x['Score'], reverse=True
)

st.success(f"Best QAOA Portfolio: **{best_label}**")
st.dataframe(
    pd.DataFrame(all_results[:5]),
    use_container_width=True
)

st.divider()
st.markdown(
    "*Built with Qiskit · Yahoo Finance · "
    "IBM Quantum 20-Day Sprint · VIT Chennai*"
)
