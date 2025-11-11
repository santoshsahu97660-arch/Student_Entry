import streamlit as st
import pandas as pd

st.set_page_config(page_title="Student Entry Form", page_icon="🎓", layout="centered")

st.title("🎓 Student Entry Portal")
st.subheader("Fill your details below 👇")

# Create a session state to store entries
if "students" not in st.session_state:
    st.session_state["students"] = []

# Form layout
with st.form("student_form", clear_on_submit=True):
    name = st.text_input("🧑 Name:")
    number = st.text_input("📞 Mobile Number:")
    course = st.selectbox("📚 Select Course:", ["Python", "Data Science", "Java", "Web Development", "AI & ML"])

    submit = st.form_submit_button("✅ Submit")

    if submit:
        if name and number:
            st.session_state["students"].append({"Name": name, "Number": number, "Course": course})
            st.success(f"✅ {name}'s data has been added successfully!")
        else:
            st.error("⚠️ Please fill all fields before submitting!")

# Display all entered data
st.write("---")
st.subheader("📋 Student Entries")

if len(st.session_state["students"]) > 0:
    df = pd.DataFrame(st.session_state["students"])
    st.table(df)
else:
    st.info("No entries yet. Fill the form above to add your first student! 📄")

# Footer
st.write("---")
st.caption("Developed by Santosh 💻 | Streamlit Demo App 2025")
