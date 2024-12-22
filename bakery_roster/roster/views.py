from django.shortcuts import render, redirect
from .models import Staff, Roster

def index(request):
    return render(request, 'index.html')

def view_roster(request):
    staff_list = Staff.objects.all()
    roster_data = {staff: {day: "" for day in ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]} for staff in staff_list}
    
    for entry in Roster.objects.all():
        roster_data[entry.staff][entry.day] = entry.timeslot

    return render(request, 'roster.html', {'staff': staff_list, 'roster': roster_data})

def save_roster(request):
    if request.method == 'POST':
        Roster.objects.all().delete()  # Clear existing roster

        staff_list = Staff.objects.all()
        for staff in staff_list:
            for day in ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]:
                timeslot = request.POST.get(f"{staff.name}_{day}")
                if timeslot:
                    Roster.objects.create(staff=staff, day=day, timeslot=timeslot)

    return redirect('view_roster')