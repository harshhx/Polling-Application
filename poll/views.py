from django.shortcuts import render


# Create your views here.

def home(request):
    return render(request, "poll/home.html", {})


def create(request):
    return render(request, "poll/create.html", {})


def results(request, poll_id):
    return render(request, "poll/results.html", {})


def vote(request, poll_id):
    return render(request, "poll/vote.html", {})
