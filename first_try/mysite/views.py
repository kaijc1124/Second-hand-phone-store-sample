import json
import time
import urllib
from paypal.standard.forms import PayPalPaymentsForm
#from django.core.urlresolvers import reverse
from django.urls import reverse
from datetime import datetime

from django.shortcuts import render,redirect
from django.http import HttpResponse, Http404
from mysite.models import Post
from mysite.models import Phone_Product
from mysite.models import Phone_Product2
from mysite.models import Phone_Maker
from mysite.models import Phone_Model
from mysite.models import phone_cart
from mysite.models import Users
from mysite.models import born111
from plotly.offline import plot
import plotly.graph_objs as go
import numpy as np
from mysite.models import Email
from first_try import settings
from django.core.mail import EmailMessage
from mysite.models import phone_shopped2

# Create your views here.

def about(request):

    return render(request,"me.html")

def blog_list(request):

    blogs=Post.objects.all()

    return render(request, "blog_list.html", locals())


def blog_detail(request,tl):

    try:
        blog=Post.objects.get(title=tl)

    except Post.DoesNotExist:
        raise Http404('找不到部落格')

    now=datetime.now()

    return render(request,"blog_detail2.html",locals())

def homepage(request):

    return render(request,"homepage.html",locals())

def youtube(request,tvc=0):

    tv_list=[{"name":"新聞","tvcode":"wM0g8EoUZ_E","num":0},
             {"name":"音樂","tvcode":"L_a3fATxzIY","num":1},
             {"name":"動畫","tvcode":"2FJcu6qsM2k","num":2},]

    tv=tv_list[tvc]

    return render(request,"youtube.html",locals())

def phone(request):

    phone=Phone_Product2.objects.all().order_by("Model")
    maker=Phone_Maker.objects.all()

    smaker = None
    rest="0"
    ulog=""
    plog = ""
    ulogIn = ""
    logIn=""
    spas=""
    logOut =""
    mac=""
    uac = ""
    upas = ""
    m_logIn=False


    try:
        uac=request.POST['user-account']

    except:
        uac = ""

    if uac != "":
        ulog = True
    else:
        ulog = False

    try:
        upas = request.POST['user-password']
    except:
        upas=""

    if upas!="":
        plog = True
    else:
        plog=False

    #print(ulog, plog)


    try:
        smaker = request.GET.getlist("Maker")
        if smaker==[]:
            smaker = None

    except:

        pass

    try:
        rest=request.GET['rest']
    except:
        rest="0"

    if ulog==True and plog==True:
        try:
            spas=Users.objects.get(User_account=uac)
            ulogIn = True
        except:
            ulogIn = False

    if ulogIn:

        if spas.User_password!=upas:
            logIn=False

        else:
            logIn = True

    if logIn:
        request.session['account'] = uac
        request.session['logIn']=logIn

    try:
        logOut=request.POST["logOut"]

    except:
        logOut=None

    if logOut=="登出":
        request.session['logIn'] = False
        request.session['account'] = None

    try:
        m_logIn = request.session['logIn']
        mac = request.session['account']

    except:
        pass

    if m_logIn:
        request.session.set_expiry(60*60)





    return render(request,"phone_list.html",locals())

def phone_create(request):

    try:
        m_logIn = request.session['logIn']
        ac=request.session['account']
    except:
        m_logIn = False
        ac = False

    dele=""
    delet = False
    csuc = False

    product=Phone_Product2.objects.filter(Owner=ac)

    if not m_logIn:
        return redirect("/phone/")

    try:
        maker=request.POST["maker"]
        country=request.POST["country"]
        model=request.POST["model"]
        url=request.POST["url"]
        description=request.POST["description"]
        price=request.POST["price"]
        quantity=request.POST["quantity"]
        img = request.FILES.get("img")
        csuc=True

    except:
        csuc=False
        pass

    if csuc == True:
        try:
            Phone_Maker.objects.get(Maker=maker)
        except:
            Makers = Phone_Maker(Maker=maker, Country=country)
            Makers.save()

    if csuc == True:
        try:
            Phone_Model.objects.get(Model=model)
        except:
            m = Phone_Maker.objects.get(Maker=maker)
            mlSave=Phone_Model(Maker=m,Model=model,URL=url)
            mlSave.save()

    if csuc==True:
        mod=Phone_Model.objects.get(Model=model)
        psave=Phone_Product2(Model=mod,Description=description,Price=int(price),Quantity=int(quantity),Img=img,Owner=ac)
        psave.save()

    try:
        dele=request.POST["deletion"]

    except:
        pass

    if dele != "":
        try:
            id=Phone_Product2.objects.get(id=dele)
            id.delete()
            delet = True
        except:
            pass



    return render(request,"phone_create.html",locals())

def baby(request):
    """"""""""""""""""""""""""""""""""""""""""""""""""""
    datas=list()
    old=""
    with open("111born.csv","r",encoding="utf-8") as babys:
        read=babys.readlines()

    
    for i,d in enumerate(read):
        detail = d.replace(","," ")
        detail=detail.split(" ")
        if detail[0]!=old and i!=0:
            
                if old!="":
                    baby111Save = born111(City=save[0],Sum=save[1],Male=save[2],Female=save[3])
                    baby111Save.save()
            
            save=list()
            old = detail[0]
            datas.append(detail[0])


            save.append(old)
        if i!=0:
            datas.append(int(detail[2]))
            save.append(int(detail[2]))
    """""""""""""""""""""""""""""""""""""""""""""""""""""

    born=born111.objects.all().order_by("-Sum")

    citys=[]
    sums=[]
    males=[]
    females=[]


    for data in born:
        citys.append(data.City)
        sums.append(int(data.Sum))
        males.append(data.Male)
        females.append(data.Female)

    plot_display=plot([go.Bar(x=citys,y=sums)],output_type="div")
    mplot_display = plot([go.Bar(x=citys, y=males)], output_type="div")
    fplot_display = plot([go.Bar(x=citys, y=females)], output_type="div")

    return render(request,"readcsv_plotly.html",locals())

def account_create(request):
    recaptcha_response=""
    nac = ""
    npa = ""
    nch = ""
    emails=""
    echeck = ""
    ac_search=""
    rePass=False
    acPass = False
    paPass = False
    chPass = False
    ePass = False
    tryIn = False
    allPass = False
    ask=""

    try:
        ask=request.POST.get("logIn")

    except:
        pass

    if ask=="創建":
        tryIn=True

    try:
        recaptcha_response=request.POST.get('g-recaptcha-response')

    except:
        pass



    url="https://www.google.com/recaptcha/api/siteverify"
    values={
        'secret':settings.GOOGLE_RECAPTCHA_SECRET_KEY,
        'response':recaptcha_response
    }


    data=urllib.parse.urlencode(values).encode()
    req=urllib.request.Request(url,data=data)
    response=urllib.request.urlopen(req)
    result=json.loads(response.read().decode())

    if result['success']==True:
        rePass = True




    try:
        nac=request.POST["new-account"]
    except:
        pass

    if nac!="" and len(nac)>5:

        try:
            ac_search=Users.objects.get(User_account=nac)
            acPass=False
        except:
            acPass=True

    try:
        npa=request.POST["new-password"]
    except:
        pass

    if npa != "" and len(npa)>5:
        paPass = True

    try:
        nch=request.POST["check-password"]
    except:
        pass

    if nch != "" and nch==npa:
        chPass = True

    try:
        emails=request.POST["e-mail"]
    except:
        pass

    if emails!="":
        try:
            echeck=Email.objects.get(email=emails)
            ePass=False
        except:
            ePass=True


    if ePass and rePass and chPass and paPass and acPass:
        allPass=True
        eSave=Email(email=emails)
        eSave.save()

    if allPass:
        nemail=Email.objects.get(email=emails)
        allSave=Users(User_account=nac,User_password=npa,email=nemail)
        allSave.save()

        ori_email=settings.EMAIL_HOST_USER
        body="註冊成功 歡迎使用會員功能"
        message=u'''{}'''.format(body)

        email=EmailMessage('二手手機商店-創建帳號',
                           message,
                           ori_email,
                           [emails])

        email.send()

    return render(request,"account_create.html",locals())




def cart(request):
    owner = None
    logIn = None
    login=False

    try:
        owner=request.session["account"]
        logIn=request.session["logIn"]
    except:
        owner=None
        logIn=None


    if owner==None or logIn==None:
        return redirect("/phone/")

    if owner!=None and logIn!=None:
        login=True

    if login:
        ca=phone_cart.objects.filter(User_account=owner)
        products=Phone_Product2.objects.all()

    return render(request,"phone_cart.html",locals())


def cart_add(request,id):
    login = False

    try:
        owner = request.session["account"]
        logIn = request.session["logIn"]
    except:
        owner = None
        logIn = None

    if owner!=None and logIn!=None:
        login=True

    if owner == None or logIn == None:
        return redirect("/phone/")

    if login:
        try:
            add=Phone_Product2.objects.get(id=id)

        except:
            add=None

        try:
            already=phone_cart.objects.get(User_account=owner,pid=id)

        except:
            already=None

        if add!=None and already==None:
            add_item=phone_cart(User_account=owner,pid=id)
            add_item.save()

    return redirect("/phone/")

def cart_del(request,id):
    login = False

    try:
        owner = request.session["account"]
        logIn = request.session["logIn"]
    except:
        owner = None
        logIn = None

    if owner != None and logIn != None:
        login = True

    if owner==None or logIn==None:
        return redirect("/phone/")

    if login:
        try:
            dele = phone_cart.objects.get(User_account=owner,pid=id)
            dele.delete()
        except:
            pass

    return redirect("/phone/cart/")

def deliver(request):
    login = False

    try:
        owner = request.session["account"]
        logIn = request.session["logIn"]
    except:
        owner = None
        logIn = None

    if owner != None and logIn != None:
        login = True

    if owner==None or logIn==None:
        return redirect("/phone/")

    if login:
        try:
            ca=phone_cart.objects.filter(User_account=owner)
            lst = list()
            plst=   list()
            idlst= list()
            for c in ca:
                try:
                    item = request.POST[str(c.pid)]
                    lst.append(int(item))
                    pa = Phone_Product2.objects.get(id=c.pid)
                    plst.append(pa.Model.Model)
                    idlst.append(c.pid)
                    request.session["quantity"] = lst
                    request.session["produt"]=plst
                    request.session["pid"] = idlst
                except:
                    request.session["quantity"] = None
                    request.session["produt"] = None
                    request.session["pid"] = None

        except:
            ca=False


    return render(request,"phone_deliver.html",locals())


def shopped_add(request):
    login = False
    address = None
    phone_number = None
    pq_si=False

    try:
        owner = request.session["account"]
        logIn = request.session["logIn"]
    except:
        owner = None
        logIn = None

    if owner != None and logIn != None:
        login = True

    if owner==None or logIn==None:
        return redirect("/phone/deliver/")

    try:
        send = request.POST["send"]
    except:
        send = None

    if login and send=="送出訂單":
        plst=request.session["produt"]
        lst=request.session["quantity"]
        idlst=request.session["pid"]


        try:
            address=request.POST["address"]
            phone_number=request.POST["phone_number"]

        except:
            address = None
            phone_number = None
            return redirect("/phone/deliver/")

        print(address)
        print(phone_number)

        if address!=None and phone_number!=None:

            for i in range(len(lst)):
                product=Phone_Product2.objects.get(id=idlst[i])
                if product.Quantity >= lst[i]:
                    pq_si = True
                else:
                    pq_si = False

                    break

            if pq_si == False:
                return redirect("/phone/cart/")

            if pq_si==True:

                for i in range(len(lst)):
                    product = Phone_Product2.objects.get(id=idlst[i])
                    product.Quantity=product.Quantity-lst[i]
                    product.save()
                    shopped=phone_shopped2(User_account=owner,pid=idlst[i],quantity=lst[i],address=address,phone_number=phone_number,paid="No")
                    shopped.save()
                    carts=phone_cart.objects.get(User_account=owner,pid=idlst[i])
                    carts.delete()


    return redirect("/phone/shopped_list/")


def shopped_list(request):
    login = False
    pay = None
    try:
        owner = request.session["account"]
        logIn = request.session["logIn"]
    except:
        owner = None
        logIn = None

    if owner!=None and logIn!=None:
        login=True

    else:
        return redirect("/phone/")

    shopped_item= phone_shopped2.objects.filter(User_account=owner)
    products=Phone_Product2.objects.all()

    total=0
    sp_lst=list()

    for sp in shopped_item:
        if sp.paid=="No":
            p=Phone_Product2.objects.get(id=sp.pid)
            total+=p.Price*sp.quantity
            sp_lst.append(p.Model.Model)

    if total>0:
        host=request.get_host()
        try:

            paypal_dict={
                "business":settings.PAYPAL_RECEIVER_EMAIL,
                "amount":total,
                "item_name":"{}".format(sp_lst),
                "invoice":"invoice-{}".format(owner),
                "currency_code":"TWD",
                "notify_url":"http://{}{}".format(host,reverse('paypal-ipn')),
                "return_url":"http://{}/done/".format(host),
                "cancel_return":"http//{}/canceled/".format(host),
            }



            paypal_form=PayPalPaymentsForm(initial=paypal_dict)

        except:
            pass

    return render(request,"phone_shopped.html",locals())


def payment_done(request):
    login = False
    pay = None
    try:
        owner = request.session["account"]
        logIn = request.session["logIn"]
    except:
        owner = None
        logIn = None

    if owner!=None and logIn!=None:
        login=True

    else:
        return redirect("/phone/")

    """""""""""""""""""""
    try:
        pay=phone_shopped2.objects.filter(User_account=owner,paid="No")
        for p in pay:
            p.paid="Yes"
            p.save()
    except:
        return redirect("/phone/shopped_list/")
    """""""""""""""""""""""""""""
    return render(request,"payment_done.html")
