#Create Travel Booking
def book(request, id):
    travel = Travels.objects.get(id=id)
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.travel = travel
            booking.save()

            #Send Email To Admin
            subject = 'New Booking Created'
            message = f'A new booking has been created:\n\nTravel: {travel.name}\nPeriod: {booking.start_date} to {booking.end_date}\nClient: {booking.client_name}\nContact: {booking.contact_email}'
            from_email = booking.contact_email
            recipient_list = ['estmuch254@gmail.com']

            send_mail(subject, message, from_email, recipient_list)
            
            return redirect('bookings')
    else:
        form = BookingForm()

    context = {
        'travel': travel,
        'form':form
    }

    return render(request, "booking.html", context)