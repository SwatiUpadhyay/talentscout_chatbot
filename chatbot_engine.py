# chatbot_engine.py

import os
import requests
from dotenv import load_dotenv

# Load the Hugging Face token from .env
load_dotenv()
API_URL = "https://api-inference.huggingface.co/models/HuggingFaceH4/zephyr-7b-beta"
HF_TOKEN = os.getenv("HUGGINGFACE_API_KEY")

headers = {
    "Authorization": f"Bearer {HF_TOKEN}"
}

def generate_questions(tech_stack):
    """
    Calls the Hugging Face inference API to generate technical interview questions
    for the provided tech stack.
    """
    prompt = (
        f"The candidate has listed the following technologies: {tech_stack}.\n\n"
        f"For EACH of these technologies, generate EXACTLY 3 technical interview questions."
        f" DO NOT include any other technologies or extra instructions.\n\n"
        f"Label each section clearly with the technology name followed by a colon.\n"
        f"Only return the questions."
    )

    payload = {
        "inputs": prompt,
        "parameters": {
            "max_new_tokens": 512,
            "temperature": 0.7,
            "return_full_text": False
        }
    }

    try:
        response = requests.post(API_URL, headers=headers, json=payload)
        response.raise_for_status()
        result = response.json()
        generated_text = result[0]["generated_text"]
        return generated_text.strip()
    except Exception as e:
        return f"❌ Error generating questions: {e}"


def filter_to_only_selected_techs(raw_text, tech_stack):
    """
    Filters the generated output to include only the user-specified techs,
    and keeps only the first 3 questions per tech.
    """
    allowed = [tech.strip().lower() for tech in tech_stack.split(",")]
    lines = raw_text.splitlines()
    final_output = []

    current_tech = ""
    keep = False
    count = 0

    for line in lines:
        line_strip = line.strip()

        # Start of a new tech section
        if line_strip.endswith(":"):
            tech_name = line_strip[:-1].strip().lower()
            keep = tech_name in allowed
            count = 0  # Reset question count per tech

            if keep:
                current_tech = line_strip
                final_output.append(f"\n**🧠 {current_tech}**")
        
        elif keep and line_strip:
            # Basic heuristic: count lines starting with lowercase letters or a question
            if count < 3:
                final_output.append(line_strip)
                count += 1
            else:
                continue  # Ignore extra questions
        
        elif not line_strip:
            continue
        else:
            # Remove any accidental tips or meta instructions
            if any(bad in line_strip.lower() for bad in ["each question", "include a mix", "avoid", "instead"]):
                continue

    return "\n".join(final_output).strip()
