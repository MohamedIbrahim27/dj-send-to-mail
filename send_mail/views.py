from django.shortcuts import render,redirect
from django.contrib.auth.models import User
# Create your views here.
from django.core.mail import send_mail,EmailMultiAlternatives
from django.conf import settings
from django.template.loader import render_to_string
from.models import Contact
def home(request):
    if request.method == 'POST':
        username=request.POST['username']
        phone=request.POST['phone']
        message=request.POST['message']
        print(username)
        print(phone)
        print(message)
        Contact.objects.create(
            name=username,
            phone=phone,
            message=message,
        )
        # user=request.user
        # mailsubject='congratulation'
        # messge=f"hi {user.username} you send {message} ,{phone} .wait admin to responise you "
        # email_send=settings.EMAIL_HOST_USER
        # recive=[user.email,]
        # emailmessage=send_mail(mailsubject,messge,email_send,recive,)
        
        context={
            'username':username,
            'phone':phone,
            'message':message,
        }
        # subject = render_to_string("message_subject.txt").strip().replace('\n', '')
        text_body = render_to_string("message.html", context)
        html_body = render_to_string("message.html", context)
        user=request.user
        usenmail=User.objects.get(username=user)
        print(usenmail.email)
        msg = EmailMultiAlternatives(
            # subject=subject,
            from_email=settings.EMAIL_HOST_USER,
            to=[usenmail.email,],
            body=text_body
        )
        msg.attach_alternative(html_body, "text/html")
        msg.send()
        print('done')
        return redirect('/')
    return render(request,"index.html")