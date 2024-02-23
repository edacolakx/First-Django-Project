from . import views
from django.urls import path

urlpatterns = [
    path('',views.anasayfa)   , 
    path('iletisim',views.iletisim) ,   
    path('kurslar',views.kurslar),
    path('kategori/<int:category>',views.redirected)  ,  
    path('kategori/<str:category>',views.abc,name='red')    
]
