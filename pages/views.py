from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
from django.shortcuts import render, get_object_or_404, redirect
from .models import ServiceSection, HomePage, WhyBestSection, PricingSection, AboutCard, WebDevelopmentPage, Enquiry

def home(request):
    home = HomePage.objects.first()
    why_best = WhyBestSection.objects.first()
    
    context ={
        "home": home,
        "why_best": why_best,
    }
    return render(request, "pages/home.html", context)

def web_development(request):
    page = WebDevelopmentPage.objects.first()
    services = ServiceSection.objects.filter(page_type='web')
    price = PricingSection.objects.filter(page_type='web')

    context = {
        'page': page,
        'services': services,
        'price': price,
    }
    return render(request, 'pages/web_development.html', context)

def software_development(request):
    services = ServiceSection.objects.filter(page_type='software')
    return render(request, 'pages/software_development.html', {'services': services})

def digital_marketing(request):
    services = ServiceSection.objects.filter(page_type='digital')
    price = PricingSection.objects.filter(page_type='digital')
    
    context = {
        'services': services,
        'price': price,
    }

    return render(request, 'pages/digital_marketing.html', context)

def about_us(request):
    services = ServiceSection.objects.filter(page_type='about')
    cards = AboutCard.objects.filter(
        is_active=True
    ).order_by('order')

    context = {
        'services': services,
        'cards': cards
    }
    return render(request, 'pages/about_us.html', context)


# =========================
# ENQUIRY (SAVE + EMAIL)
# =========================
def enquiry(request):
    if request.method == "POST":

        # 1️⃣ SAVE TO DATABASE
        enquiry_obj = Enquiry.objects.create(
            name=request.POST.get("name"),
            email=request.POST.get("email"),
            phone=request.POST.get("phone"),
            service=request.POST.get("service"),
            message=request.POST.get("message"),
        )

        # -------------------------
        # 2️⃣ EMAIL TO ADMIN
        # -------------------------
        admin_subject = "New Enquiry - Vetri IT Systems"

        admin_message = f"""
New enquiry received:

Name: {enquiry_obj.name}
Email: {enquiry_obj.email}
Phone: {enquiry_obj.phone}
Service: {enquiry_obj.service}

Message:
{enquiry_obj.message}
        """

        send_mail(
            admin_subject,
            admin_message,
            settings.DEFAULT_FROM_EMAIL,
            [settings.ADMIN_EMAIL],
            fail_silently=False,
        )

        # -------------------------
        # 3️⃣ AUTO-REPLY TO USER
        # -------------------------
        user_subject = "Thank you for contacting Vetri IT Systems"

        user_message = render_to_string(
            "emails/enquiry_reply.txt",
            {
                "name": enquiry_obj.name,
                "service": enquiry_obj.service,
            }
        )

        send_mail(
            user_subject,
            user_message,
            settings.DEFAULT_FROM_EMAIL,
            [enquiry_obj.email],
            fail_silently=False,
        )

    return redirect("home")