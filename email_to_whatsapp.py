import imaplib
import email
from email.header import decode_header
from twilio.rest import Client

# Email Credentials
EMAIL_USER = "your_email@gmail.com"
EMAIL_PASS = "your_app_password"
IMAP_SERVER = "imap.gmail.com"  # For Gmail
IMAP_PORT = 993

# Twilio Credentials
TWILIO_SID = "your_twilio_sid"
TWILIO_AUTH_TOKEN = "your_twilio_auth_token"
TWILIO_WHATSAPP_NUMBER = "whatsapp:+14155238886"  # Twilio Sandbox Number
YOUR_WHATSAPP_NUMBER = "whatsapp:+your_number"

def check_email():
    try:
        # Connect to email server
        mail = imaplib.IMAP4_SSL(IMAP_SERVER, IMAP_PORT)
        mail.login(EMAIL_USER, EMAIL_PASS)
        mail.select("inbox")

  # Search for unread emails
        status, messages = mail.search(None, 'UNSEEN')
        mail_ids = messages[0].split()

        for num in mail_ids:
            # Fetch the email
            status, msg_data = mail.fetch(num, '(RFC822)')
            for response_part in msg_data:
                if isinstance(response_part, tuple):
                    msg = email.message_from_bytes(response_part[1])
                    subject, encoding = decode_header(msg["Subject"])[0]

                    if isinstance(subject, bytes):
                        subject = subject.decode(encoding if encoding else "utf-8")

                    from_email = msg.get("From")

                    # Send WhatsApp notification
                    send_whatsapp_message(from_email, subject)

        mail.logout()

    except Exception as e:
        print(f"Error: {e}")

def send_whatsapp_message(from_email, subject):
    try:
        client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
        message = f"New Email Alert!\nFrom: {from_email}\nSubject: {subject}"
        
        client.messages.create(
  body=message,
            from_=TWILIO_WHATSAPP_NUMBER,
            to=YOUR_WHATSAPP_NUMBER
        )

        print("WhatsApp notification sent!")

    except Exception as e:
        print(f"Error sending WhatsApp message: {e}")

if _name_ == "_main_":
    check_email()
