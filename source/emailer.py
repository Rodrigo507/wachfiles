from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
import smtplib
from decouple import config


def send_email(date_file):
    msg = MIMEMultipart()

    sender = config('EMAIL_ADDRESS')

    recipients = config('EMAIL_RECIPIENTS').replace(" ", "").split(",")

    msg['Subject'] = 'Revicion de archivo '+date_file
    msg['From'] = sender
    msg["To"] = "," .join(recipients)

    msg.preamble = 'Mensaje de multiples partes.\n'

    part = MIMEText("Mime")
    #part = MIMEText("En el archivo adjunto se encuentran los resultados")
    msg.attach(part)

    # Esta es la parte binaria (puede ser cualquier extensión):
    # part = MIMEApplication(open(fecha_pdf, "rb").read())
    # part.add_header('Content-Disposition', 'attachment', filename=fecha_pdf)
    # msg.attach(part)

    # Crear una instancia del servidor para envio de correo (hacerlo una sola vez)
    server = smtplib.SMTP("smtp.gmail.com:587")

    # Iniciar sesión en el servidor (si es necesario):
    server.ehlo()
    server.starttls()
    server.login(sender, config('PASSWORD'))
    # Envio
    server.sendmail(sender, recipients, msg.as_string())
    server.quit
