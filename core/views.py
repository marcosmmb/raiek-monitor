from django.shortcuts import render
import requests

# Create your views here.

URLBASE = '188.166.149.243:5000'

def post_request(url, data = {}):
    r = requests.post(url, data)
    return r.json()

def home(request):
    return render(request, "home.html")

def accountInformation(request):    

    if(request.method=="POST"):
        acc = request.POST.get('account')
        d = {'account_value': acc}

        url = 'http://' + URLBASE + '/get_account_information'
        j = post_request(url, d)

        return render(request,"accountInformation.html", j)
    
    return render(request,"accountInformation.html")

def accountHistory(request):

    if(request.method=="POST"):
        acc = request.POST.get('account')
        count = request.POST.get('count')
        d = {'account_value': acc, 'count_value': count}
    
        url = 'http://' + URLBASE + '/get_account_history'
        j = post_request(url, d)

        return render(request,"accountHistory.html", j)

    return render(request,"accountHistory.html")

def blockCount(request):

    if(request.method=="GET"):
        d = {}
    
        url = 'http://' + URLBASE + '/get_block_count'
        j = post_request(url, d)

        return render(request,"blockCount.html", j)

    if(request.method=="POST"):
        d = {}
    
        url = 'http://' + URLBASE + '/get_block_count'
        j = post_request(url, d)

        return render(request,"blockCount.html", j)

    return render(request,"blockCount.html")

def representativesOnline(request):

    if(request.method=="GET"):
        d = {}
    
        url = 'http://' + URLBASE + '/get_online_representatives'
        j = post_request(url, d)
        reps = j["representatives"]
        lp = len(reps)
        j["len"] = lp

        return render(request,"representativesOnline.html", j)

    if(request.method=="POST"):
        d = {}
    
        url = 'http://' + URLBASE + '/get_online_representatives'
        j = post_request(url, d)
        reps = j["representatives"]
        lp = len(reps)
        j["len"] = lp

        return render(request,"representativesOnline.html", j)

    return render(request,"representativesOnline.html")

def nodeVersion(request):

    if(request.method=="GET"):
        d = {}
    
        url = 'http://' + URLBASE + '/get_node_version'
        j = post_request(url, d)

        return render(request,"nodeVersion.html", j)

    return render(request,"nodeVersion.html")
