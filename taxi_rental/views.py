from django.shortcuts import render, redirect

# Create your views here.


def home(request):

    print(" Home Page is Invoked Successfully ")

    return render(request,'index.html')

def fetch_destination(request):

    request.session['start'] = request.POST['location']
    request.session['end'] = request.POST['destination']

    return redirect('/')

def checkout(request):



    return redirect('/')
