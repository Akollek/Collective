from django.shortcuts import render
from django.http import HttpResponse
from participants.models import Participant

def index(request):
    return HttpResponse("Test")


def create_user(request):

