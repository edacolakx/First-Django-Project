from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect,HttpResponseNotFound
from django.urls import reverse
data={
    "mobil":"flutter react native",
    "web":"react html css",
    "backend":"django nodejs"
}

def numara(req):
    return HttpResponse('05064062114')
def isim(req):
    return HttpResponse('eda çolak')
    
def bos(req,category):
    try:
        category_text=data[category]
        return render(req,'index.html',{
            'data':category_text
        })
    except:
        return HttpResponseNotFound('bulunamadı')

def bos1(req, category1):
    try:
        category_index = int(category1) - 1
        category_list = list(data.keys())
        if 0 <= category_index < len(category_list):
            redirect_text = category_list[category_index]
            redirected_url = reverse("courses_by_category", args=[redirect_text])
            return HttpResponseRedirect(redirected_url)
        else:
            return HttpResponseNotFound('Bulunamadı')
    except ValueError:
        return HttpResponseNotFound('Geçersiz istek')


def index(request):
    return render(request,'indexa.html')