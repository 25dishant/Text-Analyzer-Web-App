from django.http import HttpResponse
from django.shortcuts import render
import requests


def index(request):
    return render(request, 'index.html')


def analyze(request):

    return render(request, 'analyze.html')


def improvedstring(request):
    djtext = str(request.POST.get('inputtext', 'default'))
    rempuncsw1 = request.POST.get('rempuncsw1', 'off')
    capsw2 = request.POST.get('capsw2', 'off')
    titlesw3 = request.POST.get('titlesw3', 'off')
    remnlchsw4 = request.POST.get('remnlchsw4', 'off')
    remextspsw5 = request.POST.get('remextspsw5', 'off')
    charcountsw = request.POST.get('charcountsw6', 'off')
    puncs = """!#$%&'()*+,-/:;<=>?@[\]^_`{"|}~"""
    if rempuncsw1 == 'on':
        analyzed = ""
        for ch in djtext:
            if ch not in puncs:
                analyzed += ch
        djtext = analyzed
    if capsw2 == 'on':
        analyzed = ""
        analyzed = djtext.upper()
        djtext = analyzed
    if titlesw3 == 'on':
        analyzed = ""
        analyzed = djtext.title()
        djtext = analyzed
    if remnlchsw4 == 'on':
        analyzed = ""
        for ch in djtext:
            if ch != '\n' and ch != '\r':
                analyzed += ch
        djtext = analyzed
    if remextspsw5 == 'on':
        analyzed = ""
        for i, ch in enumerate(djtext):
            if i < len(djtext):
                if not (djtext[i] == " " and djtext[i+1] == " "):
                    analyzed += ch
        djtext = analyzed
    if charcountsw == 'on':
        count = len(djtext)
    else:
        count = 'not yet asked'
    analyzed = djtext
    params = {'result': analyzed, 'charcount': count}
    return render(request, 'improvedstring.html', params)


def contact(request):
    return render(request, 'contact.html')
