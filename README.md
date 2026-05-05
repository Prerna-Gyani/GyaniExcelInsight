# GyaniExcelInsight

This project is done by Prerna Gyanchandani 

Link: https://gyaniexcelinsight.streamlit.app/


---

# 🤖 AI Excel Chatbot using Gemini & Streamlit

---

## 📌 Overview
The AI Excel Chatbot is an intelligent data analysis web application built using Streamlit and Google Gemini API.  
It enables users to upload one or multiple Excel files and interact with the data using natural language queries.

The system performs automatic data analysis, generates visualizations, and provides AI-driven insights, making it suitable for academic, research, and business use cases.

---

## 🎯 Objectives
- Simplify data analysis for non-technical users  
- Enable AI-based interaction with structured datasets  
- Support multi-file dataset handling  
- Provide automatic insights, trends, and explanations  

---

## 🚀 Features

### 📂 Dataset Management
- Upload multiple Excel files  
- Switch between datasets dynamically  
- Supports `.xlsx` format  

### 📊 Automatic Data Analysis
- Dataset preview  
- Summary statistics (mean, std, min, max)  
- Missing value detection  

### 📉 Visualization
- Interactive scatter plots  
- Dynamic axis selection  
- Works with numerical columns  

### 🤖 AI Chatbot (Gemini Powered)
- Ask natural language questions  
- Context-aware answers  
- Generates insights and trends  

### 🔑 Secure API Input
- User provides Gemini API key  
- No hardcoded credentials  

### 🆕 Chat System
- New Chat option  
- Clears previous conversation  
- Retains datasets  

---

## 🛠️ Tech Stack

| Technology | Purpose |
|-----------|--------|
| Streamlit | Web interface |
| Pandas | Data processing |
| Matplotlib | Visualization |
| Seaborn | Advanced plotting |
| Google Gemini API | AI chatbot |
| OpenPyXL | Excel handling |

---

## 📦 Installation

### Step 1: Clone Repository
```bash
git clone https://github.com/your-username/ai-excel-chatbot.git
cd ai-excel-chatbot
````

### Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run Application

```bash
streamlit run app.py
```

---

## 🔑 How to Use

1. Open the application
2. Enter your Gemini API key in the sidebar
3. Upload Excel file(s)
4. Select dataset
5. View:

   * Data preview
   * Analysis
   * Graphs
6. Ask questions in chatbot

---

## 📁 Project Structure

```
ai-excel-chatbot/
│
├── app.py
├── requirements.txt
├── packages.txt
└── README.md
```

---

## 📄 requirements.txt

```
streamlit
pandas
matplotlib
seaborn
google-generativeai
openpyxl
```

---

## 📄 packages.txt (For Streamlit Cloud Fix)

```
libgl1
```

---

## ⚠️ Common Error Fix

### Error:

```
ImportError: libGL.so.1 not found
```

### Solution:

Add `packages.txt` with:

```
libgl1
```

---

## 🔮 Future Enhancements

* AI-generated dashboards
* Multi-file reasoning (RAG)
* PDF/Excel report export
* Natural language to Pandas queries
* Firebase integration
* Advanced analytics (clustering, prediction)

---

## 📚 Use Cases

* Academic projects
* Data analytics assignments
* Business insights
* Research analysis
* Exploratory Data Analysis (EDA)

---

## 🤝 Contribution

* Fork the repository
* Create feature branch
* Submit pull request

---

## 📜 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

Developed as part of an AI/ML project.

Thankyou for visiting

Check out more projects on: https://share.streamlit.io/user/prerna-gyani
