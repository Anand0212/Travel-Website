"""
URL configuration for travelpage project.

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
from django.urls import path
from travelapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index),
    path('events/', views.events),
    path('register/', views.register),
    path('about/', views.about),
    path('ulogout/', views.ulogout),
    path('about/', views.about),
    path('contact/', views.contact),
    # for try purpose:
    path('indextry/', views.indextry),
    path('indextry1/', views.indextry1),
    # try purpose ends
    path('catfilter/<n>/', views.catfilter),
    path('locfilter/<sid>/', views.locfilter),
    path('sortby/<oid>/', views.sortby),
    path('edetails/<eid>/', views.edetails),
    #path('enroll/<eid>', views.enroll),
    path('ilogin/', views.ilogin),
    path('confirm/', views.confirm),
    path('eenroll/<eid>/', views.eenroll),
    path('updateqty/<x>/<cid>/', views.updateqty),
    path('remove/<cid>', views.remove),

] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
