from datetime import datetime,date
from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect

veri={
    'web':'html css',
    'mobil':'react native flutter',
    'backend':'django nodejs'
}

db={
    "courses":[
        {
            "title":"javascript kursu",
            "description":"javascript kursu açıklaması",
            "imageUrl":"a.jpg",
            "slug":"javascript kursu bu bi url",
            "date":date(2022,5,14),
            "isactive":True,
            "isUpdated":True
        },
        {
            "title":"python kursu",
            "description":"python kursu açıklaması",
            "imageUrl":"b.png",
            "slug":"python kursu bu bi url",
            "date":date(2023,4,5),
            "isactive":True,
            "isUpdated":True
        },
        {
            "title":"react native kursu",
            "description":"react native kursu açıklaması",
            "imageUrl":"c.jpg",
            "slug":"react native kursu bu bi url",
            "date":datetime.now(),
            "isactive":True,
            "isUpdated":True
        },
        {
            "title":"flutter kursu",
            "description":"flutter kursu açıklaması",
            "imageUrl":"d.png",
            "slug":"flutter kursu bu bi url",
            "date":date(2022,3,5),
            "isactive":True,
            "isUpdated":True
        },
    ],
    "categories":[
        {"name":"programlama","id":1,"slug":"programlama"},
        {"name":"web","id":2,"slug":"web-gelistirme"},
        {"name":"mobil","id":3,"slug":"mobil"},
        ]
}

def anasayfa(request):
    return render(request,'anasayfa.html')

def kurslar(request):
    kurslar=db["courses"]
    kategoriler=db["categories"]
    return render(request,'kurslar.html',{
        "categories":kategoriler,
        "courses":kurslar
    })

def iletisim(request):
    return render(request,'iletisim.html')

def redirected(request,category):
    
    text=list(veri.keys())
    redtext=text[category-1]
    redirectedurl=reverse('red',args=[redtext])
    return HttpResponseRedirect(redirectedurl)


def abc(request,category):
    kurslar=db["courses"]
    kategoriler=db["categories"]
    return render(request,'index.html',{
        "categories":kategoriler,
        "courses":kurslar
    })

