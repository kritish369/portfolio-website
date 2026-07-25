from django.http import HttpResponse
from django.shortcuts import render

# Simple view that returns text
def home(request):
    return render(request, 'home.html')  # Render the home.html template
def about(request):
    return render(request, 'about.html')  # Render the about.html template
def skills(request):
    return render(request, 'skills.html')  # Render the skills.html template
def contact(request):
    return render(request, 'contact.html')  # Render the contact.html template
def projects(request):
    return render(request, 'projects.html')  # Render the projects.html template
def bootstrap(request):
    return render(request,"bootstrap.html")  # Render the bootstrap.html template
# View that renders an HTML template
