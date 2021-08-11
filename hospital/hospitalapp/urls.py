from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import homepage,userauthenticate,loginuser,result,prediction,signupuser,doctormodel,logout,pharmacymodel,labmodel,mainhomepage

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', mainhomepage,),
    path('homepage', homepage, name='homepage'),
    path('loginuser/', loginuser,name='userlogin'),
    path('signupuser/',signupuser,name="signupuser"),
    path('logout/',logout),
    path('user/authenticate/',userauthenticate),
    path('doctor/',doctormodel),
    path('pharmacy/',pharmacymodel),
    path('lab/',labmodel),
    path('prediction/',prediction, name="prediction"),
    path('result/',result, name="result"),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)