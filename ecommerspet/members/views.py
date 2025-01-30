from django.shortcuts import render,redirect
from .form import Participantform 

from django.shortcuts import render

def success(request):
    return render(request,"success.html")

def regeration(request):
    if request.method == "POST":
        # Process form data here...
        return render(request, "success.html")  # Ensure an HttpResponse is returned
    
    # If it's a GET request, return a response
    return render(request, "register.html")  # Ensure the template exis

# def regeration(request):
#     if request.method == 'POST' :
#         form = Participantform(request.POST)
#         if form.is_valid():
#             form.save()
#             return render(request,'regestration/succesfull.html')
#         else:
#             form = Participantform()
#         return render(request,'regestartion/register.html',{"form" : form})
        






# Create your views here.

