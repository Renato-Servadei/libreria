from flask_mail import Message
from flask import current_app, render_template
from threading import Thread

#envio de mails de manera sincrona
# def confirmacion_compra(mail, usuario, libro):
#     try:
#         message = Message('Confirmacion de compra de libro', 
#         sender = current_app.config['MAIL_USERNAME'], 
#         recipients=['brazukatekeremata@gmail.com'])
#         message.html = render_template('emails/confirmacion_compra.html', usuario=usuario, libro=libro)
#         mail.send(message)
#     except Exception as ex:
#         raise Exception(ex)

#envio asincrono
def confirmacion_compra(app, mail, usuario, libro):
    try:
        message = Message('Confirmacion de compra de libro', 
        sender = current_app.config['MAIL_USERNAME'], 
        recipients=['brazukatekeremata@gmail.com'])
        message.html = render_template('emails/confirmacion_compra.html', usuario=usuario, libro=libro)
        thread = Thread(target=envio_email_async, args=[app, mail, message])
        thread.start()
    except Exception as ex:
        raise Exception(ex)

def envio_email_async(app, mail, message):
    with app.app_context():
        mail.send(message)