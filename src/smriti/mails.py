import sendgrid
from django.conf import settings

def sendgrid_mail(to, subject, content, asmid=False):
    client = sendgrid.SendGridClient(settings.SENDGRID_API_KEY)
    message = sendgrid.Mail()

    message.add_to("<"+to+">")
    message.set_from("Student Website NITK <"+settings.EMAIL_HOST_USER+">")
    message.set_subject(subject)
    message.set_html(content)

    if type(asmid) == int:
        message.smtpapi.set_asm_group_id(asmid)

    client.send(message)
