from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.shop, name="shop"),
    path('signup/', views.signup, name="signup"),
    path('pincode/', views.pincode, name="pincode"),
    path('customersignup', views.customersignup, name="customersignup"),
    path('vendorsignup', views.vendorsignup, name="vendorsignup"),
    path('handlelogin', views.handlelogin, name="handlelogin"),
    path('handlelogout', views.handlelogout, name="handlelogout"),
    path('about/', views.about, name="about"),
    path('update_catalogue', views.update_catalogue, name="update_catalogue"),
    path('ven_to_cata/', views.ven_to_cata, name="ven_to_cata"),
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)