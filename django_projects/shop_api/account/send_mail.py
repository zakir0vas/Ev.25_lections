from django.core.mail import send_mail

def send_confirmation_email(user, code):
    full_link = f'http://localhost:8000/api/v1/accounts/activate/{code}/'
    send_mail(
        'Здравствуйте активируйте ваш аккаунт!',
        f'Чтобы активировать ваш аккаунт вам нужно пройти по ссылке: \n{full_link}',
        'saikalzakirova07@gmail.com',
        [user],
        fail_silently=False
    )