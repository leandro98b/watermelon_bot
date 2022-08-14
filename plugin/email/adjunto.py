import smtplib
import config

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders



def upload (nombre):
    nombre_archivo = nombre

    fromaddr = config.fromaddr
    toadd = config.toaddr
    msg = MIMEMultipart()
    msg['From'] = "leandrojavier@disroot.org"
    msg['To'] = "leandrojev@estudiantes.uci.cu"
    msg['Subjecct'] = "Mensaje adjunto"
      
    body = "click para abrir"
    msg.attach(MIMEText(body, 'plain'))
    adjunto = open(nombre_archivo, "rb")
    parte = MIMEBase('appliation', 'octet-stream')
    parte.set_payload((adjunto).read())
    encoders.encode_base64(parte)
    parte.add_header('Content-Disposition', "attacment;filename= %s" % nombre_arcchivo)
    msg.attach(parte)

    server = smtplib.SMTP('disroot.org', 587)
    server.starttls()
    server.login(config.fromaddr, config.password)
    texto = msg.as_string()
    server.sendmail(config.fromaddr, config.toaddr, texto)
    server.quit()