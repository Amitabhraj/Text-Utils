'''i have created this file by own-Amitabh raj'''
from django.http import HttpResponse
from django.shortcuts import render


def Amitabh(request):
    return render(request, 'index.html')


# def about(request):
#     return HttpResponse("about Amitabh Bhai <a href='http://127.0.0.1:8000/'><p>Back button</p></a>")


def analyz(request):
    #take text
    dj= request.POST.get('text','default')
    
    
    #check checkbox value
    remove_punc= request.POST.get('removepunc','off')
    upper= request.POST.get('upper','off')
    newline= request.POST.get('newline','off')
    spaceRemover= request.POST.get('ExtraSpaceRemover','off')
    charcount= request.POST.get('CharacterCount','off')
    
    
    
    
    
    #check which checkbox is on
    if remove_punc=="on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed=""
        for char in dj:
            if char not in punctuations:
                analyzed= analyzed+char
                
        params={"comment":"Text is:-","purpose":"Removing Punctuation", "analyze_text":analyzed}
        return render(request, 'analyze.html', params)
    
    
    
    
    
    
    elif(upper=="on"):
        analyzed=""
        for char in dj:
            analyzed=analyzed+char.upper()
            
        params={"comment":"Text is:-","purpose":"capatilizing ", "analyze_text":analyzed}
        return render(request, 'analyze.html', params)
    
    
    
    
    
    elif(newline=="on"):
        analyzed=""
        for char in dj:
            if char!="\n" and char!="\r":
                analyzed=analyzed+char
                
        params={"comment":"Text is:-","purpose":"Removing Newline", "analyze_text":analyzed}
        return render(request, 'analyze.html', params)
    
    
    
    
    
    
    elif(spaceRemover=="on"):
        analyzed=""
        for index, char in enumerate(dj):
            if dj[index]==" " and dj[index+1]==" ":
                pass
            else:
                analyzed=analyzed+char
                 
        params={"comment":"Text is:-","purpose":"Removing Extra Space", "analyze_text":analyzed}
        return render(request, 'analyze.html', params)
    
    
    
    
    
    
    elif(charcount=="on"):
        analyzed=""
        for index, char in enumerate(dj):
            if dj[index]==" ":
                pass
            else:
                analyzed=analyzed+char
                anal=(len(analyzed))
                 
        params={"purpose":"Counting character present in Text", "analyze_text":anal,"char":"Character Count:-"}
        return render(request, 'analyze.html', params)
    
    
    
    
    
    else:
        return HttpResponse("<h1>ERROR</h1>")





# def capatilize_first(request):
#     return HttpResponse("capatilize first <a href='http://127.0.0.1:8000/removepunc'><p>Back button</p></a>")
# 
# 
# def space_remove(request):
#     return HttpResponse("space remove<a href='http://127.0.0.1:8000/capatilize'><p>Back button</p></a>")
# 
# 
# def newline(request):
#     return HttpResponse("newline <a href='http://127.0.0.1:8000/spaceremove'><p>Back button</p></a>")
# 
# 
# def charcount(request):
#     return HttpResponse("charcount <a href='http://127.0.0.1:8000/newline'><p>Back button</p></a>")
