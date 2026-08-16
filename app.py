import streamlit as st

# Page settings
st.set_page_config(
    page_title="Student Support Chatbot",
    page_icon="🎓",
    layout="centered"
)

# Sidebar
st.sidebar.title("🎓 Student Support")
st.sidebar.write("Choose a category:")

category = st.sidebar.selectbox(
    "Category",
    [
        "General",
        "Academics",
        "Examinations",
        "Attendance",
        "Library",
        "Fees & Administration"
    ]
)

st.sidebar.divider()
st.sidebar.info(
    "This chatbot provides quick answers to common student queries."
)

# Main page
st.title("🎓 Student Support Chatbot")

st.write(
    "Welcome! I am your Student Support Assistant. "
    "Ask me about academics, exams, attendance, library, fees and other student services."
)

st.divider()

# Question box
question = st.text_input(
    "💬 Type your question here:"
)

# Chatbot logic
if question:

    question = question.lower()

    if "hello" in question or "hi" in question or "hey" in question:
        answer = "Hello! 😊 How can I help you today?"

    elif "attendance" in question:
        answer = (
            "The minimum required attendance is generally 75%. "
            "Please check your college rules for exact requirements."
        )

    elif "exam" in question or "examination" in question:
        answer = (
            "For examination schedules, dates and notices, "
            "please check the official examination notice or contact your department."
        )

    elif "library" in question or "book" in question:
        answer = (
            "The library provides books and study resources for students. "
            "Please check your college notice for the current library timings."
        )

    elif "fee" in question or "fees" in question:
        answer = (
            "For fee-related information, please contact the college "
            "accounts or administration department."
        )

    elif "course" in question or "courses" in question:
        answer = (
            "The college offers various academic programs. "
            "Please check the official college website for the complete list of courses."
        )

    elif "faculty" in question or "teacher" in question:
        answer = (
            "For faculty-related information, please contact your department "
            "or check the official college directory."
        )

    elif "leave" in question:
        answer = (
            "For leave, students should follow their college's "
            "official leave application procedure."
        )

    elif "holiday" in question or "holidays" in question:
        answer = (
            "Please check the official academic calendar "
            "for the current holiday schedule."
        )

    elif "contact" in question:
        answer = (
            "For official assistance, please contact your college "
            "administration or student support department."
        )

    elif "result" in question or "results" in question:
        answer = (
            "For examination results, please check the official student portal "
            "or examination department."
        )

    elif "assignment" in question:
        answer = (
            "Please contact your respective subject faculty for "
            "assignment deadlines and submission instructions."
        )

    elif "scholarship" in question:
        answer = (
            "For scholarship information, check the official scholarship portal "
            "and contact your college administration for assistance."
        )

    elif "id card" in question or "identity card" in question:
        answer = (
            "For student ID card-related issues, please contact "
            "the college administration office."
        )

    elif "timetable" in question or "time table" in question:
        answer = (
            "Please check your department notice board or student portal "
            "for the latest class timetable."
        )

    else:
        answer = (
            "Sorry, I don't have information about that yet. 😕 "
            "Try asking about attendance, exams, library, fees, courses, "
            "faculty, leave, results or scholarships."
        )

    st.success("🤖 " + answer)

# Suggested questions
st.divider()

st.subheader("💡 Try asking")

col1, col2 = st.columns(2)

with col1:
    st.write("• What is the attendance requirement?")
    st.write("• When are the exams?")
    st.write("• Tell me about the library.")
    st.write("• How can I apply for leave?")

with col2:
    st.write("• How can I check my results?")
    st.write("• Tell me about scholarships.")
    st.write("• How can I contact faculty?")
    st.write("• Where can I get the timetable?")

# About project
st.divider()

with st.expander("ℹ️ About This Project"):
    st.write(
        "The Student Support Chatbot is a Python-based application "
        "designed to provide quick responses to common student queries."
    )

    st.write(
        "The project uses Python and Streamlit to create an "
        "interactive web-based interface."
    )

    st.write(
        "The current version uses keyword-based query matching "
        "to identify questions and provide appropriate responses."
    )