from django.shortcuts import render

tasks = ["soccer","cycling","coding","gaming","school","work"]

# Create your views here.
def index(request):
    return render(request, "tasks/index.html", {
        "tasks": tasks
    })
    