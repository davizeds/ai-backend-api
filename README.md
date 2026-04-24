# 🤖 AI Backend API (FastAPI + OpenAI)

API simples construída com FastAPI que recebe um texto e retorna uma resposta gerada por IA (OpenAI).

## 🚀 Tecnologias

- Python
- FastAPI
- Uvicorn
- OpenAI API
- Python-dotenv

---

## 📁 Estrutura do Projeto


app/
├── main.py
├── routers/
│ └── ai.py
├── services/
│ └── ai_service.py
└── schemas/
└── ai_schema.py


---

## ⚙️ Configuração

### 1. Clonar o projeto

bash
git clone https://github.com/davizeds/ai-backend-api.git
cd ai-backend-api
2. Criar ambiente virtual
python -m venv .venv
.\.venv\Scripts\activate
3. Instalar dependências
pip install fastapi uvicorn openai python-dotenv
4. Criar arquivo .env

Na raiz do projeto:

.env

Conteúdo:

OPENAI_API_KEY=your_api_key_here
▶️ Rodando o projeto
python -m uvicorn app.main:app --reload

Acesse:

👉 http://127.0.0.1:8000/docs

📌 Endpoint
POST /ask
Request:
{
  "text": "o que é uma API?"
}
Response:
{
  "mensagem": "Uma API é..."
}
🧠 Como funciona
Recebe um texto via API
Envia para a OpenAI
Retorna a resposta gerada pela IA
⚠️ Observações
Necessário ter saldo na OpenAI para funcionar
Nunca exponha sua API KEY

👨‍💻 Autor

Davi Felipe Nasario
