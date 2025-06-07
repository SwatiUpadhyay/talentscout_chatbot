# TalentScout – AI Hiring Assistant Chatbot

**TalentScout** is an AI-powered chatbot built with Streamlit and Hugging Face's Zephyr-7B model to assist in the initial screening of candidates for tech roles.  

It collects candidate information and generates relevant technical questions based on their declared tech stack.

---

## 🔧 Installation Instructions

1. **Clone the repository**

git clone https://github.com/your-username/talentscout_chatbot.git

cd talentscout_chatbot


2. **Install dependencies**

    pip install -r requirements.txt

3. **Add your Hugging Face API key**

    HUGGINGFACE_API_KEY=your_huggingface_api_key

4. **Run the Streamlit app**

    streamlit run app.py
   

**Usage Guide**

Once the app is running, the chatbot will :

- Greet the candidate and explain its purpose

- Collect personal information: name, contact, experience, role, location, tech stack

- Let the user input technologies they’re familiar with (e.g., Python, Django, React)

- Generate 3–5 technical interview questions per technology

- Prevent empty submissions and handle unknown inputs gracefully

- Support an “Exit” button to end the interaction respectfully

- Log candidate data to data/logs.csv


**Technical Details**

- Language: Python

- UI: Streamlit

- LLM: Hugging Face Inference API (Zephyr-7B)

- Prompt Handling: Custom structured prompt + output filtering

- Environment Management: python-dotenv

- Data Logging: Saved to CSV file on form submit



**Prompt Strategy**

The chatbot uses structured prompts to achieve two main goals:

📥 Information Gathering
- Inputs are collected via a conversational form, validated, and stored in memory using Streamlit.

📤 Technical Question Generation
- Once a tech stack is provided, a prompt is sent to the LLM asking for 3–5 interview questions per technology. Prompts are designed to:

    - Avoid hallucination of unrelated tech

    - Return clearly labeled, structured sections

    - Follow a clean and readable format
    - 

**Challenges & Solutions**

- Stateless sessions : Used st.form and cleaned input post-submit
- Prompt hallucination : Filtered responses to match only provided tech stack
- Repetition / long output : Trimmed to 3 questions max per topic
- Exit behavior : Implemented a separate Exit button
- API security : API key stored in .env and excluded via .gitignore

🧪 Note
- All candidate data is simulated for demonstration purposes only.
- This app was built as part of a technical internship assessment.



👩‍💻 Developed By
Swati Upadhyay


🎥 Watch the demo video : https://www.loom.com/share/622ef72630ee435aa97f4ad808dc432c

Summary : In this video, I demonstrate my internship project, a smart hiring assistant called Talent Scout.
It collects candidate details and uses AI to generate custom interview questions.
I walk you through the process of filling out the form and show how the chatbot generates questions based on the input.
Please take a look at the generated questions and let me know your thoughts!
