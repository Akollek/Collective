from django.shortcuts import render
from django.http import HttpResponse
from participants.models import Participant, Cart
import twilio.twiml
from twilio.rest import TwilioRestClient
import urllib2
from socketIO_client import SocketIO
import pusher



def index(request):
    return render(request, 'index.html')

def arrived(request):
    if request.GET["arrived"]=="true":
        cart = Cart.objects.get(id=1)
        cart.busy = False
        cart.save()
        return HttpResponse("arrived")

def recieve_text(request):
    ACCOUNT_SID = "AC26cf52f20d934430deaa4b8c7bec76b4" 
    AUTH_TOKEN = "2768e19093ff757adc2173edaf9080e0" 
    states = {
        'AK': '1',
        'AR': '3',
        'AZ': '4',
        'CA': '5',
        'CO': '6',
        'CT': '7',
        'DE': '8',
        'FL': '9',
        'GA': '10',
        'IA': '12',
        'ID': '13',
        'IL': '14',
        'IN': '15',
        'KS': '16',
        'KY': '17',
        'LA': '18',
        'MA': '19',
        'MD': '20',
        'ME': '21',
        'MI': '22',
        'MN': '23',
        'MO': '24',
        'MS': '25',
        'MT': '26',
        'NC': '27',
        'ND': '28',
        'NE': '29',
        'NH': '30',
        'NJ': '31',
        'NM': '32',
        'NV': '33',
        'NY': '34',
        'OH': '35',
        'OK': '36',
        'OR': '37',
        'PA': '38',
        'RI': '39',
        'SC': '40',
        'SD': '41',
        'TN': '42',
        'TX': '43',
        'UT': '44',
        'VA': '45',
        'VT': '46',
        'WA': '47',
        'WI': '48',
        'WV': '49',
        'WY': '50'
    }
    state = request.GET['FromState']
    if state not in states:
        client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN) 
        client.messages.create(
            to=request.GET["From"], 
            from_="+12892719788", 
            body="Sorry, your state or province is not supported",  
        )
        return HttpResponse("Bad State")
    p = pusher.Pusher(
        app_id='89419',
        key='252fc5137f1d1fcb5ea2',
        secret='22c2c9e013e94dd206e2'
    )


    pusher['incoming'].trigger('text', {
    'state': states[state]
    })


    #number   = request.GET['From']
    #numbers = [p.number for p in Participant.objects.all()]

    #if number not in numbers:
    #    return create_participant(request)

    #participant = Participant.objects.get(number=number)

    #cmd = request.GET['Body']

    #if cmd.lower() == "collect":
        # if cart.x+cart.y == cart.node:
        #     participant.score += 100
        # else:
        #     participant.score -= 50 


    #if cart.busy:
    #    return HttpResponse("Busy")
    #else:
    #    cart.busy = True
    #    cart.save()


    #if "f" in cmd[:2].lower():
        #urllib2.urlopen("https://agent.electricimp.com/leRzGyr7qLZn?pin=1")
    #    new = newLocation("F", cart)
    #    cart.x = new[0]
    #    cart.y = new[1]
        #cart.o = new[2]

    #if "l" in cmd[:2].lower():
        #urllib2.urlopen("https://agent.electricimp.com/leRzGyr7qLZn?pin=2")
    #    new = newLocation("L", cart)
    #     cart.x = new[0]
    #     cart.y = new[1]
    #     #cart.o = new[2]

    # if "r" in cmd[:2].lower():
    #     #urllib2.urlopen("https://agent.electricimp.com/leRzGyr7qLZn?pin=5")
    #     new = newLocation("R", cart)
    #     cart.x = new[0]
    #     cart.y = new[1]
    #     #cart.o = new[2]

    #if "off" in textBody.lower():
    #    urllib2.urlopen("https://agent.electricimp.com/leRzGyr7qLZn?state=0&number=1").read()
    #else:
    #    urllib2.urlopen("https://agent.electricimp.com/leRzGyr7qLZn?state=1&number="+textBody).read()



 
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
    return HttpResponse("You sent the text: " + cmd + " from the user " + participant.username)



def drive(request):
    body=request.GET["Body"].lower()
    if "green" in body:
        urllib2.urlopen("https://agent.electricimp.com/leRzGyr7qLZn/?pin=7&value=1")
        return HttpResponse("GO")
    elif "red" in body:
        urllib2.urlopen("https://agent.electricimp.com/leRzGyr7qLZn/?pin=7&value=0")
        return HttpResponse("STOP")
    return HttpResponse("NO COMMAND")



def create_participant(request):
    number   = request.GET['From']
    username = request.GET['Body']
    Participant.objects.create(number=number,username=username)
    return HttpResponse("OK")


