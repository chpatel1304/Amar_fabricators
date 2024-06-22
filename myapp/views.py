from django.shortcuts import render
from .models import Contact,Career
from django.conf import settings
from django.core.mail import send_mail,EmailMessage,EmailMultiAlternatives
import os
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.core.files.temp import NamedTemporaryFile
from django.core.files.temp import gettempdir
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.templatetags.static import static


# Create your views here.
def index(request):
	return render(request,'index.html')

def home(request):
	return render(request,'index.html')

def aboutus(request):
	return render(request,'aboutus.html')

def manu_cap(request):
	return render(request,'manu_cap.html')

def career(request):
	if request.method=="POST":
		Career.objects.create(
				fullname=request.POST['fullname'],
				email=request.POST['email'],
				phone=request.POST['phone'],
				cv=request.FILES['cv']
			)
		if 'cv' in request.FILES:
            # Save the uploaded file to a temporary location with the original file name
			cv_file = request.FILES['cv']
			temp_dir = gettempdir()
			temp_file_path = os.path.join(temp_dir, cv_file.name)

			# Save the file to the temporary directory
			with open(temp_file_path, 'wb+') as temp_file:
			    for chunk in cv_file.chunks():
			        temp_file.write(chunk)

			# Email details
			subject = 'Thank You For Contact.'
			context = {
			    'fullname': request.POST['fullname'],
			    # 'email': request.POST['email'],
			    # 'message': request.POST.get('message', '')
			}
			email_from = settings.EMAIL_HOST_USER
			recipient_list = [request.POST['email']]

			# Render the HTML template with context data
			html_message = render_to_string('email_user.html', context)
			plain_message = strip_tags(html_message)

			# Create the email and attach the file
			email = EmailMultiAlternatives(subject, plain_message, email_from, recipient_list)
			email.content_subtype = 'html'  # Set the email content type to HTML
			email.attach_file(temp_file_path)
			email.content_subtype = 'html'  # Main content is text/html

			email.attach_alternative(html_message,"text/html")
			email.send()


			subject1 = 'New Contact Found.'
			context1 = {
			    'fullname': request.POST['fullname'],
			    'phone': request.POST['phone'],
			    'email': request.POST['email'],
			    # 'message': request.POST.get('message', '')
			}
			email_from1 = request.POST['email']
			recipient_list1 = [settings.EMAIL_HOST_USER]

			# Render the HTML template with context data
			html_message1 = render_to_string('email_admin.html', context1)
			plain_message1 = strip_tags(html_message1)

			# Create the email and attach the file
			email1 = EmailMultiAlternatives(subject1, plain_message1, email_from1, recipient_list1)
			email1.content_subtype = 'html'  # Set the email content type to HTML
			email1.attach_file(temp_file_path)
			email1.content_subtype = 'html'  # Main content is text/html

			email1.attach_alternative(html_message1,"text/html")
			email1.send()

			msg="Career Saved Successfully"
			return render(request,'career.html',{'msg':msg})

	else:
		return render(request,'career.html')

def contact(request):
	if request.method=="POST":
		Contact.objects.create(
				fullname=request.POST['fullname'],
				email=request.POST['email'],
				phone=request.POST['phone'],
				message=request.POST['message'],
			)

		subject = 'Thank You For Contact.'
		context = {
		    'fullname': request.POST['fullname'],
		    'phone': request.POST['phone'],
		    # 'email': request.POST['email'],
		    # 'message': request.POST.get('message', '')
		}
		email_from = settings.EMAIL_HOST_USER
		recipient_list = [request.POST['email']]

		# Render the HTML template with context data
		html_message = render_to_string('contact_email_user.html', context)
		plain_message = strip_tags(html_message)

		# Create the email and attach the file
		email = EmailMultiAlternatives(subject, plain_message, email_from, recipient_list)
		email.content_subtype = 'html'  # Set the email content type to HTML
		# email.attach_file(temp_file_path)
		email.content_subtype = 'html'  # Main content is text/html

		email.attach_alternative(html_message,"text/html")
		email.send()


		subject1 = 'New Contact Found.'
		context1 = {
		    'fullname': request.POST['fullname'],
		    'email': request.POST['email'],
		    'phone': request.POST['phone'],
		    'message': request.POST.get('message', '')
		}
		email_from1 = request.POST['email']
		recipient_list1 = [settings.EMAIL_HOST_USER]

		# Render the HTML template with context data
		html_message1 = render_to_string('contact_email_admin.html', context1)
		plain_message1 = strip_tags(html_message1)

		# Create the email and attach the file
		email1 = EmailMultiAlternatives(subject1, plain_message1, email_from1, recipient_list1)
		email1.content_subtype = 'html'  # Set the email content type to HTML
		# email1.attach_file(temp_file_path)
		email1.content_subtype = 'html'  # Main content is text/html

		email1.attach_alternative(html_message1,"text/html")
		email1.send()

		msg="Details Send Successfully"
		return render(request,'contact.html',{'msg':msg})

	else:
		return render(request,'contact.html')


def error_404_view(request, exception):
	print("custom")
	return render(request, '404.html')