from django.shortcuts import render, redirect
from .forms import CreatePoll
from .models import Poll


# Create your views here.

def home(request):
    polls = Poll.objects.all()
    context = {
        "polls": polls
    }
    return render(request, "poll/home.html", context)


def create(request):
    if request.method == "POST":
        form = CreatePoll(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = CreatePoll()
    context = {
        "form": form
    }
    return render(request, "poll/create.html", context)


def results(request, poll_id):
    return render(request, "poll/results.html", {})


def vote(request, poll_id):
    return render(request, "poll/vote.html", {})
