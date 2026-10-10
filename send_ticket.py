import os, smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

# === ВПИШИТЕ СВОИ ДАННЫЕ СЮДА ===
sender_email = "vasha_pochta@gmail.com"
sender_password = "ВАШ_НОВЫЙ_КОД"
receiver_email = "vasha_pochta@gmail.com"
file_path = "/sdcard/Download/quicktickets-order-23468479 (2).pdf"
# ================================

try:
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = "Билет на спектакль (Gmail)"
    msg.attach(MIMEText("Ваш билет во вложении.", 'plain'))

    filename = os.path.basename(file_path)
    with open(file_path, "rb") as attachment:
        part = MIMEBase("application", "pdf")
        part.set_payload(attachment.read())
    
    encoders.encode_base64(part)
    part.add_header("Content-Disposition", f"attachment; filename={filename}")
    msg.attach(part)

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(sender_email, sender_password)
    server.sendmail(sender_email, receiver_email, msg.as_string())
    server.quit()
    print("УРА! Письмо успешно улетело на Gmail!")

except FileNotFoundError:
    print(f"Ошибка: Файл '{file_path}' не найден в этой папке!")
except Exception as e:
    print(f"Ошибка при отправке: {e}")
