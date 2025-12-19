# Personalized Financial Assistance And Product Recommendation System Using Large Language Models

> **Wells Fargo I&P Hackathon 2025** | Team Neural Nexus

A hybrid recommendation system combining **collaborative filtering**, **vector similarity search**, and **Large Language Models (LLMs)** to deliver personalized, explainable financial product recommendations.

---

## Problem Statement

Traditional banking recommendation systems rely on rule-based filtering or basic collaborative filtering, which often fail to:
- Capture **semantic relationships** between user needs and products
- Provide **explainable** recommendations that build customer trust
- Handle the **cold-start problem** for new users with limited transaction history

---

## Solution

We built a **hybrid AI recommendation engine** that combines three approaches:

| Approach | Implementation | Purpose |
|----------|---------------|---------|
| **Collaborative Filtering** | k-NN vector search on user embeddings | Find similar customers |
| **Content-Based Filtering** | Semantic search on product embeddings | Match products to user context |
| **LLM Reasoning** | DeepSeek R1 + Mistral-7B | Generate explainable recommendations |

---

## System Architecture

<img width="382" height="536" alt="image" src="https://github.com/user-attachments/assets/36084f0f-6825-4255-83d8-134c4da499f7" />


---

## Key Features

### 1. Hybrid Recommendation Engine
- **Collaborative Filtering**: Identifies similar users via k-NN search on 22-attribute customer embeddings
- **RAG Pipeline**: Retrieves relevant products from vector DB, then generates contextual recommendations via LLM

### 2. Multi-LLM Orchestration
- **DeepSeek R1-Distill-Llama-8B**: Financial Q&A and reasoning tasks
- **Mistral-7B-Instruct**: Transaction summarization and synthesis
- **Task-specific routing**: Each model handles what it does best

### 3. Behavioral Analysis
- Periodic batch jobs summarize transaction histories into user personas
- LLM-generated insights capture spending patterns and financial behaviors
- Summaries improve recommendation relevance over time

### 4. News Recommendation
- Topic extraction from user content using LLMs
- Real-time financial news fetching via NewsAPI
- Personalized article suggestions based on detected interests

---

## 🛠️ Tech Stack

| Category | Technologies |
|----------|-------------|
| **LLMs** | DeepSeek R1-Distill-Llama-8B, Mistral-7B-Instruct-v0.3 |
| **Inference** | HuggingFace Inference API (Novita provider) |
| **Vector Database** | Pinecone Serverless (AWS us-east-1) |
| **Embeddings** | Sentence Transformers (all-mpnet-base-v2, 768-dim) |
| **ML/Data** | Python, Pandas, NumPy |
| **Data Generation** | Faker |
| **External APIs** | NewsAPI |

---

## Project Structure

```
aidhp-neural-nexus/
├── code/src/
│   ├── chatbot/                    # LLM orchestration & recommendations
│   │   ├── collaborativeFilteringLLM.py   # User similarity → product recommendations
│   │   ├── question_answering_chatbot.py  # RAG-based Q&A pipeline
│   │   ├── periodicDataSummarization.py   # Batch behavioral analysis
│   │   ├── deepseek_chatbot.py            # DeepSeek model interface
│   │   ├── mistral_chatbot.py             # Mistral model interface
│   │   └── recommendNews.py               # Topic extraction + news fetching
│   │
│   ├── pushingData2VectorDB/       # Vector database ingestion
│   │   ├── customerInfoToVectorDB.py      # Customer embedding pipeline
│   │   └── ProductsInfoToVectorDB.py      # Product embedding pipeline
│   │
│   ├── dataManipulations/          # ETL & data transformation
│   │   ├── changingStrucutreOfCustomerData.py
│   │   ├── combiningCSVs.py
│   │   └── dataTransformationForChatBotHistory.py
│   │
│   ├── syntheticDataGeneration/    # Test data generation
│   │   ├── dataGeneration.py              # User profile synthesis
│   │   ├── addingUsedProductsSection.py   # Product usage simulation
│   │   └── productInfoGeneration.py       # Product catalog creation
│   │
│   └── service/                    # REST API (Flask)
│       ├── app.py
│       ├── config.py
│       └── models.py
```

---

## Data Pipeline

### Customer Embedding Pipeline
```python
# 22 attributes encoded per customer:
CustomerID, Gender, AccountBalance, TransactionDateTime,
User_Profile, Age, Marital_Status, Income_Level,
Education_Level, Occupation, Residential_Status, Dependents,
Debt_to_Income, Credit_Bureau_Score, Credit_History,
Recent_Personal_Loan_Inquiry_6M, Recent_Credit_Card_Inquiry_6M,
Recent_Mortgage_Inquiry_6M, Recent_Personal_Loan_Inquiry_1Y,
Recent_Credit_Card_Inquiry_1Y, Recent_Mortgage_Inquiry_1Y,
servicesUsed
```

### Product Catalog
- **30 financial products** across 3 categories:
  - Bank Services (10): Premium accounts, FDs, lockers, forex accounts
  - Investment Services (10): Mutual funds, REITs, ULIPs, retirement plans
  - Other Services (10): Credit monitoring, fraud protection, tax advisory

---

## Getting Started

### Prerequisites
```bash
Python 3.9+
Pinecone API Key
HuggingFace API Key
NewsAPI Key (optional, for news recommendations)
```

### Installation
```bash
# Clone the repository
git clone https://github.com/yourusername/aidhp-neural-nexus.git
cd aidhp-neural-nexus

# Install dependencies
pip install -r requirements.txt

# Set up API keys (create files in /apiKey directory)
echo "your-pinecone-key" > apiKey/pineconeAPI.txt
echo "your-huggingface-key" > apiKey/huggingFace.txt
echo "your-newsapi-key" > apiKey/newsAPI.txt
```

### Index Setup (One-time)
```bash
# Generate synthetic data
python code/src/syntheticDataGeneration/dataGeneration.py
python code/src/syntheticDataGeneration/productInfoGeneration.py

# Push embeddings to Pinecone
python code/src/pushingData2VectorDB/customerInfoToVectorDB.py
python code/src/pushingData2VectorDB/ProductsInfoToVectorDB.py
```

### Usage
```python
# Collaborative Filtering Recommendations
from collaborativeFilteringLLM import collaborativeFiltering
collaborativeFiltering("C1015616")  # Returns top-3 products for similar users

# Q&A with Product Recommendations
from question_answering_chatbot import askQuestion
askQuestion("I'm a student looking to save for retirement. What are my options?")

# Transaction-Based Recommendations
from periodicDataSummarization import getRecommendations
getRecommendations("C5533885")  # Based on spending behavior
```

---

## How It Works

### 1. Collaborative Filtering Flow
```
User ID → Fetch embedding from Pinecone → k-NN search for similar users
→ Retrieve similar user profiles → Query product index
→ LLM refines & explains top-3 recommendations
```

### 2. Q&A + Recommendation Flow
```
User Question → DeepSeek generates answer → Mistral summarizes interaction
→ Summary embedded → Semantic search on product index
→ LLM selects & justifies relevant products
```

### 3. Behavioral Recommendation Flow
```
Transaction History → LLM summarizes spending patterns
→ Summary embedded → Product similarity search
→ LLM generates personalized recommendations with reasoning
```

---

## Use Cases

| Use Case | Module | Description |
|----------|--------|-------------|
| New user recommendations | `collaborativeFilteringLLM.py` | Find similar users, recommend their popular products |
| Financial Q&A | `question_answering_chatbot.py` | Answer queries + suggest relevant products |
| Post-transaction upsell | `periodicDataSummarization.py` | Analyze spending → recommend complementary products |
| Personalized news | `recommendNews.py` | Extract interests → fetch relevant financial news |

---

## 👥 Team Neural Nexus

Built during **Wells Fargo I&P Hackathon 2025**

---
