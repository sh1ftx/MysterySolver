# Essa parte é apenas para testar implementações específicas 

import google.generativeai as genai

# Configurar API Key
genai.configure(api_key="")

# Criar um modelo
model = genai.GenerativeModel("gemini-pro")

# Gerar conteúdo
response = model.generate_content("Como a IA funciona?")

# Exibir resposta
print(response.text)
