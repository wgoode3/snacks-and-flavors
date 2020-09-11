from django.shortcuts import render, redirect
from .models import Snack, Flavor

# Create your views here.
def index(request):
    context = {"snacks": Snack.objects.all()}
    return render(request, "index.html", context)

def create(request):
    print(request.POST)
    Snack.objects.create(
        name=request.POST["name"],
        calories=request.POST["calories"]
    )
    return redirect("/")

def new_flavor(request, s_id):
    context = {
        "snack": Snack.objects.get(id=s_id) 
    }
    return render(request, "flavor.html", context)

def add_flavor(request, s_id):
    print(request.POST)
    Flavor.objects.create(name=request.POST["name"], snack_id=s_id)
    return redirect(f"/snacks/{s_id}")