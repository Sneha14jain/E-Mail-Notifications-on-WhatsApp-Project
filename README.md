# E-Mail-Notifications-on-WhatsApp-Project
Developed an automation script that monitors emails and send instant notifications to Whatsapp using Python ,IMAP , and Twilio API.

 Overview :
This Python project automates email monitoring and sends real-time WhatsApp notifications for new emails using IMAP (for email retrieval) and Twilio API (for WhatsApp messaging).

How It Works:

1. The script connects to an email inbox using IMAP.

2. It scans for unread emails and extracts sender details and subject.

3. The extracted details are sent as a WhatsApp message using Twilio API.

4. The process runs automatically at regular intervals using Task Scheduler (Windows) or Cron Jobs (Linux/Mac).


Technologies Used :

Python – Core programming language

IMAP Protocol – For accessing emails

Twilio API – For sending WhatsApp messages

Task Scheduler / Cron Jobs – For automation

Use Cases:

Instant email notifications for urgent messages
Helps businesses & professionals stay updated
Can be modified for custom email filtering
