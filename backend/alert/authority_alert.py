import os
import time
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()

ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")

WHATSAPP_FROM = os.getenv("WHATSAPP_FROM")
AUTHORITY_NUMBERS = os.getenv("AUTHORITY_NUMBERS", "").split(",")

# basic checks
if not ACCOUNT_SID or not AUTH_TOKEN:
    raise Exception("❌ Twilio credentials missing")

if not WHATSAPP_FROM:
    raise Exception("❌ WHATSAPP_FROM missing")

if not AUTHORITY_NUMBERS or AUTHORITY_NUMBERS == [""]:
    raise Exception("❌ AUTHORITY_NUMBERS missing")

client = Client(ACCOUNT_SID, AUTH_TOKEN)

_last_sent = 0
COOLDOWN = 10  # seconds

def send_authority_alert(reason, location, priority, lat, lng):
    global _last_sent
    now = time.time()

    if now - _last_sent < COOLDOWN:
        return

    map_link = f"https://www.google.com/maps?q={lat},{lng}"

    message_body = f"""
🚨 AI SURVEILLANCE ALERT

📍 Location: {location}
🗺️ Map: {map_link}

⚠️ Issue: {reason}
🔴 Priority: {priority}

🕒 Immediate attention required
"""

    for number in AUTHORITY_NUMBERS:
        number = number.strip()

        # ✅ WHATSAPP ONLY (NO SMS)
        client.messages.create(
            body=message_body,
            from_=f"whatsapp:{WHATSAPP_FROM}",
            to=f"whatsapp:{number}"
        )

    print("📨 Authority alerted via WhatsApp")
    _last_sent = now
