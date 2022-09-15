from django.core.mail import EmailMultiAlternatives
from django.conf import settings


def send_add_alert(sender, receiver):
    subject, from_email, to = 'You are popular!', settings.DEFAULT_FROM_EMAIL, '{}'.format(receiver.email)
    text_content = 'Great news! {} {} added you to their top call list! Stay tuned for gig alerts. To view gig invitations, sign in to your GigForte account!'.format(sender.first_name, sender.last_name)
    html_content = '<p>Great news! {} {} added you to their top call list! Stay tuned for gig alerts.</p> <p>To view gig invitations, sign in to your GigForte account: <a href="https://gig-forte-1.herokuapp.com/">GigForte</a></p>'.format(sender.first_name, sender.last_name)
    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    msg.attach_alternative(html_content, "text/html")
    msg.send()

    