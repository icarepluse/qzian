import fitz  # PyMuPDF
from huggingface_hub import InferenceClient
from django.core.files.storage import FileSystemStorage
from django.utils.crypto import get_random_string
from .models import qustion,answer,optionAnser,tests
import streamlit as st
import json
import pandas as pd
import requests
import json
import os
from dotenv import load_dotenv
load_dotenv('.env')
API_KEY = os.getenv('APIKEY')


# Google Gemini API URL
API_URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent?key={API_KEY}"


def extract_text_from_pdf(pdf_file):
    pdf_document = fitz.open(stream=pdf_file.read(), filetype="pdf")
    text = ""
    for page_num in range(pdf_document.page_count):
        page = pdf_document.load_page(page_num)
        text += page.get_text()
    return text

def genqustion(request):
    
    print(API_KEY)
    upload  =  request.FILES.get('filespdf')
    uploaded_file = upload
    
    num_questions =request.POST.get('nofq')
    # Extract text from the PDF

    uids=request.session.get('unicids')
    extracted_text = extract_text_from_pdf(uploaded_file)
    generated_mcqs = generate_mcqa(extracted_text, num_questions,uids)
      
    return generated_mcqs


def generate_mcqa(topic,num_questions,uids):
  
        headers = {
        "Content-Type": "application/json"
        }
        prompt = f"""Generate {num_questions} multiple-choice questions and answers from the following text. Ensure questions are contextually relevant and do not explicitly refer to the text:

{topic}

Please format the output as follows:
Question: [Your question here]
a) [Option A]
b) [Option B]
c) [Option C]
d) [Option D]
Answer: [Correct answer]

Provide each question and its answers on a new line, followed by a separator for each question.
"""
        data = {
        "contents": [{"parts": [{"text": prompt}]}]
        }
    
        response = requests.post(API_URL, headers=headers, json=data)

        data = json.loads(response.text)
       
# Access the value of the "parts" key
        #parts_value = data.get("candidates", {}).get("content", {}).get("parts")
        
        parts_value = data.get("candidates", {})
        
        for item in parts_value:
                parts = item.get('content', {}).get('parts', [])
                for part in parts:
                        text_value = part.get('text')
                        
                        
                        
                        
        mcqs = text_value.strip().split("\n\n")
        for mcq in mcqs:
                carttmps=get_random_string(length=15)
                lines = mcq.split("\n")
                if len(lines) >= 5:
                    # Extract and display question, options, and answer
                    question = lines[0].replace("Question:", "").strip()
                    options = [line.strip() for line in lines[1:5]]
                    answers = lines[5].replace("Answer:", "").strip()

                    qtions=qustion()
                    qtions.qstion=question
                    qtions.key=carttmps
                    qtions.unicid=uids
                    qtions.save()
                  
                  
                  
                    
                    for option in options:
                        optin=optionAnser()
                        optin.option=option
                        optin.key=carttmps
                        optin.unicid=uids
                        optin.save()
                      
                    anr=answer()
                    anr.answers=answers
                    anr.key= carttmps
                    anr.unicid=uids
                    anr.save()
                  #  st.write(f"Answer: {answer}")
                  #  st.write("---")  # Add a separator between questions
                #print(response.text)
   
        return 1