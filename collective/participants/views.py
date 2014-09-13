from django.shortcuts import render
from django.http import HttpResponse
from participants.models import Participant
import twilio.twiml
from twilio.rest import TwilioRestClient
import urllib2

def index(request):
    return render(request, 'Collective/website/index.html')


def recieve_text(request):
    number   = request.GET['From']
    textBody = request.GET['Body']
    numbers = [p.number for p in Participant.objects.all()]

    if "off" in textBody.lower():
        urllib2.urlopen("https://agent.electricimp.com/leRzGyr7qLZn?state=0&number=1").read()
    else:
        urllib2.urlopen("https://agent.electricimp.com/leRzGyr7qLZn?state=1&number="+textBody).read()



    #ACCOUNT_SID = "AC26cf52f20d934430deaa4b8c7bec76b4" 
    #AUTH_TOKEN = "" 
 
    #client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN) 
 
    #client.messages.create(
    #to=number, 
    #from_="+12892719788", 
    #body=body,  
    #)
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



def newLocation(command, cart):
    if (cart.x=="A" and cart.y=="0"):
        if cart.o=="N":
            if command=="F":
                return "A1"
            elif command=="L":
                return "B0"
            elif command=="R":
                return "B0"
        elif cart.o=="E":
            if command=="F":
                return "B0"
            elif command=="L":
                return "A1"
            elif command=="R":
                return "A1"
        elif cart.o=="S":
            if command=="F":
                return "A0"
            elif command=="L":
                return "B0"
            elif command=="R":
                return "A1"
        elif cart.o=="W":
            if command=="F":
                return "A0"
            elif command=="L":
                return "B0"
            elif command=="R":
                return "A1"
    #A1
    if (cart.x=="A" and cart.y=="1"):
        if cart.o=="N":
            if command=="F":
                return "A2"
            elif command=="L":
                return "A0"
            elif command=="R":
                return "B1"
        elif cart.o=="E":
            if command=="F":
                return "B1"
            elif command=="L":
                return "A2"
            elif command=="R":
                return "A0"
        elif cart.o=="S":
            if command=="F":
                return "A0"
            elif command=="L":
                return "B1"
            elif command=="R":
                return "A2"
        elif cart.o=="W":
            if command=="F":
                return "A1"
            elif command=="L":
                return "A0"
            elif command=="R":
                return "A2"             
    #A2
    if (cart.x=="A" and cart.y=="2"):
        if cart.o=="N":
            if command=="F":
                return "A3"
            elif command=="L":
                return "A1"
            elif command=="R":
                return "B2"
        elif cart.o=="E":
            if command=="F":
                return "B2"
            elif command=="L":
                return "A3"
            elif command=="R":
                return "A1"
        elif cart.o=="S":
            if command=="F":
                return "A1"
            elif command=="L":
                return "B2"
            elif command=="R":
                return "A3"
        elif cart.o=="W":
            if command=="F":
                return "A2"
            elif command=="L":
                return "A1"
            elif command=="R":
                return "A3"
    #A3
    if (cart.x=="A" and cart.y=="3"):
        if cart.o=="N":
            if command=="F":
                return "A3"
            elif command=="L":
                return "A2"
            elif command=="R":
                return "B3"
        elif cart.o=="E":
            if command=="F":
                return "B3"
            elif command=="L":
                return "A2"
            elif command=="R":
                return "A2"
        elif cart.o=="S":
            if command=="F":
                return "A2"
            elif command=="L":
                return "B3"
            elif command=="R":
                return "B3"
        elif cart.o=="W":
            if command=="F":
                return "A3"
            elif command=="L":
                return "A2"
            elif command=="R":
                return "B3"
    #B0
    if (cart.x=="A" and cart.y=="1"):
        if cart.o=="N":
            if command=="F":
                return "A2"
            elif command=="L":
                return "A0"
            elif command=="R":
                return "B1"
        elif cart.o=="E":
            if command=="F":
                return "B1"
            elif command=="L":
                return "A2"
            elif command=="R":
                return "A0"
        elif cart.o=="S":
            if command=="F":
                return "A0"
            elif command=="L":
                return "B1"
            elif command=="R":
                return "A2"
        elif cart.o=="W":
            if command=="F":
                return "A1"
            elif command=="L":
                return "A0"
            elif command=="R":
                return "A2"
    #B0
    if (cart.x=="B" and cart.y=="0"):
        if cart.o=="N":
            if command=="F":
                return "B1"
            elif command=="L":
                return "A0"
            elif command=="R":
                return "C0"
        elif cart.o=="E":
            if command=="F":
                return "C0"
            elif command=="L":
                return "B1"
            elif command=="R":
                return "A0"
        elif cart.o=="S":
            if command=="F":
                return "B0"
            elif command=="L":
                return "C0"
            elif command=="R":
                return "A0"
        elif cart.o=="W":
            if command=="F":
                return "A0"
            elif command=="L":
                return "C0"
            elif command=="R":
                return "B1"
    #B1
    if (cart.x=="B" and cart.y=="1"):
        if cart.o=="N":
            if command=="F":
                return "B2"
            elif command=="L":
                return "A1"
            elif command=="R":
                return "C1"
        elif cart.o=="E":
            if command=="F":
                return "C1"
            elif command=="L":
                return "B2"
            elif command=="R":
                return "B0"
        elif cart.o=="S":
            if command=="F":
                return "B0"
            elif command=="L":
                return "C1"
            elif command=="R":
                return "A1"
        elif cart.o=="W":
            if command=="F":
                return "A1"
            elif command=="L":
                return "B0"
            elif command=="R":
                return "B2"
    #B2
    if (cart.x=="B" and cart.y=="2"):
        if cart.o=="N":
            if command=="F":
                return "B3"
            elif command=="L":
                return "A2"
            elif command=="R":
                return "C2"
        elif cart.o=="E":
            if command=="F":
                return "C2"
            elif command=="L":
                return "B3"
            elif command=="R":
                return "B1"
        elif cart.o=="S":
            if command=="F":
                return "B2"
            elif command=="L":
                return "C2"
            elif command=="R":
                return "A2"
        elif cart.o=="W":
            if command=="F":
                return "A2"
            elif command=="L":
                return "B1"
            elif command=="R":
                return "B3"
    #B3
    if (cart.x=="B" and cart.y=="3"):
        if cart.o=="N":
            if command=="F":
                return "B3"
            elif command=="L":
                return "A3"
            elif command=="R":
                return "C3"
        elif cart.o=="E":
            if command=="F":
                return "C3"
            elif command=="L":
                return "A3"
            elif command=="R":
                return "B2"
        elif cart.o=="S":
            if command=="F":
                return "B2"
            elif command=="L":
                return "C3"
            elif command=="R":
                return "A3"
        elif cart.o=="W":
            if command=="F":
                return "A3"
            elif command=="L":
                return "B2"
            elif command=="R":
                return "C3"
    #C0
    if (cart.x=="C" and cart.y=="0"):
        if cart.o=="N":
            if command=="F":
                return "C1"
            elif command=="L":
                return "B0"
            elif command=="R":
                return "D0"
        elif cart.o=="E":
            if command=="F":
                return "D0"
            elif command=="L":
                return "C1"
            elif command=="R":
                return "B0"
        elif cart.o=="S":
            if command=="F":
                return "C0"
            elif command=="L":
                return "D0"
            elif command=="R":
                return "B0"
        elif cart.o=="W":
            if command=="F":
                return "B0"
            elif command=="L":
                return "D0"
            elif command=="R":
                return "C1"
    #C1
    if (cart.x=="C" and cart.y=="1"):
        if cart.o=="N":
            if command=="F":
                return "C2"
            elif command=="L":
                return "B1"
            elif command=="R":
                return "D1"
        elif cart.o=="E":
            if command=="F":
                return "D1"
            elif command=="L":
                return "C2"
            elif command=="R":
                return "C0"
        elif cart.o=="S":
            if command=="F":
                return "C0"
            elif command=="L":
                return "D1"
            elif command=="R":
                return "B1"
        elif cart.o=="W":
            if command=="F":
                return "B1"
            elif command=="L":
                return "C0"
            elif command=="R":
                return "C2"
    #C2
    if (cart.x=="C" and cart.y=="2"):
        if cart.o=="N":
            if command=="F":
                return "C3"
            elif command=="L":
                return "B2"
            elif command=="R":
                return "D2"
        elif cart.o=="E":
            if command=="F":
                return "D2"
            elif command=="L":
                return "C3"
            elif command=="R":
                return "C1"
        elif cart.o=="S":
            if command=="F":
                return "C1"
            elif command=="L":
                return "D2"
            elif command=="R":
                return "B2"
        elif cart.o=="W":
            if command=="F":
                return "B2"
            elif command=="L":
                return "C1"
            elif command=="R":
                return "C3"
    #C3
    if (cart.x=="C" and cart.y=="3"):
        if cart.o=="N":
            if command=="F":
                return "C3"
            elif command=="L":
                return "B3"
            elif command=="R":
                return "D3"
        elif cart.o=="E":
            if command=="F":
                return "D3"
            elif command=="L":
                return "B3"
            elif command=="R":
                return "C2"
        elif cart.o=="S":
            if command=="F":
                return "C2"
            elif command=="L":
                return "D3"
            elif command=="R":
                return "B3"
        elif cart.o=="W":
            if command=="F":
                return "B3"
            elif command=="L":
                return "C2"
            elif command=="R":
                return "D3"
    #D0
    if (cart.x=="D" and cart.y=="0"):
        if cart.o=="N":
            if command=="F":
                return "D1"
            elif command=="L":
                return "C0"
            elif command=="R":
                return "C0"
        elif cart.o=="E":
            if command=="F":
                return "D0"
            elif command=="L":
                return "D1"
            elif command=="R":
                return "C0"
        elif cart.o=="S":
            if command=="F":
                return "D0"
            elif command=="L":
                return "D1"
            elif command=="R":
                return "C0"
        elif cart.o=="W":
            if command=="F":
                return "C0"
            elif command=="L":
                return "D1"
            elif command=="R":
                return "D1"
    #D1
    if (cart.x=="D" and cart.y=="1"):
        if cart.o=="N":
            if command=="F":
                return "D2"
            elif command=="L":
                return "C1"
            elif command=="R":
                return "D0"
        elif cart.o=="E":
            if command=="F":
                return "D1"
            elif command=="L":
                return "D2"
            elif command=="R":
                return "D0"
        elif cart.o=="S":
            if command=="F":
                return "D0"
            elif command=="L":
                return "D2"
            elif command=="R":
                return "C1"
        elif cart.o=="W":
            if command=="F":
                return "C1"
            elif command=="L":
                return "D0"
            elif command=="R":
                return "D2"
    #D2
    if (cart.x=="D" and cart.y=="2"):
        if cart.o=="N":
            if command=="F":
                return "D3"
            elif command=="L":
                return "C2"
            elif command=="R":
                return "D1"
        elif cart.o=="E":
            if command=="F":
                return "D2"
            elif command=="L":
                return "D3"
            elif command=="R":
                return "D1"
        elif cart.o=="S":
            if command=="F":
                return "D1"
            elif command=="L":
                return "D2"
            elif command=="R":
                return "C2"
        elif cart.o=="W":
            if command=="F":
                return "C2"
            elif command=="L":
                return "D3"
            elif command=="R":
                return "D3"
    #D3
    if (cart.x=="D" and cart.y=="3"):
        if cart.o=="N":
            if command=="F":
                return "D3"
            elif command=="L":
                return "C3"
            elif command=="R":
                return "D2"
        elif cart.o=="E":
            if command=="F":
                return "D3"
            elif command=="L":
                return "C3"
            elif command=="R":
                return "D2"
        elif cart.o=="S":
            if command=="F":
                return "D2"
            elif command=="L":
                return "C3"
            elif command=="R":
                return "C3"
        elif cart.o=="W":
            if command=="F":
                return "C3"
            elif command=="L":
                return "D2"
            elif command=="R":
                return "D2"
    else:
        return "n/a"