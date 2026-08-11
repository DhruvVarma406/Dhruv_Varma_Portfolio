from django.shortcuts import render, redirect
from .models import Contact
from .google_sheets import add_contact_to_sheet


def home(request):
    return render(request, 'home.html')


def success(request):
    return render(request, 'success.html')


def contact(request):

    if request.method == "POST":

        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")

        # Save contact in Django database
        contact = Contact.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message
        )

        # Save the same contact in Google Sheets
        add_contact_to_sheet(
            contact.name,
            contact.email,
            contact.subject,
            contact.message,
            contact.created_at
        )

        return redirect("success")

    return redirect("home")