from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth.models import User
from Adminapp.models import CategoryDb,ProductDb,ServicesDb
from django.contrib.auth import authenticate,login
from django.utils.datastructures import MultiValueDictKeyError
from django.core.files.storage import FileSystemStorage
from Webapp.models import ContactDb
from django.contrib import messages

#********************************* loading index page ****************

def Adminindex(request):
    return render(request,"admin_index.html")


#********************************* loading login page ****************

def Loginpage(request):
    return render(request,"login.html")

def dashboard(request):
    totalcategorycount=CategoryDb.objects.count()
    totalproductcount=ProductDb.objects.count()
    return render(request,"dashboard.html",{"totalcategorycount":totalcategorycount,"totalproductcount":totalproductcount})

def Loginpagesubmit(request):
    if request.method == "POST":
        un=request.POST.get('username')
        pswd=request.POST.get("password")
        if User.objects.filter(username__contains=un).exists():
            user=authenticate(username=un,password=pswd)
            if user is not None:
                request.session['username']=un
                request.session['password']=pswd
                login(request,user)
                return redirect(dashboard)
            else:
                return redirect(Loginpage)
        else:
            return redirect(Loginpage)
        
def Adminlogout(request):
    del request.session['username']
    del request.session['password']
    return redirect(Loginpage)
        
#category operations =========================================================================================

def AddCategory(request):
    return render(request,"add_category.html")


def Addcategorypost(request):
    if request.method == "POST":
        categoryname=request.POST.get("name")
        descriptions=request.POST.get("description")
        categoryimage=request.FILES["imgg"]
        obj=CategoryDb(categoryname=categoryname,description=descriptions,category_image=categoryimage)
        obj.save()
        messages.success(request,"Category added")
        return redirect(AddCategory)

def ViewCategory(request):
    data=CategoryDb.objects.all()
    return render(request,"view_category.html",{"data":data})

def DeleteCategory(request,catid):
    delobj=CategoryDb.objects.filter(id=catid)
    delobj.delete()
    messages.error(request,"Category deleted...")
    return redirect (ViewCategory)

def EditCategory(request,catid):
    data=CategoryDb.objects.get(id=catid)
    return render(request,"edit_category.html",{"data":data})

def UpdateCategory(request,catid):
    if request.method == "POST":
        categoryname=request.POST.get("name")
        descriptions=request.POST.get("description")
    try:
        categoryimage=request.FILES["imgg"]
        fs=FileSystemStorage()
        file=fs.save(categoryimage.name,categoryimage)
    except MultiValueDictKeyError:
        file=CategoryDb.objects.get(id=catid).category_image
    CategoryDb.objects.filter(id=catid).update(categoryname=categoryname,description=descriptions,category_image=file)
    messages.warning(request,"Category updated")
    return redirect (ViewCategory)

    #===========================================================================================================================





#product operations =========================================================================================


def Addproduct(request):
    data=CategoryDb.objects.all()
    return render(request,"add_product.html",{"data":data})

def Addproductspost(request):
    category=request.POST.get("category")
    products=request.POST.get("name")
    description=request.POST.get("description")
    price=request.POST.get("price")
    pic=request.FILES["imgg"]
    productobj=ProductDb(categoryname=category,product_name=products,description=description,price=price,product_image=pic)
    productobj.save()
    messages.success(request,"product added")
    return redirect(Addproduct)



def Viewproducts(request):
    data=ProductDb.objects.all()
    return render(request,"view_product.html",{'data':data})

def Deleteproduct(request,prdtid):
    prdtobj=ProductDb.objects.filter(id=prdtid)
    prdtobj.delete()
    messages.error(request,"Product deleted")

    return redirect(Viewproducts)

def Editproduct(request,prdtid):
    data=ProductDb.objects.get(id=prdtid)
    catdata=CategoryDb.objects.all()
    return render(request,"edit_product.html",{'data':data,'catdata':catdata})
    

def Updateproduct(request,prdtid):
    if request.method == "POST":
        category=request.POST.get("category")
        products=request.POST.get("name")
        description=request.POST.get("description")
        price=request.POST.get("price")
        try:

            pic=request.FILES["imgg"]
            fs=FileSystemStorage()
            file=fs.save(pic.name,pic)
        except MultiValueDictKeyError:
            file= ProductDb.objects.get(id=prdtid).product_image
        ProductDb.objects.filter(id=prdtid).update(categoryname=category,product_name=products,description=description,price=price,product_image=file)
        messages.warning(request,"Product updated")
        return redirect(Viewproducts)  
    


def Contactdetails(request):
    data=ContactDb.objects.all()
    return render(request,"Contact.html",{'data':data})

def Deletecontactdetails(request,coid):
    delobj=ContactDb.objects.filter(id=coid)
    delobj.delete()
    messages.error(request,"Contact deleted")
    return redirect (Contactdetails)




def Addservices(request):
    return render(request,"add_services.html")


def Viewservices(request):
    data=ServicesDb.objects.all()
    return render(request,"view_services.html",{'data':data})


def Addservicespost(request):
    if request.method == "POST":
        name=request.POST.get("name")
        descriptions=request.POST.get("description")
        imgg=request.FILES["imgg"]
        obj=ServicesDb(servicename=name,description=descriptions,service_image=imgg)
        obj.save()
        messages.success(request,"Service added")
        return redirect(Addservices)
    
def Deleteservices(request,sid):
    prdtobj=ServicesDb.objects.filter(id=sid)
    prdtobj.delete()
    messages.error(request,"Service deleted")
    return redirect(Viewservices)


def Editservices(request,sid):
    data=ServicesDb.objects.get(id=sid)
    return render(request,"edit_services.html",{"data":data})

def Updateservices(request,sid):
    if request.method == "POST":
        name=request.POST.get("name")
        descriptions=request.POST.get("description")
    try:
        imgg=request.FILES["imgg"]
        fs=FileSystemStorage()
        file=fs.save(imgg.name,imgg)
    except MultiValueDictKeyError:
        file=ServicesDb.objects.get(id=sid).service_image
    ServicesDb.objects.filter(id=sid).update(servicename=name,description=descriptions,service_image=file)
    messages.warning(request,"Services updated")
    return redirect (Viewservices)



# def Userlogin(request):
#     data=ContactDb.objects.all()
#     return render(request,"Contact.html")


