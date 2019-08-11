import json
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
import pyrebase
import cv2
import matplotlib.pyplot as plt
from .models import UserData, Claim, ProcessedClaim
from django.core.files.base import ContentFile


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
storage = firebase.storage()



def get_current_user(request):
    uid = request.session['uid']
    user = auth.get_account_info(uid)
    return user['users'][0]

def get_no_of_users(request):
    users = database.child('users').get().val()
    return len(users)


def dashboard(request):
    user = get_current_user(request)
    no_of_users = get_no_of_users(request)

    claims = Claim.objects.filter(user_id=user['localId'])
    claim_count = Claim.objects.count()
    p_claim_count = ProcessedClaim.objects.count()

    context = {
        'user': user,
        'page': 'dashboard',
        'claims': claims,
        'claim_count': claim_count,
        'p_claim_count': p_claim_count,
        'no_of_users': no_of_users
    }
    return render(request, 'dashboard.html', context)


def updateProfile(request):
    user = get_current_user(request)
    if request.method == 'POST':
        user_data = {
            'username': request.POST['username'],
            'first_name': request.POST['firstName'],
            'last_name': request.POST['lastName'],
            'mobile': request.POST['mobile'],
            'email': request.POST['email'],
            'city': request.POST['city'],
            'state': request.POST['state'],
            'address': request.POST['address'],
        }

        database.child('users').child(user['localId']).child('details').set(user_data)

        return dashboard(request)
    else:
        context = {
            'user': user
        }
        return render(request, 'profile.html', context)


def scratchDetection(request):
    user = get_current_user(request)
    if request.method == 'POST' and request.FILES['image']:
        new_claim = Claim()
        new_claim.claim_id = new_claim.setClaimId()
        new_claim.user_id = user['localId']
        new_claim.model_name = request.POST['name']
        new_claim.brand = request.POST['brand']
        new_claim.device_image = request.FILES['image']
        new_claim.save()

        claim = Claim.objects.filter(claim_id=new_claim.claim_id)[0]

        imgpath = '/home/thephenom1708/DigiClaim/digiclaim' + claim.device_image.url

        img = cv2.imread(imgpath, 0)
        denoised = cv2.medianBlur(img, 3)

        L1 = cv2.Canny(denoised, 50, 300, L2gradient=False)

        L2 = cv2.Canny(denoised, 100, 150, L2gradient=True)

        titles = ['Original Image', 'L1 Norm', 'L2 Norm', 'Denoised']

        outputs = [img, L1, L2, denoised]

        #cv2.imwrite("../images/" + claim.claim_id + '_' + 'pre_L1.jpeg', L1)
        #cv2.imwrite("../images/" + claim.claim_id + '_' + 'pre_L2.jpeg', L2)

        for i in range(4):
            plt.subplot(1, 4, i + 1)
            plt.imshow(outputs[i], cmap='gray')
            plt.title(titles[i])
            plt.xticks([])
            plt.yticks([])
        plt.show()
        print(type(L1))
        z = L1.shape
        print(z)
        uplimit = (z[0] * 13) // 100
        for i in range(z[0]):
            for j in range(z[1]):
                if L1[i][j] > 150:
                    L1[i][j] = 255
                else:
                    L1[i][j] = 0

        y = L2.shape
        for i in range(y[0]):
            for j in range(y[1]):
                if L2[i][j] > 150:
                    L2[i][j] = 255
                else:
                    L2[i][j] = 0

        count = 0
        totcount = 0;
        print(y)
        for i in range(uplimit, z[0] - uplimit):
            for j in range(15, z[1] - 15):
                totcount = totcount + 1;
                if L1[i][j] == 255:
                    print(str(i) + " " + str(j) + " " + str(L1[i][j]))
                    count = count + 1

        print("Count " + str(count))
        print("Total " + str(totcount))
        z = L1.shape
        print(z)
        print(uplimit)
        print(z[0] - uplimit)

        flag = False
        if count > 100:
            flag = True
            print("Scratch on Screen")
        else:
            flag = False
            print("Scratch not present on screen")

        cv2.imwrite("/home/thephenom1708/DigiClaim/digiclaim/images/" + claim.claim_id + '_' + 'denoised.jpeg', denoised)
        cv2.imwrite("/home/thephenom1708/DigiClaim/digiclaim/images/" + claim.claim_id + '_' + 'L1.jpeg', L1)
        cv2.imwrite("/home/thephenom1708/DigiClaim/digiclaim/images/" + claim.claim_id + '_' + 'L2.jpeg', L2)

        denoised_img = open("/home/thephenom1708/DigiClaim/digiclaim/images/" + claim.claim_id + '_' + 'denoised.jpeg', 'rb')
        l1 = open("/home/thephenom1708/DigiClaim/digiclaim/images/" + claim.claim_id + '_' + 'L1.jpeg', 'rb')
        l2 = open("/home/thephenom1708/DigiClaim/digiclaim/images/" + claim.claim_id + '_' + 'L2.jpeg', 'rb')

        denoised_content = ContentFile(denoised_img.read())
        l1_content = ContentFile(l1.read())
        l2_content = ContentFile(l2.read())

        new_processed_claim = ProcessedClaim()
        new_processed_claim.claim_id = claim.claim_id
        new_processed_claim.initial_image = claim.device_image
        new_processed_claim.scratch_flag = flag

        new_processed_claim.image_denoised.save(claim.claim_id + '_' + 'denoised.jpeg', denoised_content)
        new_processed_claim.image_l1.save(claim.claim_id + '_' + 'L1.jpeg', l1_content)
        new_processed_claim.image_l2.save(claim.claim_id + '_' + 'L2.jpeg', l2_content)

        new_processed_claim.save()

        device_data = database.child('users').child(user['localId']).child('PhoneAttributes').get().val()

        pdf = storage.child(user['localId'] + '/PDF').get_url(None)

        context = {
            'user': user,
            'flag': flag,
            'claim': new_claim,
            'processed_claim': new_processed_claim,
            'brand': device_data['Brand'],
            'sdk': device_data['SDK'],
            'model_id': device_data['Id'],
            'version_code': device_data['Version Code'],
            'pdf': pdf,
            'page': 'scratchDetection'
        }
        return render(request, 'result.html', context)

    else:
        context = {
            'user': user,
            'page': 'scratchDetection'
        }
        return render(request, 'scratchDetection.html', context)


def claimInfo(request, claim_id):
    user = get_current_user(request)
    claim = Claim.objects.filter(claim_id=claim_id)
    processed_claim = ProcessedClaim.objects.filter(claim_id=claim_id)

    device_data = database.child('users').child(user['localId']).child('PhoneAttributes').get().val()

    pdf = storage.child(user['localId'] + '/PDF').get_url(None)

    context = {
        'user': user,
        'flag': processed_claim[0].scratch_flag,
        'claim': claim[0],
        'processed_claim': processed_claim[0],
        'brand': device_data['Brand'],
        'sdk': device_data['SDK'],
        'model_id': device_data['Id'],
        'version_code': device_data['Version Code'],
        'pdf':pdf,
        'page': 'scratchDetection'
    }

    return render(request, 'result.html', context)




