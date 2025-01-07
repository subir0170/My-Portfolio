from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages

def contact(request: HttpRequest):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        number = request.POST.get('number')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

       


        # Prepare the email content
        email_message = f'''
        You have received a new message:

        Name: {name}
        Email: {email}
        Phone Number: {number}
        Subject: {subject}
        Message: {message}
        '''

        # Send the email
        try:
            send_mail(
                subject,
                email_message,
                settings.EMAIL_HOST_USER,  # Use the email from settings
                ['aiondatta1234@gmail.com'],  # Replace with your recipient email
                fail_silently=True,
            )
            messages.success(request, 'Your message has been sent successfully!')
            return redirect('')  # Redirect to a success page after sending
        except Exception as e:
            #messages.error(request, 'Please try again.')
            print(f"Error sending email: {e}")
            # Optionally, you can render an error message here
            

    return render(request, 'index.html', {})