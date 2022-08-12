from django.http import HttpResponse
from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect




class AddTask(forms.Form):
    task = forms.CharField(label="New Task")
    priority = forms.IntegerField(label="Priority", min_value = 1, max_value = 15)


# Create your views here.
def index(request):
    if "tasks" not in request.session:
        request.session["tasks"] = []

    return render(request, "tasks/index.html", {
        "tasks": request.session["tasks"]
    })
    
def add(request):
    if request.method == "POST":
        form = AddTask(request.POST)
        if form.is_valid():
            task = form.cleaned_data["task"]
            request.session["tasks"] += [task]
            return HttpResponseRedirect("/tasks/")
        else:
            return render(request, "tasks/add.html", {
                "form": form
                })

    return render(request, "tasks/add.html", {
        "form":AddTask()
    })