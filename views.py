from django.shortcuts import render

def home(request):
    return render(request, 'home.html')  # Render the home template
def about(request):
    return render(request, 'about.html')