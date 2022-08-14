import smtplib
import config

server = smtplib.SMTP('disroot.org', 587)
server.starttls()
server.login(config.fromaddr, config.password)
mensaje = "otra prueba mas"
server.sendmail(config.fromaddr, config.toaddr, mensaje)
server.quit()