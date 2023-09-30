from django.shortcuts import get_object_or_404, render,redirect
from .models import *
from .forms import *
from django.core.mail import send_mail, EmailMessage
from django.utils.translation import gettext as _
from django.utils.translation import get_language, activate, gettext
from django.core.paginator import Paginator

# def homex(request):
#     trans = translate(language='en')
#     return render(request, 'homex.html', {'trans': trans})

def translate(language):
    cur_language = get_language()
    try:
        activate(language)
        text = gettext('hello')
    finally:
        activate(cur_language)
    return text

def home(request):
    trans = translate(language='en')
    travels = Travels.objects.all()[:4]
    context = {
        'travels': travels,
        'trans': trans,
    }
    return render(request, 'base.html', context)



#View all travel listings


#View an individual travel listing
def travel(request, id):
    travel = Travels.objects.get(id=id)
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.travel = travel
            booking.save()
            #Sending the email
            subject = 'Thank you for booking your trip with us!'
            message = f'Jambo, {booking.client_name}\n\n'
            message += f'Thank you for booking with us a trip to {booking.travel} from {booking.start_date} to {booking.end_date}\n\n'
            message += f'One of our very able account managers will get in touch with you shortly😊'
            from_email = 'ernestmucheru254@gmail.com'
            recipient_list = [booking.contact_email]
            cc_list = ['ernestmucheru254@gmail.com']


            send_mail(subject, message, from_email, recipient_list)

            cc_subject = 'New Booking'
            cc_message = f'A new booking has arrived!.'
            cc_message = f'Dear esteemed account manager,\n\n'
            cc_message += f'{booking.client_name} has booked a trip with us a trip to {booking.travel} from {booking.start_date} to {booking.end_date}\n\n Kindly reach out to them ASAP on {booking.contact_email} for further planning.'
            message += f'One of our very able account managers will get in touch with you shortly😊'
            cc_recipient_list = ['ernestmucheru254@gmail.com']  # Replace with the desired CC recipient's email address

            cc_email = EmailMessage(cc_subject, cc_message, from_email, cc_recipient_list)
            cc_email.send()

            return redirect('success')
    else:
        form = BookingForm()

    context = {
        'travel': travel,
        'form':form
    }

    return render(request, 'destination_details.html', context)

def success(request):
   
    return render(request, 'success.html')

#Create a travel listing
def createtravel(request):
    if request.method == "POST":
        form = TravelForm(request.POST, request.FILES)
        if form.is_valid():
            travel = form.save(commit=False)
            travel.save()
            return redirect('home')
    else:
        form = TravelForm()
    return render(request, 'go/travels_form.html', {'form': form})



#View Your Bookings
def bookings(request):
    bookings = Booking.objects.all()
    context = {
        'bookings': bookings
    }
    return render(request, 'myBookings.html', context)

# View all Travels Available on destinations.html
def destinations(request):
    travels = Travels.objects.order_by('name')
    paginator = Paginator(travels, 4)

    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)

    context = {
        'travels':travels,
        'page':page,
    }
    return render(request, 'destinations.html', context)

