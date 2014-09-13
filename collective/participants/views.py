from django.shortcuts import render
from django.http import HttpResponse
from participants.models import Participant
import twilio.twiml
from twilio.rest import TwilioRestClient

def index(request):
    return render(request, 'Collective/website/index.html')


def recieve_text(request):
    number   = request.GET['From']
    textBody = request.GET['Body']
    numbers = [p.number for p in Participant.objects.all()]

    if "hi" in textBody.lower():
        body="Hello there!"
    elif "bye" in textBody.lower():
        body="Goodbye!"
    else:
        body="You didn't send a greeting"
    ACCOUNT_SID = "AC26cf52f20d934430deaa4b8c7bec76b4" 
    AUTH_TOKEN = "" 
 
    client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN) 
 
    client.messages.create(
    to=number, 
    from_="+12892719788", 
    body=body,  
    )
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
