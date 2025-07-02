# ☁️ Cloud Cost Prediction using Machine Learning

A powerful and lightweight machine learning model that predicts **cloud infrastructure cost** based on key resource inputs: CPU, memory, and storage. This helps developers, DevOps engineers, and finance teams estimate spend **before** provisioning resources — enabling **better cost control and planning**.

---

## 🚀 Features

- 🔮 **Predictive ML Model** (Linear Regression)
- 📊 Trained on realistic cloud pricing data
- 🔌 Exposed as a **FastAPI REST API**
- 🧪 Easily testable using Postman or `curl`
- 📁 Simple and extensible project structure
- ✅ MIT Licensed & ready to deploy

---

## 💥 Real-World Impact

### 💡 Why Predict Cloud Costs?

Predicting cloud costs before provisioning infrastructure is like knowing your electricity bill before turning on the appliances.

Cloud pricing is complex — driven by:
- 💻 vCPUs
- 🧠 RAM (GB)
- 💽 Storage (GB)

With this model:
- 📉 Avoid surprise cloud bills
- 🧮 Simulate infra costs for upcoming deployments
- 📈 Align with your budgeting strategy

### 👤 Example Use Case 1: DevOps/Developer Team

> “I need a VM with 8 CPUs, 32 GB RAM, 500 GB storage. What’s the monthly cost?”

Rather than guess, call the API → get estimate → decide → save costs 💰

### 👤 Use Case 2: Product / Finance Team

> “We expect 20,000 new users next month. Can we model cost for scaled infra?”

This tool allows the team to simulate and compare different resource combinations **before provisioning** anything.

---

## 🧠 Technologies Used

| Layer          | Tech                    |
|----------------|-------------------------|
| ML Modeling    | scikit-learn, pandas    |
| API Framework  | FastAPI + Uvicorn       |
| Packaging      | joblib                  |
| Data Source    | CSV (or future AWS Cost Explorer) |
| Language       | Python 3.9+             |

---

## 🗂️ Folder Structure
📁 Folder Structure
<pre> cloud-cost-forecasting/ ├── ml/ │ └── train_model.py # Trains the ML model │ ├── data/ │ └── cloud_cost_data.csv # Sample cloud cost input data │ ├── models/ │ └── cloud_cost_model.pkl # Trained and serialized model │ ├── app.py # FastAPI app to serve predictions ├── requirements.txt # Python package dependencies ├── README.md # Project documentation └── LICENSE # MIT License </pre>
---

## 📄 License

This project is licensed under the **MIT License**.  
See the [LICENSE](./LICENSE) file for more details.

---
## 👩‍💻 Author

**Nikitha** — Passionate about **AI, MLOps & Cloud** technologies.  
Connect on [GitHub](https://github.com/Nikitha1099) or [LinkedIn](https://www.linkedin.com/in/nikitha-pyata-b610b5193/) to collaborate.


---

