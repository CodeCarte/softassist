import google.generativeai as genai

API_KEY = 'AIzaSyBUwsezPUNBeSpEwU2RrB1y3rm2IVcQ0hw'
genai.configure(api_key = API_KEY)


model = genai.GenerativeModel('gemini-1.5-pro')

response = model.generate_content('Por que o céu é azul?')

print(response.text)

