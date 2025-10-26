import streamlit as st

# Set up the app title
st.set_page_config(page_title="Inch to Millimeter Converter", page_icon="📏", layout="centered")

st.title("📏 Inch to Millimeter Converter")

# Input field for user to enter the inch value
inch_value = st.number_input("Enter value in inches:", min_value=0.0, format="%.4f")

# Conversion factor
conversion_factor = 25.4

# Convert when button is clicked
if st.button("Convert"):
    mm_value = inch_value * conversion_factor
    st.success(f"{inch_value} inch = {mm_value:.4f} mm")

# Add some footer info
st.markdown("---")
st.caption("Developed by Raghvendra Dhakar | Simple Unit Converter using Streamlit")
