from django.core.mail import send_mail


class EmailService:
    @staticmethod
    def send_email(from_email, to_email, subject, text):
        send_mail(
            subject=subject,
            message=text,
            from_email=from_email,
            recipient_list=[to_email],
            fail_silently=False,
        )
