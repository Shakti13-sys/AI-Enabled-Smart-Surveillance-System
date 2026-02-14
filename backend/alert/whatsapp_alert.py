from twilio.rest import Client
import time
import os
from dotenv import load_dotenv

# 🔐 Twilio credentials 
ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
AUTH_TOKEN  = os.getenv("TWILIO_AUTH_TOKEN")

FROM_WHATSAPP = os.getenv("TWILIO_FROM")   # Twilio sandbox
TO_WHATSAPP   = os.getenv("TWILIO_TO") # authority number

client = Client(ACCOUNT_SID, AUTH_TOKEN)

def send_whatsapp_alert(reason, location):
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")

    message = f"""
🚨 *AI SURVEILLANCE ALERT*

📍 Location: {location}
⏰ Time: {timestamp}
⚠️ Threat: {reason}

🚔 Immediate action required
"""

    client.messages.create(
        body=message,
        from_=FROM_WHATSAPP,
        to=TO_WHATSAPP
    )

    print("📲 WhatsApp alert SENT")
