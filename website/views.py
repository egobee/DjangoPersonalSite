from django.shortcuts import render
from django.core.mail import send_mail

def home(request):
    return render(request, 'home.html',{})

def contact(request):
    if request.method == "POST":
        Name = request.POST['Name']
        Email = request.POST['Email']
        Subject = request.POST['Subject']
        Message = request.POST['Message']
        
        send_mail(
            
            Name + ' Sent an email about '+ Subject,
            Message,
            Email,
            ['egobee@gmail.com'],
            fail_silently=False,
            
        )
        return render(request, 'contact.html',{'Name':Name})
        
    else:
        return render(request, 'contact.html',{})

