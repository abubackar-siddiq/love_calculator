import random
import streamlit as st

# Set the title of the app
st.title("Love Percentage Calculator ❤️")

# Create input fields for the user's name and their lover's name
user_name = st.text_input("Enter Your Name:")
lover_name = st.text_input("Enter Your Lover's Name:")

# Button to trigger love calculation
if st.button("Calculate Love"):
    if user_name == "" or lover_name == "":
        st.error("Please enter both names!")  # Display error message
    else:
        # Generate random love percentage
        love_percentage = random.randint(1, 100)
        
        # Determine the love level based on the percentage
        if love_percentage <= 10:
            love_result = "Low"
        elif 10 < love_percentage <= 40:
            love_result = "Good"
        elif 40 < love_percentage <= 70:
            love_result = "Crazy"
        else:
            love_result = "On Peak"
        
        # Display the result
        st.subheader(f"{user_name} ❤ {lover_name}")
        st.write(f"Your Love: {love_percentage}%")
        st.success(f"Your love is {love_result}!")
