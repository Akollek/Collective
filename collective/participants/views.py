from django.shortcuts import render
from django.http import HttpResponse
from participants.models import Participant
import twilio.twiml

def index(request):
    return HttpResponse("Test")


def recieve_text(request):
    textBody = request.GET['Body']
    return HttpResponse("You sent the text: " + textBody)