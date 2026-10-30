import streamlit as st
import pandas as pd

st.set_page_config(page_title="Ingredient Analyzer", page_icon="🧴")
st.title("🧴 Ingredient Safety Checker")
st.write("Enter any cosmetic ingredient and check its safety instantly!")

pd.read_excel('ingredients.xls')

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
# --- FOOTER - Created By Sanika Shelar ---
st.markdown("---")
st.markdown("""
<div style='text-align:center; padding: 15px; background-color: #f9f9f9; border-radius: 10px; margin-top: 20px;'>
    <p style='color:#333; font-size:16px; margin-bottom: 5px;'>Made with ❤️ by <b>Sanika Shelar</b></p>
    <a href='https://github.com/shelarsanika1210-spec' target='_blank' style='text-decoration:none; margin-right:15px;'>🌟 GitHub</a>
    <a href='https://www.linkedin.com/in/sanika-shelar' target='_blank' style='text-decoration:none;'>💼 LinkedIn</a>
</div>
""", unsafe_allow_html=True)
# Hide Streamlit default footer
hide_style = """
<style>
footer {visibility: hidden;}
#MainMenu {visibility: hidden;}
header {visibility: hidden;}
</style>
"""
st.markdown(hide_style, unsafe_allow_html=True)