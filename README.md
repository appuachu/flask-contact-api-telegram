# HTML Contact Form API with Telegram Integration

##This project demonstrates how to integrate a simple Flask-based API with a basic HTML contact form. The API receives user input (name, email, phone) and sends the details to a Telegram chat using the Telegram Bot API.

# Features
```bash
✅ Flask API for handling contact form submissions
✅ Sends contact details to Telegram via a bot
✅ Simple HTML frontend for demonstration
✅ CORS enabled for easy integration
✅ Can be hosted on GitHub Pages (Frontend) and any Flask-supported server (Backend)
```
# Installation & Setup
```bash
## 1. Clone the Repository

git clone https://github.com/your-username/flask-contact-api-telegram.git
cd flask-contact-api-telegram

## 2. Install Dependencies

Make sure you have Python 3 installed, then run:
pip install flask flask-cors requests

## 3. Set Up Telegram Bot

Create a bot using @BotFather on Telegram
Get the BOT TOKEN from BotFather
Get your Chat ID (Use this guide to find your chat ID)
Add them to app.py:
TELEGRAM_BOT_TOKEN = 'your-bot-token'
TELEGRAM_CHAT_ID = 'your-chat-id'

## 4. Run the Flask API
python app.py
API will start on http://127.0.0.1:5000
```

# Deployment
```bash
* Hosting the Frontend
You can host index.html on GitHub Pages or any static web hosting service.

* Deploying the Backend
Heroku: Use Flask buildpack
Render: Deploy app.py with Python runtime
VPS / Cloud Server: Run with gunicorn or uwsgi
Local Deployment with Port Forwarding
```

