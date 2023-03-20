from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from .user_info import UserInfo
from .verify_email import MailVerify
from . import writeintoDb
from .LoginCheck import checkLogin,checkRegister
from . BASEURL import BASE_URL
from django.views.decorators.csrf import csrf_exempt

# mail_check=MailVerify()
uf=UserInfo()

# Create your views here.
@csrf_exempt
def home_page_view(requests):
    if requests.method=="POST":
        email=requests.POST.get('email')
        password=requests.POST.get('pass')
        Message,IsValid=checkLogin(email=email,password=password)

        if IsValid:
            requests.session['isLogin']=True
            return redirect(BASE_URL+'movies')#after database code ,render movie page
        else:
            return render(requests,'front/home.html',{'BASE_URL':BASE_URL,'log':True,'reg':False,'otp':False,'Message':Message})#after database code ,render movie page

    else:
        data = requests.GET.get('data')
        if data!=None:
            return render(requests,'front/home.html',{'BASE_URL':BASE_URL,'log':True,'reg':False,'otp':False,'Message':data})
        else:
            return render(requests,'front/home.html',{'BASE_URL':BASE_URL,'log':True,'reg':False,'otp':False,'Message':""})


@csrf_exempt
def Register_page_view(requests):
    if requests.method=="GET":

        return render(requests,'front/home.html',{'BASE_URL':BASE_URL,'log':False,'reg':True,'otp':False,'Message':""})
    
    elif requests.method=='POST':

        fname=requests.POST.get('fname')
        lname=requests.POST.get('lname')
        email=requests.POST.get('email')
        college=requests.POST.get('cname')
        password=requests.POST.get('u_pass')

        # Check existing email
        isExist=checkRegister(email=email)
        if isExist:

            return render(requests,'front/home.html',{'BASE_URL':BASE_URL,'log':False,'reg':True,'otp':False,"Message":"Mail id has been registered already!"})
        else:
            uf.values(fname=fname,lname=lname,email=email,college=college,password=password)
            mail_check=MailVerify()
            otp_gen=mail_check.verifyOtp(email=email,name=(fname+" "+lname))
            
            uf.set_otp(otp=otp_gen)

            return render(requests,'front/home.html',{'BASE_URL':BASE_URL,'log':False,'reg':False,'otp':True,'email':email})

@csrf_exempt    
def Otpview(requests):
    if requests.method == 'POST':
        try:
            otp=requests.POST.get('otp_user')
            print(otp)
            if uf.check_otp(otp):
                print('Otp verified')
                writeintoDb.writeIntoDB(uf)
                return HttpResponseRedirect(redirect_to=BASE_URL)
            else :
                url = BASE_URL + '?data=' + "Wrong OTP ,Please Try again!"
                return HttpResponseRedirect(redirect_to=url)

            
        except:
            print("Error occured in redirecting")
            url =BASE_URL + '?data=' + ""
            return HttpResponseRedirect(redirect_to=url)
    else:
        return redirect(BASE_URL)

def logout(request):

    request.session['isLogin']=False
    print('log out function')
    return redirect(BASE_URL+'movies')