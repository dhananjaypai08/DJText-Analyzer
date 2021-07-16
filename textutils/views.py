from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    #return HttpResponse('Home')
    params={'name':'Dhananjay','place':'mumbai'}
    return render(request,'index.html',params)

def analyze(request):
    djtext=request.POST.get('text','default')
    removepunc=request.POST.get('removepuncs','off')
    fullcap=request.POST.get('fullcaps','off')
    charcount=request.POST.get('charcount','off')

    print(removepunc)#to check if the checkbox i s selected or not
    print(djtext)

    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    txt = ''

    if removepunc=='on':
        for char in djtext:
            if char not in punctuations:
                txt+=char
        param={'purpose':'Text after Removing punctuations ','analyzed_text':txt}
        djtext = txt
    
    if fullcap=='on':
        capital=''
        for char in djtext:
            capital+=char.upper()
        param={'purpose':'Capitalized text ','analyzed_text':capital}
        djtext = capital

    if charcount=='on':
        count = 0
        for num in djtext:
            if num!=" ":
                count+=1
        param={'purpose':'Character count ','analyzed_text':djtext+" "+str(count)}
        djtext = txt+" "+str(count)
        
    if (removepunc !='on' and fullcap!='on' and charcount!='on'):
        return HttpResponse('Error')
    return render(request,'analyze.html',param)

def aboutus(request):
    return render(request,'about_us.html')
    