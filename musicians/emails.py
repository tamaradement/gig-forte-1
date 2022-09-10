from django.core.mail import send_mail

def send_add_alert(sender, receiver):
    send_mail(
        'You are popular!', 
        'Great news! {} {} added you to their top call list! Stay tuned for gig alerts. To view gig invitations, sign in to your account! https://gig-forte-1.herokuapp.com/'.format(sender.first_name, sender.last_name), 
        'tamara.dement@gmail.com', 
        [receiver.email], 
        fail_silently=False
    )