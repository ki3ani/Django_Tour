from datetime import datetime
from django.shortcuts import render
import datetime

# Create your views here.

def index(request):

    x = datetime.datetime.now()

    return render(request, "newyear/index.html", {
        "newyear": x.day == 1 and x.month == 1
    })