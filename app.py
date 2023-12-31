import google.generativeai as genai
import os

genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

model = genai.GenerativeModel('gemini-pro')

# for m in genai.list_models():
#     if 'generateContent' in m.supported_generation_methods:
#         print(m.name)

response = model.generate_content("Hi, call me Mr.HooQii")

print(response.text)