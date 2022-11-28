from django.http import HttpResponse
from django.shortcuts import render
def about(request):
    return render(request, 'home.html')
def reversed(request):
    user_text = request.GET['usertext']
    reversed_text = user_text[::-1]
    text_len = len(user_text.split())
    return render(request,'reversed.html',{'usertext' : user_text,'reversedtext': reversed_text,'text': text_len})