import os
import secrets
from PIL import Image
from flask import url_for, current_app


def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, fext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + fext
    picture_path = os.path.join(current_app.root_path,
                                'static',
                                'profile_pics',
                                picture_fn)
    output_size = (125, 125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)
    return picture_fn


def send_reset_email(user, sender, configdict=None):
    from flask_mail import Message
    from base_site import mail

    token = user.get_reset_token()
    msg = Message('Password Reset Request',
                  sender=sender,
                  recipients=[user.email])
    msg.body = f''' To reset your password, visit the following link:

{url_for('users.reset_token',token=token,_external=True)}

If you didn't make this request then simply ignore
this email and no changes will be made
'''
    mail.send(msg)


def send_reset_email_not_working_for_now(user, sender, configdict):
    """ sending email with sendgrid """
    from sendgrid import SendGridAPIClient
    from sendgrid.helpers.mail import Mail

    token = user.get_reset_token()
    content = list()
    content.append("<strong>To reset your password, visit the link: ")
    content.append(f"{url_for('users.reset_token',token={},_external=True)}")
    content.append("")
    content.append("If you didn't make this request then simply ignore")
    content.append("this email and no changes will be made</strong>")
    message = Mail(
        from_email=sender,
        to_emails=user.email,
        subject='Password Reset Request',
        html_content= "\n".join(content)
    )
    try:
        sg = SendGridAPIClient(configdict.get('SENDGRID_API_KEY'))
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
        return response
    except Exception as e:
        print(e)
    return ''