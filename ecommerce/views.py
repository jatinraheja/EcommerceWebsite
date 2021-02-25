from django.shortcuts import render
from ecommerce.models import Register
# Create your views here.
def index(request):
    return render(request,'index.html')

def contact(request):
    return render(request,'contacts.html')

def login(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        reigstered_users = Register.objects.all()
        for item in reigstered_users:
            if item.email == email and item.password == password:
                return render(request,'index.html')
                
    return render(request,'LogIn.html')

def register(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        password = request.POST.get("password")
        register = Register(name=name,email=email,phone=phone,password=password)
        register.save()
    return render(request,'register.html')

