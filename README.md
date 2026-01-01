# CivicPulse AI

CivicPulse AI is an AI-powered civic intelligence backend designed to help urban authorities and citizens prioritize, analyze, and respond to civic issues using data-driven insights.

---

## 🚨 Problem Statement

Urban local bodies receive thousands of civic complaints during monsoon seasons and peak urban activity periods.  
However, decision-makers lack:
- Prioritization mechanisms
- Ward-level intelligence
- Risk-based resource allocation

This leads to delayed responses, repeated failures, and reactive governance.

---

## 💡 Solution Overview

CivicPulse AI transforms raw civic complaints into actionable governance intelligence by:
- Automatically classifying complaint severity
- Aggregating ward-level analytics
- Predicting flood risk
- Computing a unified **Ward Risk Index**

This enables proactive, data-driven urban governance.

---

## 🧠 Core Features

- 📋 Civic Complaints Management
- ⚠️ AI-based Severity Classification
- 🌧️ Flood Risk Prediction
- 📊 Ward-wise Analytics
- 🚨 Unified Ward Risk Index
- 📚 Auto-generated API Documentation

---

## 🏗️ System Architecture
# CivicPulse AI

CivicPulse AI is an AI-powered civic intelligence backend designed to help urban authorities and citizens prioritize, analyze, and respond to civic issues using data-driven insights.

---

## 🚨 Problem Statement

Urban local bodies receive thousands of civic complaints during monsoon seasons and peak urban activity periods.  
However, decision-makers often lack:

- Effective prioritization mechanisms  
- Ward-level risk visibility  
- Data-driven resource allocation  

This results in delayed responses and reactive governance.

---

## 💡 Solution Overview

CivicPulse AI converts raw civic complaints into actionable governance intelligence by:

- Automatically classifying complaint severity  
- Aggregating ward-wise analytics  
- Predicting flood risk  
- Computing a unified **Ward Risk Index**

This enables proactive, transparent, and data-driven urban governance.

---

## 🧠 Core Features

- 📋 Civic Complaints Management  
- ⚠️ AI-based Severity Classification  
- 🌧️ Flood Risk Prediction  
- 📊 Ward-wise Analytics  
- 🚨 Unified Ward Risk Index  
- 📚 Auto-generated API Documentation (Swagger)

---

## 🏗️ System Architecture

Client / Dashboard
|
v
FastAPI Backend (CivicPulse AI)
|
├── Complaints API
├── Severity Engine
├── Flood Risk Engine
├── Analytics Engine
└── Ward Risk Index Engine
|
v
SQLite Database



---

## 🧪 API Modules

| Endpoint | Description |
|--------|------------|
| `/complaints` | Create and list civic complaints |
| `/risk/predict` | Flood risk prediction |
| `/analytics/ward/{ward}` | Ward-wise complaint analytics |
| `/risk-index/ward/{ward}` | Unified ward risk score |

---

## 🛠️ Tech Stack

- **Backend:** FastAPI (Python)  
- **Database:** SQLite + SQLAlchemy  
- **AI / Logic:** Explainable rule-based intelligence  
- **Documentation:** Swagger / OpenAPI  
- **Version Control:** Git & GitHub  

---

## 🚀 Getting Started

### Setup Virtual Environment
```bash
python -m venv venv
venv\Scripts\activate
