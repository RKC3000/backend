from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

tasks = []


# forms + client-side validation
class NewTaskForm(forms.Form):
    task = forms.CharField(label="New Task")


# Create your views here.
def index(request):
    return render(request, "tasks/index.html", {"tasks": tasks})


def add(request):
    if request.method == "POST":
        form = NewTaskForm(request.POST)
        if form.is_valid():  # check for valid
            task = form.cleaned_data["task"]  # if yes the add to list of task
            tasks.append(task)
            return HttpResponseRedirect(
                reverse("tasks:index")
            )  # this will be for the redirect to the index of tasks and this is done by reverse route
        else:
            return render(
                request, "tasks/add.html", {"form": form}
            )  # if not then just send back and tell them to check the validation

    return render(
        request, "tasks/add.html", {"form": NewTaskForm()}
    )  # if simple user want to GET the form, then empty form is given
