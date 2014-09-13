from django.shortcuts import render
from django.http import HttpResponse
from participants.models import Participant
import twilio.twiml

def index(request):
    return render(request, 'Collective/website/index.html')


def recieve_text(request):
    number   = request.GET['From']
    textBody = request.GET['Body']
    numbers = [p.number for p in Participant.objects.all()]
    #if number in numbers:
    #    execute_command(request)
    #else:
    #    create_participant(request)
    return HttpResponse("You sent the text: " + textBody + " from the number " + number)


def create_participant(request):
    number   = request.GET['From']
    username = request.GET['Body']
    Participant.objects.create(number=number,username=username)
    return("OK")

#def execute_command(request):
