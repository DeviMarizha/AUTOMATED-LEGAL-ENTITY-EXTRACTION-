# AUTOMATED-LEGAL-ENTITY-EXTRACTION-
**Description**
Automated Legal Entity Extraction using Legal-BERT and semantic similarity filtering. Extracts entities from complex legal documents with high accuracy (F1: 0.92). Includes a Streamlit web app for visualization, analysis, and real-time processing.

**Features** 
- Legal-BERT based Named Entity Recognition
- Semantic similarity filtering for better precision
- Entity extraction (Person, Organization, Location, Time)
- Highlighted text visualization
- Entity table with confidence scores
- Statistical analysis dashboard
- Streamlit web application

**Working**
  Legal Document → Preprocessing → Tokenization (BIO) → Legal-BERT Model → Semantic Filtering → Entity Extraction → Visualization

**Performance**
- Precision: 0.92
- Recall: 0.92
- F1-score: 0.92
- Accuracy: 0.99
  
**Tech Stack**
- Python
- Legal-BERT (Transformers)
- Streamlit
- Pandas, NumPy
- Scikit-learn
  
**Installation**
git clone https://github.com/your-username/legal-entity-extraction.git
cd legal-entity-extraction
pip install -r requirements.txt
streamlit run app.py

**Example**
Input:
"Google signed a contract on March 10, 2024."

Output:
Google → ORG
March 10, 2024 → TIM

**Unique Points**
- Combines Legal-BERT with semantic filtering
- Handles complex legal text and nested entities
- Includes real-time web application

**Limitations**
- Class imbalance in dataset
- Limited multilingual support

**Future Scope**
- Multilingual legal NLP
- Chatbot-based legal queries
