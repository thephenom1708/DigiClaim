import json
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from .models import User
from detection.models import Claim, ProcessedClaim
import pyrebase


config = {
    'apiKey': "AIzaSyDkQWQjchqJICUemhhKDdDwOWYuDs1Fhwc",
    'authDomain': "digiclaiminsurance.firebaseapp.com",
    'databaseURL': "https://digiclaiminsurance.firebaseio.com",
    'projectId': "digiclaiminsurance",
    'storageBucket': "digiclaiminsurance.appspot.com",
    'messagingSenderId': "615762764001"
};
firebase = pyrebase.initialize_app(config);
auth = firebase.auth()
database = firebase.database()



def get_current_user(request):
    uid = request.session['uid']
    user = auth.get_account_info(uid)
    return user['users'][0]


def index(request):
    return render(request, 'index.html')


def register(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        new_user = auth.create_user_with_email_and_password(email, password)
        user = auth.sign_in_with_email_and_password(email, password)

        request.session['uid'] = user['idToken']
        print(user)

        context = {
            'user': user,
        }

        return render(request, 'profile.html', context)
    else:
        return render(request, 'register.html')



def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        try:
            user = auth.sign_in_with_email_and_password(email, password)
            request.session['uid'] = user['idToken']
            request.session['localId'] = user['localId']
            print(user['localId'])

            id = user['localId']
            claims = Claim.objects.filter(user_id=str(id))
            claim_count = Claim.objects.count()
            p_claim_count = ProcessedClaim.objects.count()
            user_count = 10

            context = {
                'user': user,
                'page': 'dashboard',
                'claims': claims,
                'claim_count': claim_count,
                'p_claim_count': p_claim_count,
                'user_count': user_count
            }
            return render(request, 'dashboard.html', context)

        except Exception:
            context = {
                'error_msg': 'Invalid Credentials! Please try again !!!'
            }
            return render(request, 'login.html', context)
    else:
        return render(request, 'login.html')


def logout(request):
    return render(request, 'index.html')
