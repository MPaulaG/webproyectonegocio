from django.shortcuts import render , redirect
from .forms import ContactForm 
from django.urls import reverse
from django.core.mail import EmailMessage

# Create your views here.
def contact(request):
    contactForm= ContactForm()
       
    if request.method=="POST":
        contactForm=ContactForm(data=request.POST)
        name=request.POST.get('name', '')
        email=request.POST.get('email', '')
        title=request.POST.get('title', '')
        content=request.POST.get('content', '')
        email=EmailMessage(
            "GLA Tax Solutions: Nuevo mensaje",
            "De{}<{}>\n\n Asunto:\n\n{}\n\n Mensaje:\n\n{}".format(name,email,title,content),
            "Paula"
            "automatico"
            "no-contestar@inbox.mailtrap.io",
            ["mpaula_12@live.com"],
            reply_to=[email]
        )
        
        try:
            email.send()
            print("Bienvenido a GLA Tax Solutions")
            return redirect(reverse('contact')+"?ok")
        except:
            return redirect(reverse('contact')+"?fail")



    return render(request,"contact/contact.html", {'contactForm':contactForm})
