# using SendGrid's Python Library
# https://github.com/sendgrid/sendgrid-python
import os
import ssl
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail, Email

ssl._create_default_https_context = ssl._create_unverified_context

subjects = {
    "burst_pipe": "🚨 Urgent: Possible Burst Pipe Detected",
    "continuous_usage": "💧 Alert: Continuous Water Usage Detected",
    "time_of_use_anomaly": "⏰ Notice: Unusual Water Usage Pattern"
}

messages = {
    "burst_pipe": "Alert: You may have a burst pipe 🚨. Please check your water system immediately!",
    "continuous_usage": "Alert: Continuous water usage detected 💧. Please check your system and take any necessary action.",
    "time_of_use_anomaly": "Alert: Your water usage time is unusual ⏰. Please review your recent consumption."
}

def send_email(name, email, leak_type):
    message = Mail(
        from_email=Email("Utilyze <anisha.torres@utilyze.co>"),
        to_emails=f'{email}',
        subject=f'{subjects[leak_type]}',
        html_content = f"""
        <html>
        <body style="font-family: Arial, sans-serif; line-height: 1.6; color: #333;">
            <h2>Water Usage Alert</h2>
            <p>Hello {name},</p>
            <p>{messages[leak_type]}</p>
            <hr style="border: none; border-top: 1px solid #eee; margin: 20px 0;">
            <p style="font-size: 0.9em; color: #777;">
            This is an automated notification from Water Analytics.
            </p>
        </body>
        </html>
        """
    )
    try:
        print("Getting sg")
        print(os.environ.get('SENDGRID_API_KEY'))
        sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
        # sg.set_sendgrid_data_residency("eu")
        # uncomment the above line if you are sending mail using a regional EU subuser
        print("SG: ", sg)
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(e.message)

send_email("Anisha", "anishabhaskartorres@gmail.com", "burst_pipe")
