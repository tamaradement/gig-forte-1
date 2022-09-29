from django.core.mail import EmailMultiAlternatives
from django.conf import settings


def send_gig_cancel_alert(gig):
    personnel = gig.personnel.all()
    bandleader = gig.bandleader.first_name + ' ' + gig.bandleader.last_name
    bandleader_email = gig.bandleader.email
    date = gig.event_date.strftime('%m/%d/%y')
    from_email = settings.DEFAULT_FROM_EMAIL
    to_emails = []

    for person in personnel:
        to_emails.append(person.email)

    subject = 'Gig Cancelation'
    text_content = 'Uh oh! Your gig with {} on {} has been canceled :-( For more updates, sign into your account on GigForte, or contact your bandleader: {}'.format(bandleader, date, bandleader_email)

    html_content = '<p>Uh oh! Your gig with {} on {} has been canceled :-(</p> <p>For more updates, sign into your account on GigForte: <a href="https://www.gigforte.com/">GigForte</a>, or contact your bandleader: {}</p>'.format(bandleader, date, bandleader_email)

    msg = EmailMultiAlternatives(subject, text_content, from_email, to_emails)
    msg.attach_alternative(html_content, "text/html")
    msg.send()

def send_initial_gig_alert(form):
    personnel = form.cleaned_data.get("personnel")
    bandleader = form.instance.bandleader.first_name + ' ' + form.instance.bandleader.last_name
    from_email = settings.DEFAULT_FROM_EMAIL
    to_emails = []

    for person in personnel:
        to_emails.append(person.email)
    
    subject = 'New gig offer!'

    text_content = 'Hello! You have a new gig offer from {} on GigForte :) To view details for this opportunity, sign in to your account at https://www.gigforte.com/ and navigate to Gig Invitations!'.format(bandleader) 

    html_content = '<p>Hello!</p> <p>You have a new gig offer from {} on GigForte :)</p> <p>To view gig details, or to accept/decline the offer, sign into your account! <a href="https://www.gigforte.com/gigs/gig_invites">GigForte</a></p>'.format(bandleader)
    
    msg = EmailMultiAlternatives(subject, text_content, from_email, to_emails)
    msg.attach_alternative(html_content, "text/html")
    msg.send()


    