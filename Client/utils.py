import google.generativeai as genai

def generate_content(question, prompt=""):
    GOOGLE_GEMINI_API_KEY = "AIzaSyC81p8yKmzgto9wEt2e0M25HfA46wSYRdY"
    genai.configure(api_key=GOOGLE_GEMINI_API_KEY)
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content([question, prompt])
    answer = response.text
    return answer

