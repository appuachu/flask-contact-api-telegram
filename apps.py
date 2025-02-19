from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
from datetime import datetime

app = Flask(__name__)
CORS(app)


TELEGRAM_BOT_TOKEN = ''
TELEGRAM_CHAT_ID = ''

def send_to_telegram(name, email, phone):
    message = (
        f"📩 <b>New Contact Form Submission</b>\n\n"
        f"🕒 <b>Timestamp:</b> {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
        f"👤 <b>Name:</b> {name}\n"
        f"📧 <b>Email:</b> {email}\n"
        f"📞 <b>Phone:</b> {phone}"
    )
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        'chat_id': TELEGRAM_CHAT_ID,
        'text': message,
        'parse_mode': 'HTML'
    }
    response = requests.post(url, data=payload)
    return response.json()

@app.route('/contact', methods=['GET', 'POST'])

def contact_form():
    try:
        data = request.json  
        name = data.get('name')
        email = data.get('email')
        phone = data.get('phone')

        if not name or not email or not phone:
            return jsonify({"error": "All fields are required"}), 400

        send_to_telegram(name, email, phone)

        return jsonify({"success": True, "message": "Form submitted successfully!"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
