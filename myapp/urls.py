from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('',views.index,name='index'),
    path('home/',views.home,name='home'),
    path('about-us/',views.aboutus,name='about-us'),
    path('manu-cap/',views.manu_cap,name='manu-cap'),
    path('career/',views.career,name='career'),
    path('contact/',views.contact,name='contact')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)