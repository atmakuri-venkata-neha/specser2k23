from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Events,Registrations
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from .checksum import generate_checksum,verify_checksum
from django.http import HttpResponseRedirect

# Create your views here.
def home(request):
    return render(request,'index.html')

def aboutus(request):
   
    return render(request,'AboutUs.html')
def events(request,id):
    pk = int(id)
    event = Events.objects.get(id=pk)
    return render(request,'Event.html',{
        'event':event
    })
def user(request):
    return render(request,'UserProfile.html')

def login(request):
    return render(request,'login.html')

@login_required
def updateuser(request):
    if request.method=='POST':
        user = request.user
        phone=request.POST.get('phone')
        college=request.POST.get('college')
        year_of_study=request.POST.get('year_of_study')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        # print(user.phone)
        if phone and len(str(phone))<10:
            error = 'enter valid phone number'
            return render(request,'UserProfile.html',{"error":error})
        else:
            if phone:
                user.phone=phone
            if college:
                user.college=college
            if  year_of_study:
                user.year_of_study=year_of_study
            if first_name:
                user.first_name = first_name
            if last_name:
                user.last_name = last_name
            user.save()
            return redirect('/user')
        

def techevents(request):
    techevents = Events.objects.filter(event_type_id=2)
    return render(request,'TechnicalEvents.html',{'techevents':techevents})


def nontechevents(request):
    events = Events.objects.filter(event_type_id=1)
    return render(request,'NonTechnicalEvent.html',{'nontechevents':events})



def intiatepayment(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            user = request.user
            event_id = request.POST.get('event')
            event = Events.objects.get(id=event_id)
            amount = int(request.POST.get('amount'))
            if user.events_registered==0:
                regestration_amount=100
                amount=amount+100
            else:
                regestration_amount=0
            phone = request.POST.get('phone')
            if phone:
                user.phone=phone
                user.save()
            return render(request,'Paytmform.html',{
            'event': event,
            'amount':amount,
            'reg_fee':regestration_amount
        })
    else:
        msg = 'Please login before proceeding for payment'
        return redirect('/signin')


@login_required
def makepayment(request):
    if request.method=='POST':
        user = request.user
        amount = int(request.POST.get('amount'))
        if user.events_registered:
            user.events_registered+=1
            user.save()
        else:
            user.events_registered=1
            user.save()
        event = request.POST.get('event') 
        eve = Events.objects.get(id=event)
        if eve.event_type==2:
            user.flag=1
            user.save()
        else:
            user.flag=2
            user.save()
        regestration = Registrations.objects.create(user = user.id,
                                                    event=event,
                                                    amount=amount)   
        regestration.save()
        merchant_key = settings.PAYTM_SECRET_KEY
        # print(amount)
        params = (
        ('MID','gMzudj06810822142325'),
        ('ORDER_ID', str(regestration.id)),
        ('CUST_ID', str(regestration.user)),
        ('TXN_AMOUNT', str(regestration.amount)),
        ('CHANNEL_ID', settings.PAYTM_CHANNEL_ID),
        ('WEBSITE', settings.PAYTM_WEBSITE),
        ('EMAIL', request.user.email),
        # ('MOBILE_N0',settings.MOBILE_NUMBER),
        ('INDUSTRY_TYPE_ID', settings.PAYTM_INDUSTRY_TYPE_ID),
        ('CALLBACK_URL', 'http://127.0.0.1:8000/callback/'),
        # ('PAYMENT_MODE_ONLY', 'NO'),
            )
        paytm_params = dict(params)
        checksum = generate_checksum(paytm_params, merchant_key)

        regestration.checksum = checksum
        regestration.save()

        paytm_params['CHECKSUMHASH'] = checksum
        # print('SENT: ', checksum)
        return render(request, 'redirect.html', {"context":paytm_params})
    
    

@csrf_exempt
def handlerequest(request):
    # paytm will send you post request here
    form = request.POST
    response_dict = {}
    for i in form.keys():
        response_dict[i] = form[i]
        if i == 'CHECKSUMHASH':
            checksum = form[i]

    verify =verify_checksum(response_dict, settings.PAYTM_SECRET_KEY, checksum)
    if verify:
        if response_dict['RESPCODE'] == '01':
            print('order successful')
        else:
            print('order was not successful because' + response_dict['RESPMSG'])
    return render(request, 'paymentstatus.html', {'response': response_dict})


    
def sponsors(request):
    return render(request,'OurSponsors.html')


def workshop(request):
    workshop = Events.objects.get(id=17)
    return render(request,'workshop.html',{'event':workshop})


def mworkshop(request):
    workshop = Events.objects.get(id=18)
    return render(request,'3dworkshop.html',{'event':workshop})