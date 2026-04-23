# 📈 Moomoo Quant Scanner (Simple Swing Strategy)

A lightweight quant-style project using the Moomoo OpenAPI (OpenD) to scan US stocks for **momentum + potential short squeeze setups**, generate a **daily HTML report**, and prepare for **Telegram alerts**.

---

## 🚀 What This Project Does

- Connects to Moomoo OpenD (local API bridge)
- Scans a watchlist of US stocks

## 🧠 Strategy Overview

Start with premarket change scanner

## Quick Start

1. Install & run Moomoo OpenD

Download Moomoo desktop and enable OpenAPI:

https://openapi.moomoo.com/moomoo-api-doc/en/intro/intro.html#6105

Run OpenD locally (default):

## ▶️ Run the Scanner

```
python main.py
```

## 🔥 Roadmap (Next Upgrades)

- Telegram alerts (daily report)
- Volume ratio using historical data
- Short interest integration (squeeze signal)
- Trade logging + PnL tracking
- Web dashboard (React / Streamlit)
- Auto execution (only after proven backtesting edge)
