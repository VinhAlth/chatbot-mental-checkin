# 🧠 AI Mental Health Support Chatbot

A conversational AI system designed to assist with **preliminary psychological assessments**, mental health screening, and personalized well-being support.  
Built using **Vistral 7B**, this chatbot delivers a safe, empathetic, and structured dialogue experience.

---

## 🎬 Demo

![Chatbot Demo](demo.gif)

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
- 🪷 Wellness Suggestions (e.g., mindfulness, journaling, jogging)
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

<div align="center">

| Component         | Technology                 |
|:----------------:|:--------------------------:|
| Language Model   | `Vistral-7B-Chat`               |
| Backend          | `Python`, `FastAPI`        |
| Frontend         | `Html`, `Css`              |

</div>


## 🚀 Quick Start

```bash
git clone https://github.com/VinhAlth/chatbot-mental-checkin.git
cd chatbot-mental-checkin
pip install -r requirements.txt
python main.py
````

Open your browser and visit: [http://localhost:8000](http://localhost:8000)

---

## 📁 Project Structure

```
your_project/
├── data copy/                     # Temporary folder for copied or backup data
├── logs/                          # Stores application logs (e.g., user sessions, errors)
├── result/run                     # Stores model output for each run (e.g., result_001.json)
├── src/                           # Main source code for the system (logic, AI, processing)
│   ├── __init__.py               
│   ├── executive.py               # Controls and coordinates chatbot conversation flow
│   ├── predict.py                 # Manage real-time conversation and save results to CSV
│   ├── prompts.py                 # Contains prompts for the LLM (e.g., VistralChatbot), PHQ-9 questions
│   ├── utils.py                   # Utility functions for model loading, conversation handling, etc.
│   └── end.py                     # Calculates and evaluates scores at the end of a test
├── static/                        # Static files (CSS, JS, images) for the web interface
├── templates/                     # HTML templates 
├── .gitignore                     
├── analyse.py                      # Analyzes user results after completing the questionnaire
├── main.py                        # Entry point to run the Flask web application
├── patient_infor.txt              # Temporary storage for patient information during a session
├── predict.py                     # Process data from CSV, predict, and save to CSV
├── readme.md                      # Project documentation (overview, setup, usage)
└── requirement.txt                # List of required Python packages (install via `pip install -r`)

```

---

## Sample Conversation

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


> ⚠️ **Disclaimer**: This chatbot is a research prototype and does not offer professional medical advice. If you're experiencing a mental health crisis, please contact a licensed therapist or local emergency services.
