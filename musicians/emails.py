from django.core.mail import EmailMultiAlternatives
from django.conf import settings


def send_add_alert(sender, receiver):
    subject, from_email, to = 'You are popular!', settings.DEFAULT_FROM_EMAIL, '{}'.format(receiver.email)
    text_content = 'Great news! {} {} added you to their top call list! Stay tuned for gig alerts. To view gig invitations, sign in to your GigForte account!'.format(sender.first_name, sender.last_name)
    html_content = '<p>Great news! {} {} added you to their top call list! Stay tuned for gig alerts.</p> <p>To view gig invitations, sign in to your GigForte account: <a href="https://gig-forte-1.herokuapp.com/">GigForte</a></p>'.format(sender.first_name, sender.last_name)
    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    msg.attach_alternative(html_content, "text/html")
    msg.send()

def invite_new_user(request):
    sender_name = request.user.first_name + ' ' + request.user.last_name
    invitee = request.POST['musician_first_name']
    invitee_email = request.POST['musician_email']

    subject, from_email = 'You are invited!', settings.DEFAULT_FROM_EMAIL
    text_content = 'Great news! {} would like to send you gig offers through the GigForte platform. To receive performing opportunities from {}, create an account at https://www.gigforte.com!'.format(sender_name, request.user.first_name)

    html_content = '<p>Hey {},</p><p>Great news! {} would like to send you gig offers through the GigForte platform.</p> <p>To receive performing opportunities from {}, please create an account here: <a href="https://www.gigforte.com/">GigForte</a></p'.format(invitee, sender_name, request.user.first_name)

    msg = EmailMultiAlternatives(subject, text_content, from_email, [invitee_email])
    msg.attach_alternative(html_content, "text/html")
    msg.send()