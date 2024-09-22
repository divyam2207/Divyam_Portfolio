from pathlib import Path
import time
import streamlit as st
from PIL import Image



# path settings
curr_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = curr_dir / "styles" / "main.css"
resume_file = curr_dir / "assets" / "DivyamDubey_Summer_Intern_Resume.pdf"
profile_pic = curr_dir / "assets" / "Divyam_Pic.jpg"
resume_in_drive = "https://drive.google.com/file/d/1HujyadrbMWqD7JGRGYdubtaioe_--Eh9/view?usp=drive_link"

# --- GENERAL SETTINGS ---
PAGE_TITLE = "Divyam Dubey | Digital Resume "
PAGE_ICON = ":computer:"
NAME = "Divyam Dubey"
DESCRIPTION = """
Masters in Computer Science Student @ [University of Florida](http://www.ufl.edu) :crocodile:
"""
EMAIL = "divyamdubey@ufl.edu"
SOCIAL_MEDIA = {
    ":phone: (352)-682-0794": "tel:+13526820794",
    # ":e-mail: divyamdubey@ufl.edu": EMAIL,
    " :link: LinkedIn": "https://linkedin.com/in/divyam2207",
    " :link: GitHub": "https://github.com/divyam2207",
    
    
}
PROJECTS = {
    ":card_file_box: pdfGPT - Streamlit-based web app for document processing": "https://github.com/divyam2207/pdfGPT",
    ":card_file_box: Spotify Party Collab - Collaborative music app with Spotify API": "https://github.com/divyam2207/CollaborativeMusicPlayingApplication",
    ":card_file_box: Cat Non-Cat Classifier - Machine Learning based Image Classifier": "https://github.com/divyam2207/Cat-vs-Non-Cat-Classifier",
    ":card_file_box: Bank Customer Churn Predictor - Deep learning based predictor using TensorFlow" : "https://github.com/divyam2207/Bank_Customer_Churn_Predictor" 
}

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# Create a button-like link using HTML and CSS
button_html = f"""
    <a href="{resume_in_drive}" target="_blank" style="
        display: inline-block; 
        padding: 10px 20px; 
        font-size: 16px; 
        color: #d33682; 
        background-color: transparent; 
        border: 2px solid #d33682; 
        border-radius: 25px; 
        text-decoration: none; 
        text-align: center; 
        transition: background-color 0.3s, color 0.3s;">
        Open Resume
    </a>
"""

# load css
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)

with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)

# hero section
col1, col2 = st.columns(2, gap="small")

with col1:
    st.image(profile_pic, caption=' "Any sufficiently advanced technology is indistinguishable from magic." ~ Arhtur C. Clarke')

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    # st.download_button(
    #     label="Download Resume :page_facing_up:",
    #     data=PDFbyte,
    #     file_name=resume_file.name,
    #     mime="application/octet-stream"
    # )
    st.markdown(button_html, unsafe_allow_html=True)

    st.write(":e-mail:", EMAIL)
    # st.write('---')
    # st.write(":phone:", "(352)-682-0794")

# Social links
# st.write("#")
cols = st.columns(len(SOCIAL_MEDIA))
for idx, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[idx].write(f"[{platform}]({link})")

#Technical Summary
st.write("---")
st.subheader("About me...")
st.write(""" 
I’m a Computer Science graduate student at the University of Florida, actively seeking Software Development/Engineering Internships for Summer 2025.
         
I have honed my skills in **Python, Machine Learning, and full-stack development**, creating real-time data platforms, automating processes, and building innovative web applications.

My expertise spans **Python, PHP, JavaScript, HTML, CSS, Laravel, SQL, Django, and React, complemented by certifications in Deep Learning, Machine Learning, AI, and cloud computing**. I’m also developing skills in **Data Engineering, Advanced Data Structures, and Distributed Operating Systems using Go lang and Pony**.

With a strong commitment to excellence and continuous learning, I’m passionate about solving complex problems and eager to contribute to dynamic teams that strive for innovation and impactful solutions.
""")

# Skills
st.write("---")
st.subheader("Technical Skills 	:desktop_computer:")
st.write("""
    - ► **Courses**: Advanced Data Structures, Distributed Operating System Principles, Data Engineering.
    - ► **Programming Languages**: Python, PHP, SQL, JavaScript, HTML, CSS, Java, Go (learning), Pony (learning).
    - ► **Frameworks and Tools**: Django, Laravel, React, Flask, StreamLit, Git, Linux, VS Code, Jupyter Notebook.
    - ► **Libraries**: Machine Learning, Pandas, NumPy, Matplotlib, Pytorch, Tensorflow.
    - ► **Certifications**: Microsoft Azure AZ-900, Generative AI with LLMS, Neural Networks and Deep Learning, Intro to Data Science.
""")

# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History      :male-office-worker:")
st.write("---")

# --- JOB 1
st.write(":computer:", "**Software Development Engineer | Gate 7 Infotech**")
st.write("June 2023 - June 2024")
st.write(
    """
- ► Implemented a robust real-time data-dashboard platform with PHP, Laravel, JavaScript, and SQL, resulting in a 60% increase in data retrieval speed and a 40% enhancement in user interaction quality.
- ► Integrated Authorize.Net and Twilio API to automate recurring billings and customer communication, resulting in a 40% increase in payment security and a 25% improvement in customer satisfaction ratings.
- ► Created a customer onboarding web application with a custom credit-scoring algorithm, reducing credit risk exposure by 20% and improving lease approval rates by 30%.
"""
)

# --- JOB 2

st.write('\n')
st.write(":computer:", "**Graduate Engineer Trainee | [Jio Platforms Limited](https://www.linkedin.com/company/jioplatforms/)**")
st.write("November 2022 - June 2023")
st.write(
    """
- ► Collaborated with Jio Events and Jio Cinema teams, rigorously tested APIs in Postman for a live streaming app, enhancing real-time communication and boosting user engagement by 25%.
- ► Built and implemented a real-time chat moderation system using JavaScript, reducing contentious comments by 40%.
"""
)

# --- JOB 3
st.write('\n')
st.write(":computer:", "**Software Engineer Intern | [Persistent Systems](https://www.persistent.com/)**")
st.write("February 2022 - September 2022")
st.write(
    """
- ► Mastered Python, JavaScript, HTML, CSS, GIT, and SQL during the internship, earning a pre-placement offer with a 90% score.
- ► Utilized technical problem-solving skills to optimize code and contribute to code review discussions.
"""
)

# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Projects 	:card_file_box:")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")
