import streamlit as st

# Sidebar navigation
st.sidebar.title("Sections")
choice = st.sidebar.radio(
    "", 
    options=["Start", "Mid", "End", "PDF"],
    format_func=lambda x: x  # could replace with icons/images via st.sidebar.image()
)

# Main area
st.title(f"{choice} Section")

# Depending on choice, render a different form
if choice == "Start":
    with st.form("start_form"):
        q1 = st.text_area("Question 1")
        q2 = st.text_area("Question 2")
        q3 = st.text_area("Question 3")
        submitted = st.form_submit_button("Save")
        if submitted:
            st.success("Start answers saved!")
            
elif choice == "Mid":
    with st.form("mid_form"):
        agree = st.checkbox("I agree to the terms")
        age = st.number_input("Your age", min_value=0, max_value=120)
        notes = st.text_area("Any notes?")
        if st.form_submit_button("Submit"):
            st.write("Thanks for Mid‑section input!")

elif choice == "End":
    with st.form("end_form"):
        rating = st.slider("Rate your experience", 1, 5)
        comments = st.text_area("Final comments")
        if st.form_submit_button("Finish"):
            st.balloons()
            st.success("All done!")

else:  # PDF
    st.info("Click below to download the PDF of your responses.")
    # Here you could generate a PDF on‑the‑fly and serve it:
    # pdf_bytes = make_pdf(...)
    # st.download_button("Download PDF", data=pdf_bytes, file_name="responses.pdf")