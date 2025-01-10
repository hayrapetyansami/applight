from django.contrib import messages
from django.shortcuts import render, get_object_or_404

from .models import (
    Banner,
    About,
    WatchNow,
    FeaturesCentral,
    Team,
    Testimonials,
    FAQ,
    Block,
    Contact,
    FormSubmission
)


def index(request):
    if request.method == "POST":
        full_name = request.POST.get("full-name")
        email = request.POST.get("email")
        subject = request.POST.get("subject", "")
        message = request.POST.get("message")
      
        FormSubmission.objects.create(
            full_name=full_name,
            email=email,
            subject=subject,
            message=message
        )
        
        messages.success(request, "Your message has been sent successfully !")
      
    
    banner = get_object_or_404(Banner)
    about = About.objects.all()
    watchNow = get_object_or_404(WatchNow)
    features = get_object_or_404(FeaturesCentral)
    features_items = features.items.all()
    team = Team.objects.all()
    testimonials = Testimonials.objects.all()
    faq = FAQ.objects.all()
    block = Block.objects.all()
    contact = Contact.objects.first()

    data = {
        "banner": banner,
        "about": about,
        "watchNow": watchNow,
        "features": features,
        "features_items": features_items,
        "team": team,
        "testimonials": testimonials,
        "faq": faq,
        "block": block,
        "contact": contact
    }

    return render(request, "base.html", data)
