import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import google.generativeai as genai

# ---------------- CONFIG ---------------- #
st.set_page_config(page_title="AI Excel Chatbot", layout="wide")

# ---------------- SESSION STATE ---------------- #
if "dataframes" not in st.session_state:
    st.session_state.dataframes = {}

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if "api_key" not in st.session_state:
    st.session_state.api_key = None

# ---------------- SIDEBAR ---------------- #
st.sidebar.title("⚙️ Settings")

# 🔑 API Key Input
api_key_input = st.sidebar.text_input(
    "Enter Gemini API Key",
    type="password",
    placeholder="Paste your API key here..."
)

if api_key_input:
    st.session_state.api_key = api_key_input
    genai.configure(api_key=st.session_state.api_key)

# Dataset section
st.sidebar.title("📂 Dataset Manager")

uploaded_files = st.sidebar.file_uploader(
    "Upload Excel Files",
    type=["xlsx"],
    accept_multiple_files=True
)

# New Chat button
if st.sidebar.button("🆕 New Chat"):
    st.session_state.chat_history = []
    st.success("New chat started!")

# Load datasets
if uploaded_files:
    for file in uploaded_files:
        df = pd.read_excel(file)
        st.session_state.dataframes[file.name] = df

dataset_names = list(st.session_state.dataframes.keys())

selected_dataset = st.sidebar.selectbox(
    "Select Dataset",
    dataset_names if dataset_names else ["No dataset"]
)

# ---------------- MAIN UI ---------------- #
st.title("🤖 AI Excel Chatbot (Gemini)")

# Check API Key
if not st.session_state.api_key:
    st.warning("⚠️ Please enter your Gemini API key in the sidebar.")
    st.stop()

# Load model AFTER API key is set
model = genai.GenerativeModel("gemini-1.5-pro")

if selected_dataset != "No dataset":
    df = st.session_state.dataframes[selected_dataset]

    # ---------------- DATA PREVIEW ---------------- #
    st.subheader("📊 Dataset Preview")
    st.dataframe(df.head())

    # ---------------- AUTO ANALYSIS ---------------- #
    st.subheader("📈 Automatic Analysis")

    col1, col2 = st.columns(2)

    with col1:
        st.write("### Summary Statistics")
        st.write(df.describe())

    with col2:
        st.write("### Missing Values")
        st.write(df.isnull().sum())

    # ---------------- VISUALIZATION ---------------- #
    st.subheader("📉 Visualization")

    numeric_cols = df.select_dtypes(include=["number"]).columns

    if len(numeric_cols) >= 2:
        x_col = st.selectbox("Select X-axis", numeric_cols)
        y_col = st.selectbox("Select Y-axis", numeric_cols)

        fig, ax = plt.subplots()
        sns.scatterplot(data=df, x=x_col, y=y_col, ax=ax)
        st.pyplot(fig)
    else:
        st.info("Not enough numeric columns for visualization.")

    # ---------------- CHATBOT ---------------- #
    st.subheader("💬 Ask Questions")

    user_input = st.text_input("Ask something about the dataset:")

    if user_input:
        with st.spinner("Thinking... 🤖"):
            try:
                context_data = df.head(50).to_string()

                prompt = f"""
                You are a professional data analyst.

                Dataset:
                {context_data}

                Question:
                {user_input}

                Provide:
                - Clear explanation
                - Insights
                - Trends/patterns
                """

                response = model.generate_content(prompt)

                st.session_state.chat_history.append(("User", user_input))
                st.session_state.chat_history.append(("AI", response.text))

            except Exception as e:
                st.error(f"Error: {e}")

    # ---------------- CHAT HISTORY ---------------- #
    for role, msg in st.session_state.chat_history:
        if role == "User":
            st.markdown(f"**🧑 You:** {msg}")
        else:
            st.markdown(f"**🤖 AI:** {msg}")

else:
    st.info("📂 Upload Excel file(s) to begin.")
