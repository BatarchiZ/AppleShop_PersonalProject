from email.message import EmailMessage
import ssl
import smtplib


def botSendsEmail(order, username):
    emailSender = ""
    emailReceiver = ""
    emailPassword = ""
    # emailPassword = "some password goes here"

    subject = "New order on Telegram Bot"
    body = f"""
    Hello, World
    user: {username}

    has ordered : {order}

    """

    em = EmailMessage()
    em['From'] = emailSender
    em['To'] = emailReceiver
    em['Subject'] = subject
    em.set_content(body)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(emailSender, emailPassword)
        smtp.sendmail(emailSender, emailReceiver, em.as_string())


def general_handler(chat, order):
    username = chat.username
    chat.send(
        f"Order placed, {username}. Our employee will contact you shortly for further information about your {order} order.")
    botSendsEmail(order, username)