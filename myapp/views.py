from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .forms import ContactForm

def index(request):
    sent=False
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            subject = f"Email from {cd['f_name']} address {cd['email']}"
            message = f"The Message {cd['message']}"
            send_mail(
                subject,
                message,
                'zbdtechpro@gmail.com',
                ['shohruz.zubaidov@gmail.com'],
            )
            send = True
        return redirect('index')
    else:
        form = ContactForm()

    return render(request, 'index.html', {'form': form, 'sent':sent})