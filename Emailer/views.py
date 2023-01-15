from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here
def index(request):
    if request.method == "POST":
        login_data = request.POST.dict()
        print(login_data)
        email_list = request.POST.get("email_input")
        print(email_list)
        email_body = request.POST.get("email_body")
        print(email_body)
        send_mail(
        subject = 'Automated Email Test',message = email_body,from_email = "testproject@github.com",
        recipient_list = [email_list])


    return render(request,"EmailSend.html")