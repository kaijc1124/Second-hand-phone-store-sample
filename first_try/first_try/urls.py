"""
URL configuration for first_try project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from mysite.views import about
from mysite.views import blog_list
from mysite.views import blog_detail
from mysite.views import homepage
from mysite.views import youtube
from mysite.views import phone
from mysite.views import cart
from mysite.views import deliver
from mysite.views import shopped_list
from mysite.views import cart_add
from mysite.views import phone_create
from mysite.views import shopped_add
from mysite.views import payment_done
from mysite.views import baby
#from mysite.views import payment
from mysite.views import account_create
from mysite.views import cart_del
from django.conf import settings
from django.conf.urls.static import static

#from mysite.views import phone_user

urlpatterns = [
    path("admin/", admin.site.urls),
    path("paypal/", include("paypal.standard.ipn.urls")),
    #path("payment/", payment),
    path("phone/accounts/",include('registration.backends.default.urls')),
    path("self/",about),
    path("done/",payment_done),
    path('filer/',include('filer.urls')),
    path("phone/cart/",cart),
    path("phone/cart/<int:id>/",cart_add),
    path("phone/cart/del/<int:id>/",cart_del),
    path("account_create/",account_create),
    path("blog_list/",blog_list),
    path('phone/',phone),
    path('phone/shopped_list/',shopped_list),
    path('phone/shopped_add/',shopped_add),
    path('phone/deliver/',deliver),
    path('phone/create/',phone_create),
    path('phone/account_create/',account_create),
    path('newborn111/',baby),
    path('accounts/',include('allauth.urls')),
    #path('phone/user/',phone_user),
    #path("captcha/",include("captcha.urls")),
    path('<str:tl>/',blog_detail),
    path('youtube/<int:tvc>/',youtube),
    path('',homepage),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

