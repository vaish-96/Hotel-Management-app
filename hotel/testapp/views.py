from django.shortcuts import render,redirect
from testapp.models import GuestDetails
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request,'index.html')

def checkin(request):
    if request.method == "POST":
        guest = GuestDetails(name=request.POST['name'],
                            address=request.POST['address'],
                            mobileno=request.POST['mobileno'],
                            noofdays=request.POST['noofdays'],
                            choose_type=request.POST['choose_type'],
                            payment_method=request.POST['payment_method'],)
        guest.save()
        return HttpResponse("HAI")
        # return redirect('/testapp/checkin/')
    else:
        guests = GuestDetails.objects.all()
        return render(request,'checkin.html',{'guests':guests})

def guestlist(request):
    guests = GuestDetails.objects.all()
    return render(request,'list.html',{'guests':guests})

def checkout(request):
    pass

# https://projectworlds.in/python-projects-with-source-code/hotel-management-system-python-tkinter-gui/