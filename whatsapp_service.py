import requests
import os


def send_whatsapp(phone, message):
url = f"https://graph.facebook.com/v18.0/{os.environ['PHONE_NUMBER_ID']}/messages"
headers = {
"Authorization": f"Bearer {os.environ['WHATSAPP_TOKEN']}",
"Content-Type": "application/json"
}
payload = {
"messaging_product": "whatsapp",
"to": phone,
"type": "text",
"text": {"body": message}
}
requests.post(url, headers=headers, json=payload)
