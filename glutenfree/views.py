from django.shortcuts import render
from .models import Glutenfree 

def index(request):

    template_name = "glutenfree/index.html"
    glutenfrees = Glutenfree.objects.all()
    context = {
        "glutenfrees": glutenfrees
    }
    return render(request, template_name, context)

