import streamlit as st
import pandas as pd

st.set_page_config(page_title="Ingredient Analyzer", page_icon="🧴")
st.title("🧴 Ingredient Safety Checker")
st.write("Enter any cosmetic ingredient and check its safety instantly!")

df = pd.read_excel('ingredients.xls', engine='openpyxl')

user_input = st.text_input("Enter ingredient to check:", placeholder="e.g. - paraben, vitamin c")

if user_input:
    found = df[df['ingredient'].str.lower() == user_input.lower().strip()]
    if not found.empty:
        row = found.iloc[0]
        if row['safety'].lower() == 'safe':
            st.success(f"**{row['ingredient']}** - Safe ✅")
        elif row['safety'].lower() == 'moderate':
            st.warning(f"**{row['ingredient']}** - Moderate ⚠️")
        else:
            st.error(f"**{row['ingredient']}** - Unsafe ❌")
        st.info(f"**Info:** {row['info']}")
    else:
        st.error("This ingredient is not in the database.")

st.write("---")
st.write("Available ingredients in database:")
st.dataframe(df)