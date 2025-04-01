from django.urls import path
from Webapp import views

urlpatterns=[
    path('home/',views.Homepage,name='homepage'),
    path('feedbackform/',views.feedbackform,name='feedbackform'),
    path('feedbackformpost/',views.feedbackformpost,name='feedbackformpost'),
    path('Changepassword/',views.Changepassword,name='changepassword'),

    path('about/',views.Aboutpage,name='about'),
    path('contactuser/',views.Contactpage,name='contactuser'),
     path('chef/',views.Chefpage,name='chef'),
    path('servicesuserview/',views.Servicepageuser,name='servicesuserview'),
     path('contactpost/',views.Contactpagepost,name='contactpost'),
    path('categoryfilter/<catname>',views.Filteredcategory,name='categoryfilter'),
    path('foodmenu/',views.Foodmenu,name='foodmenu'),
    path('foodmenusearch/',views.Foodmenusearch,name='foodmenusearch'),

    path('filterhome/<catname>',views.Filteredcategory_home,name='filterhome'),
    path('productmore/<int:pid>',views.Singlepage,name='productmore'),
   
   path('userregistration/',views.Userregistration,name='userreg'),
   path('userregistrationpost/',views.Userregistrationpost,name='userregistrationpost'),

   path('',views.Userlogin,name='webuserlogin'),
   path('webuserlogout/',views.Userlogout,name='webuserlogout'),
   path('webuserloginpost/',views.Userloginpost,name='webuserloginpost'),
    path('addtocart/',views.Addtocart,name="addtocart"),
     path('cartpage/',views.Cartpage,name="cartpage"),
      path('cartpagedelete/<int:cartid>',views.Removecart,name="cartpagedelete"),
      path('checkout/',views.Checkoutpage,name="checkout"),
      path('checkoutpost/',views.Checkoutpost,name="checkoutpost"),
   path('paymentnavigation/',views.paymentnavigation,name='paymentnavigation'),

]