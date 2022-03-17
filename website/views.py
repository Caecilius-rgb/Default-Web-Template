from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'website/home.html')

def bot(request):
    return render(request, 'website/bot.html')

def commands(request):
    return render(request, 'website/commands.html')

def test(request):
    return render(request, 'website/test.html')