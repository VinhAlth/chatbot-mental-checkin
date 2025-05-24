# 🧠 AI Mental Health Support Chatbot

A conversational AI system designed to assist with **preliminary psychological assessments**, mental health screening, and personalized well-being support.  
Built using **Vistral 7B**, this chatbot delivers a safe, empathetic, and structured dialogue experience.

---

## 🎬 Demo

![Chatbot Demo](video.gif)

---

## 🧾 Project Overview

This chatbot guides users through the **PHQ-9 questionnaire**, a standard clinical tool for assessing depression severity. It simulates an empathetic conversation that ensures **emotional safety**, **privacy**, and **clarity** for the user. The chatbot:

- ✅ Asks 9 PHQ-9 questions conversationally
- ✅ Responds supportively to each answer
- ✅ Calculates score internally (not visible to user)
- ✅ Summarizes findings with tailored suggestions
- ✅ Encourages professional support when necessary

---

## 🌟 Key Features

- 💬 Empathe powered by Vistral 7B and modern
- 🧠 Validated Psychological Framework (PHQ-9 logic)
- 🔐 Private Scoring with no exposure of sensitive data
- 🪷 Wel (e.g., mindfulness, journaling, jogging)
- 🚨 Professional Referral for high-risk cases
- 🖥️ User-friendly frontend for easy self-check-in

---

## 💡 Use Cases

- 🧑‍🎓 **Students** in need of periodic mental wellness check-ins  
- 🏢 **Employees** accessing corporate mental health support systems  
- 🧘 **Individuals** seeking self-guided mental health reflection or early detection  
- 🏫 **Schools & Universities** offering proactive support to learners  

---

## ⚙️ Tech Stack

| Component         | Technology                 |
|------------------|----------------------------|
| Language Model    | `Vistral 7B`               |
| Backend           | `Python`, `FastAPI`        |
| Frontend          | `Streamlit` / `React`      |
| LLM Orchestration | `LangChain`                |
| NLP Tools         | `spaCy`, `Transformers`    |
| Scoring Engine    | `PHQ-9` (custom logic)     |
| Deployment        | `Docker`, `Railway` / `GCP`|

---

## 🚀 Quick Start

```bash
git clone https://github.com/VinhAlth/chatbot-mental-checkin.git
cd chatbot-mental-checkin
pip install -r requirements.txt
uvicorn app.main:app --reload
````

Open your browser and visit: [http://localhost:8000](http://localhost:8000)

---

## 📁 Project Structure

```
chatbot-mental-checkin/
│
├── app/
│   ├── main.py              # FastAPI app
│   ├── dialogue_engine.py   # Conversation logic
│   ├── phq9.py              # PHQ-9 logic & scoring
│   ├── prompts/             # Prompt templates
│   ├── storage.py           # Logs (if enabled)
│
├── frontend/                # Streamlit UI (optional)
├── demo/                    # Demo assets (GIF, screenshots)
├── requirements.txt
└── README.md
```

---

## 🧪 Sample Conversation

> 👤 **User**: I don’t feel interested in anything these days.
> 🤖 **Chatbot**: I’m really sorry you’re feeling that way. It’s okay to feel overwhelmed. Could you tell me how often you've felt like this over the last 2 weeks?

> 👤 **User**: Almost every day.
> 🤖 **Chatbot**: Thank you for your honesty. That sounds difficult. I'm here to help you explore how you're feeling, one step at a time.

> *(… continues through 9 questions)*

> 🤖 **Chatbot (Final)**: Based on your responses, it might help to try daily mindfulness or reach out to a trusted person. If this feeling persists, I recommend talking to a mental health professional. You’re not alone, and support is available 💙

---

## ✅ Ethics & Safety

* 📋 Based on **validated psychological instruments** (PHQ-9)
* 🧠 Includes **well-being-first design** for interaction safety
* 🔐 All data is anonymized, not stored by default
* ⚠️ Clearly states **non-diagnostic disclaimer**

---

## 📚 References

* Kroenke, K., Spitzer, R. *The PHQ-9: Validity of a Brief Depression Severity Measure*
* OpenAI Vistral / LLM framework
* LangChain & Hugging Face Transformers

---

## 👨‍💻 Author & Supervision

* 👨‍💻 **Nguyễn Quốc Vinh** – LLM Developer & Dialogue Designer
* 👨‍🏫 Supervised by Dr. Huỳnh Ngọc Tính – SIU AI Lab
* 🧪 Internship Project – June–September 2024

---

## 📬 Contact

* ✉️ Email: [quoctinvinh@gmail.com](mailto:quoctinvinh@gmail.com)
* 🔗 LinkedIn: [linkedin.com/in/quoctinvinh](https://linkedin.com/in/quoctinvinh)

---

> ⚠️ **Disclaimer**: This chatbot is a research prototype and does not offer professional medical advice. If you're experiencing a mental health crisis, please contact a licensed therapist or local emergency services.
