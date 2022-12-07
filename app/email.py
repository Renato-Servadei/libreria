from flask_mail import Message
from flask import current_app, render_template


def confirmacion_compra(mail, usuario, libro):
    try:
        message = Message('Confirmacion de compra de libro', 
        sender = current_app.config['MAIL_USERNAME'], 
        recipients=['brazukatekeremata@gmail.com'])
        message.html = render_template('emails/confirmacion_compra.html', usuario=usuario, libro=libro)
        mail.send(message)
    except Exception as ex:
        raise Exception(ex)
