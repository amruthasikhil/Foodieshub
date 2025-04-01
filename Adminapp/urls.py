from django.urls import path
from Adminapp import views


urlpatterns=[
    path('adminindex/',views.Adminindex,name='adminindex'),
     path('dashboard/',views.dashboard,name='dashboard'),
    path('login/',views.Loginpage,name='login'),
    path('Loginpagesubmit/',views.Loginpagesubmit,name='loginaction'),
    path('logout/',views.Adminlogout,name='logout'),

    path('add_product/',views.Addproduct,name="addproduct"),
    path('addproductspost/',views.Addproductspost,name="addproductpost"),
    path('Viewproducts/',views.Viewproducts,name="viewproducts"),
    path('deleteproduct/<int:prdtid>',views.Deleteproduct,name="deleteproduct"),
    path('editproduct/<int:prdtid>',views.Editproduct,name="editproduct"),
    path('updateproduct/<int:prdtid>',views.Updateproduct,name="updateproduct"),


    path('addcategory/',views.AddCategory,name="addcategory"),
    path('viewcategory/',views.ViewCategory,name="viewcategory"),
    path('categorypost/',views.Addcategorypost,name='categorypost'),
    path('deletecategory/<int:catid>',views.DeleteCategory,name='deletecategory'),
    path('editcategory/<int:catid>',views.EditCategory,name='editcategory'),
    path('updatecategory/<int:catid>',views.UpdateCategory,name='updatecategory'),

    path('viewcontact/',views.Contactdetails,name="viewcontact"),
    path('contactdelete/<int:coid>',views.Deletecontactdetails,name="contactdelete"),

    path('addservices/',views.Addservices,name="addservices"),
    path('viewservices/',views.Viewservices,name="viewservices"),
    path('addservicespost/',views.Addservicespost,name='addservicespost'),
    path('deleteservices/<int:sid>',views.Deleteservices,name='deleteservices'),
        path('editservices/<int:sid>',views.Editservices,name='editservices'),
                path('updateservices/<int:sid>',views.Updateservices,name='updateservices'),

    






    

]