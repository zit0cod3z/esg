from django.shortcuts import render, redirect
import qrcode
import base64
import os
from PIL import Image
from django.http import HttpResponse
from esg_app.models import Registration
from django.views.decorators.csrf import csrf_protect
from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings
from .models import *
from io import BytesIO
from django.contrib.sites.shortcuts import get_current_site
# from PIL import Image

# Create your views here.
def register(request):
	if request.method == "POST":
		name = request.POST.get("name")
		nationality = request.POST.get("nationality")
		email = request.POST.get("email")
		organization = request.POST.get("organization")
		industry = request.POST.get("industry")
		position = request.POST.get("position")
		event = request.POST.get("event")
		instance = Registration(name=name, nationality=nationality, email=email, organization=organization, industry=industry, position=position, event=event)
		# instance.save()
		# qr_content = f"Name: {name}, Nationality: {nationality}, Organization: {organization}, Designation: {position}, Industry: {industry}"
		# qr_img = qrcode.make(qr_content)
		# qr_img = qr_img.resize((200, 200)) 
		# buffered = BytesIO()
		# qr_img.save(buffered, format="PNG")
		# qr_img_str = base64.b64encode(buffered.getvalue()).decode('utf-8')

		qr_content = f"Name: {name}, Nationality: {nationality}, Organization: {organization}, Designation: {position}, Industry: {industry}"
		qr_img = qrcode.make(qr_content)
		qr_codes_dir = os.path.join(settings.MEDIA_ROOT, 'qr_codes')
		os.makedirs(qr_codes_dir, exist_ok=True)
		qr_img_path = os.path.join(settings.MEDIA_ROOT, 'qr_codes', f'{instance.id}.png')
		qr_img.save(qr_img_path)
		qr_img_url = f"{settings.MEDIA_URL}qr_codes/{instance.id}.png"
		# filename = f"qr_code.png"
		current_site = get_current_site(request)
		# if settings.DEBUG:
		# 	qr_img_url = f"http://{current_site.domain}{settings.MEDIA_URL}qr_codes/{instance.id}.png"
		# else:
		qr_img_url = f"https://esg-registration.onrender.com{settings.MEDIA_URL}qr_codes/{instance.id}.png"
		instance.save()

		# mail = EmailMessage(
		# 	'AFRIDU REGISTRATION CONFIRMATION',
		# 	f'Hello {name}, \n  Thank you for registering to attend the upcoming AFRIDU HOMECOMING Event in Abuja, Nigeria. Scheduled to take place from 17th to 27th October 2024.\n Please note: Your visitor pass will be emailed to you the week before the event. Please ensure you bring it to registration on arrival with a form of identification. \n AFRIDU Office Address: 13B, Mambila Street off Aso Drive, Abuja.\n  Please note that only VIP delegate pass holders will be permitted to attend all events premises.\n We look forward to welcoming you to the HOMECOMING EVENT October 16th to 27th 2024 INTERNATIONAL GATHERING IN HONOUR OF AFRICAN DESCENDANTS IN DIASPORA \n .............................................................\n Yours In Nation Building Arch. Prof, Chidiebere Analechi Ogbu AFRIDU President\n ................................................................\n For Delegate, Sponsorship and Exhibition Opportunities please contact: Diplomatic Administrator Dr.Breakforth Onwubuya on +234 803 349 4643 or email AFRIDU.ORG \n Get the latest updates afridu.org.',
		# 	settings.EMAIL_HOST_USER,
		# 	[email]

		# )
		my_subject = "ESG REGISTRATION CONFIRMATION"
		my_recipient = email
		mailer = settings.EMAIL_HOST_USER
		welcome_message = name


		html_message = render_to_string("esg_app/email.html", {"instance": instance, "qr_img_url": qr_img_url})
		plain_message = strip_tags(html_message)

		message = EmailMultiAlternatives(
			subject = my_subject,
			body = plain_message,
			from_email = mailer,
			to = [my_recipient],
		)

		message.attach_alternative(html_message, "text/html")
		message.send()
		return render(request, 'esg_app/thanks.html')


	return render(request, 'esg_app/index.html')