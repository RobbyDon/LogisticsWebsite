from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.decorators import login_required
from .models import ContactMessage, Tracking
import uuid


from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, 'core/index.html')
def tracking_form(request):
    return render(request, 'core/tracking_form.html')

def tracking_results(request):
    tracking_id = request.GET.get('tracking_id')
    return render(request, 'core/tracking_results.html', {'tracking_id': tracking_id})
def about(request):
    return render(request, 'core/about.html')
def cargo_transportation(request):
    return render(request, 'core/services/cargo_transportation.html')

def air_freight(request):
    return render(request, 'core/services/air_freight.html')

def ocean_freight(request):
    return render(request, 'core/services/ocean_freight.html')

def road_freight(request):
    return render(request, 'core/services/road_freight.html')
from .models import Tracking

def index(request):
    tracking_result = None
    if request.method == 'POST':
        tracking_id = request.POST.get('tracking_id')
        try:
            tracking_result = Tracking.objects.get(tracking_id=tracking_id)
        except Tracking.DoesNotExist:
            tracking_result = "not_found"
    
    return render(request, 'core/index.html', {'tracking_result': tracking_result})
def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Save to database
        ContactMessage.objects.create(
            name=name,
            phone=phone,
            email=email,
            message=message
        )

        # Send email to admin
        send_mail(
            f"New Contact Message from {name}",
            f"Phone: {phone}\nEmail: {email}\n\nMessage:\n{message}",
            settings.DEFAULT_FROM_EMAIL,
            [settings.CONTACT_RECEIVER_EMAIL],  # Set this in settings.py
            fail_silently=False,
        )

        # Show success message
        messages.success(request, 'Your message has been sent successfully!')
        return redirect('contact')  # Redirect to clear the form

    return render(request, 'core/contact.html')
from django.contrib.auth.decorators import login_required
from .models import Tracking
from django.utils.crypto import get_random_string
import uuid
from django.shortcuts import get_object_or_404

def generate_tracking_id():
    return 'TRX-' + uuid.uuid4().hex[:10].upper()

@login_required
def tracking_dashboard(request):
    if request.method == 'POST':
        # Deletion
        delete_id = request.GET.get('delete_id')
        if delete_id:
            Tracking.objects.filter(tracking_id=delete_id).delete()
            return redirect('tracking_dashboard')

        # Update
        update_id = request.GET.get('update_id')
        if update_id:
            tracking = get_object_or_404(Tracking, tracking_id=update_id)
            tracking.current_location = request.POST.get('current_location')
            tracking.status = request.POST.get('status')
            tracking.item = request.POST.get('item') or tracking.item
            weight_input = request.POST.get('weight')
            tracking.weight = float(weight_input) if weight_input else tracking.weight
            tracking.save()
            return redirect('tracking_dashboard')

        # New Entry
        Tracking.objects.create(
            tracking_id=generate_tracking_id(),
            customer_name=request.POST['customer_name'],
            origin=request.POST['origin'],
            destination=request.POST['destination'],
            current_location=request.POST['current_location'],
            item=request.POST['item'],
            weight=request.POST['weight'],
            status=request.POST['status'],
        )
        return redirect('tracking_dashboard')

    updates = Tracking.objects.all().order_by('-updated_at')
    return render(request, 'core/tracking_dashboard.html', {'updates': updates})

def tracking_results(request):
    tracking_id = request.GET.get('tracking_id')
    tracking_result = None
    if tracking_id:
        try:
            tracking_result = Tracking.objects.get(tracking_id=tracking_id)
        except Tracking.DoesNotExist:
            tracking_result = "not_found"
    return render(request, 'core/tracking_form.html', {'tracking_result': tracking_result})
