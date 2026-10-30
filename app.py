import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Ingredient Safety Checker", page_icon="🧴", layout="centered")

st.title("🧴 Ingredient Safety Checker")
st.write("Enter any cosmetic ingredient and check if it's safe, moderate, or risky.")

# --- LOAD DATA ---
try:
    # file path safe way
    file_path = os.path.join(os.path.dirname(__file__), 'ingredients.xls')
    df = pd.read_excel(file_path)
    # clean column names
    df.columns = df.columns.str.strip().str.lower()
except Exception as e:
    st.error(f"Error loading file: {e}")
    st.stop()

# --- USER INPUT ---
user_input = st.text_input("Enter ingredient name (e.g. Paraben, Hyaluronic Acid)")

if user_input:
    found = df[df['ingredient'].str.lower() == user_input.lower().strip()]
    
    if not found.empty:
        row = found.iloc[0]
        safety = str(row['safety']).lower()
        info = row.get('info', 'No info available')
        ingredient_name = row['ingredient']

        if safety == 'safe':
            st.success(f"**{ingredient_name}** is ✅ SAFE