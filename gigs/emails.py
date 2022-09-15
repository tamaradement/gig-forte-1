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

    subject= 'Gig Cancelation'
    text_content = 'Uh oh! Your gig with {} on {} has been canceled :-( For more updates, sign into your account on GigForte, or contact your bandleader: {}'.format(bandleader, date, bandleader_email)

    html_content = '<p>Uh oh! Your gig with {} on {} has been canceled :-(</p> <p>For more updates, sign into your account on GigForte: <a href="https://gig-forte-1.herokuapp.com/">GigForte</a>, or contact your bandleader: {}</p>'.format(bandleader, date, bandleader_email)

    msg = EmailMultiAlternatives(subject, text_content, from_email, to_emails)
    msg.attach_alternative(html_content, "text/html")
    msg.send()

    