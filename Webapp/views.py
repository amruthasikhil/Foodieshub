from django.shortcuts import render,redirect
from Adminapp.models import CategoryDb,ProductDb,ServicesDb
from Webapp.models import ContactDb,RegistrationDb,CartDb,OrderDb,FeedbackDb
from django.contrib import messages
import razorpay


def Homepage(request):
    data=CategoryDb.objects.all()
    productdata=ProductDb.objects.all()[:4]
    popdata=ProductDb.objects.all().order_by('-id')[:3][::-1]
    servicedata=ServicesDb.objects.all()[:4]
    user_id=request.session['userid']
    countofcart=CartDb.objects.filter(username=user_id)
    tot_cartcount=countofcart.count()
    print("************************************************************************************************",tot_cartcount)
    return render(request,"Home.html",{"data":data,"popdata":popdata,"productdata":productdata,"servicedata":servicedata,"tot_cartcount":tot_cartcount})


def Aboutpage(request):
    data=CategoryDb.objects.all()
    fdata=FeedbackDb.objects.all()
    lid=request.session['userid']
    countofcart=CartDb.objects.filter(username=lid)
    tot_cartcount=countofcart.count()
    return render(request,"about.html",{"data":data,"feedbacks":fdata,"tot_cartcount":tot_cartcount})

def feedbackform(request):
    lid=request.session['userid']
    countofcart=CartDb.objects.filter(username=lid)
    tot_cartcount=countofcart.count()
    return render(request,"feedback.html",{"tot_cartcount":tot_cartcount})

def feedbackformpost(request):
    if request.method == "POST":
        uid=request.session['userid']
        obj=RegistrationDb.objects.get(id=uid)
        name=obj.name
        feedback = request.POST.get("message")
        val=FeedbackDb(username=name,Message=feedback)
        val.save()
        return redirect(Homepage)

    return render(request,"feedback.html")

def Servicepageuser(request):
    servicedata=ServicesDb.objects.all()
    data=CategoryDb.objects.all()
    lid=request.session['userid']
    countofcart=CartDb.objects.filter(username=lid)
    tot_cartcount=countofcart.count()
    return render(request,"services.html",{"servicedata":servicedata,"tot_cartcount":tot_cartcount})

def Foodmenu(request):
    data=CategoryDb.objects.all()
    productdata=ProductDb.objects.all()
    lid=request.session['userid']
    countofcart=CartDb.objects.filter(username=lid)
    tot_cartcount=countofcart.count()
    return render(request,"food_menu.html",{"data":data,"productdata":productdata,"tot_cartcount":tot_cartcount})

def Foodmenusearch(request):
    if request.method == "POST":
        data=CategoryDb.objects.all()
        search_text=request.POST.get("search")
        qs=ProductDb.objects.filter(product_name__contains=search_text)
        return render(request,"food_menu.html",{"data":data,"productdata":qs})



def Categorloadingypage(request):
    data=CategoryDb.objects.all()
    return render(request,"Home.html",{"data":data,"data":data})

def Changepassword(request):
    return render(request,"change_password.html")


def Filteredcategory(request,catname):
    productdata=ProductDb.objects.filter(categoryname=catname)
    print("okkk")
    data=CategoryDb.objects.all()
    return render(request,"food_menu.html",{"data":data,"productdata":productdata})

def Filteredcategory_home(request,catname):
    productdata=ProductDb.objects.filter(categoryname=catname)[:4]
    print("ok=================================kk")
    data=CategoryDb.objects.all()
    return render(request,"home.html",{"data":data,"productdata":productdata})

def Contactpage(request):
    data=CategoryDb.objects.all()
    lid=request.session['userid']
    countofcart=CartDb.objects.filter(username=lid)
    tot_cartcount=countofcart.count()
    return render(request,"usercontact.html",{"data":data,"tot_cartcount":tot_cartcount})




def Chefpage(request):
    data=CategoryDb.objects.all()
    lid=request.session['userid']
    countofcart=CartDb.objects.filter(username=lid)
    tot_cartcount=countofcart.count()
    return render(request,"chefs.html",{"data":data,"tot_cartcount":tot_cartcount})

def Contactpagepost(request):
    if request.method == "POST":
        name=request.POST.get("name")
        email=request.POST.get("email")
        subject=request.POST.get("subject")
        message=request.POST.get("message")
        print("**************************************************************")
        obj=ContactDb(name=name,email=email,subject=subject,message=message)
        obj.save()
    return redirect (Contactpage)

def Singlepage(request,pid):
    data=CategoryDb.objects.all()
    productmore=ProductDb.objects.get(id=pid)
    return render(request,"singleitempage.html",{"data":data,"productmore":productmore})

def Addtocart(request):
    if request.method == "POST":
        productname = request.POST.get("pname")
        userid = request.POST.get("userid")
        qty = request.POST.get("qty")
        totalprice = request.POST.get("totalprice")
        try:
            pimg=ProductDb.objects.get(product_name=productname)
            p_img=pimg.product_image
        except ProductDb.DoesNotExist:
            p_img=None
        obj=CartDb(username=userid,productname=productname,quantity=qty,totalprice=totalprice,pimg=p_img)
        obj.save()
        return redirect(Foodmenu)
    
def Cartpage(request):
    subtotal=0
    data=CategoryDb.objects.all()
    uid=request.session['userid']
    obj=CartDb.objects.filter(username=uid)
    productitems_incart=[]
    for i in obj:
        productname= i.productname
        print(productname,"88888888888888888888")
        subtotal= subtotal+i.totalprice

        try:
            pobj=ProductDb.objects.get(product_name=productname)
            price=pobj.price
            print("/////////////////////////////////6//////////////////",price)
            productitems_incart.append({
                "username":uid,
                "productname":i.productname,
                "quantity":i.quantity,
                "totalprice":i.totalprice,
                "pimg":i.pimg,
                "price":pobj.price,
                "id":i.id
            })
        except ProductDb.DoesNotExist:
             productitems_incart.append({
                "username":uid,
                "productname":i.productname,
                "quantity":i.quantity,
                "totalprice":i.totalprice,
                "pimg":i.pimg,
                "price":"none",
                "id":i.id
            })
    print("666666666666666666666666666666666666666666",subtotal)
    if subtotal>500:
        delivery_charge = 50
    else:
        delivery_charge = 100
    final_total=subtotal+delivery_charge
    request.session['subtotal']=final_total
    request.session['delivery_charge']=delivery_charge
    productdata=ProductDb.objects.all()[:4]
    return render(request,"cartpage.html",{"productdata":productdata,"cdata":data,"data":productitems_incart,"subtotal":subtotal,"delivery_charge":delivery_charge,"final_total":final_total})

def Removecart(request,cartid):
    obj=CartDb.objects.get(id=cartid)
    obj.delete()
    return redirect(Cartpage)

def Checkoutpage(request):
    subtotal=request.session['subtotal']
    delivery_charge=request.session['delivery_charge']
    return render(request,"checkoutpage.html",{"subtotal":subtotal,"delivery_charge":delivery_charge})

def paymentnavigation(request):
    uid=request.session['userid']
    obj=OrderDb.objects.get(Name=uid)
    customername_ob=RegistrationDb.objects.get(id=uid)
    customer=customername_ob.name
    totalamount=obj.TotalPrice
    #convert amount into paisa
    amoount=int(totalamount*100)

    amount_str=str(amoount)

    if request.method == "POST":
        order_currency = 'INR'
        client =razorpay.Client(auth=('rzp_test_MMwua6oGM7f6Bi','FYZEoZkAuia58N8GlRTUGAkE'))
        payment=client.order.create({'amount':amoount,'currency': order_currency})
    return render(request,"paymentnavigationpage.html",{'amount_str':amount_str,"customer":customer})


def Checkoutpost(request):
    if request.method == "POST":
        name=request.session['userid']
        email=request.POST.get("email")
        place=request.POST.get("place")
        address=request.POST.get("address")
        pincode=request.POST.get("pincode")
        mobile=request.POST.get("mobileno")
        message=request.POST.get("message")
        totalprice=request.POST.get("subtotal")
        obj=OrderDb(Name=name,Email=email,Place=place,Address=address,Mobile=mobile,Pin=pincode,TotalPrice=totalprice,Message=message)
        obj.save()
        return redirect(paymentnavigation)




def Userregistration(request):
    return render(request,"register.html")

def Userregistrationpost(request):
    print("--------------------------------")
    if request.method == "POST":
        print("0000000")
        name= request.POST.get("name")
        email= request.POST.get("email")
        pwd= request.POST.get("pwd")
        repwd= request.POST.get("re_pwd")
        print("========================================")
        obj=RegistrationDb(name=name,email=email,password=pwd,confirm_password=repwd)
        obj.save()
        return redirect(Userlogin)

def Userlogin(request):
    return render(request,"webuserlogin.html")

def Userloginpost(request):
    if request.method == "POST":
        username=request.POST.get("your_name")
        password=request.POST.get("your_pass")
        if RegistrationDb.objects.filter(name=username,password=password).exists():
            user=RegistrationDb.objects.get(name=username,password=password)
            request.session['name'] = username
            request.session['pwd']=password
            request.session['userid']=user.id
            return redirect(Homepage)
        else:
            messages.error(request,"Invalid details")
            return redirect(Userlogin)
    else:
        messages.error(request,"Invalid details")
        return redirect(Userlogin)


def Userlogout(request):
    del request.session['name']
    del request.session['pwd']
    return render(request,"webuserlogin.html")

# Create your views here.
