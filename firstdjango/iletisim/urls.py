from . import views
from django.urls import path
urlpatterns = [
    path('',views.index),
    path('numara' ,views.numara ),
    path('isim' ,views.isim ),
    path('<int:category1>',views.bos1),
    path('kategori/<str:category>',views.bos,name='courses_by_category'),
]
