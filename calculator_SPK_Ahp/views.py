from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("Halo, ini halaman utama dari aplikasi!")

def about(request):
    return HttpResponse("Tess")

def spk_ahp(request):
    return HttpResponse("SPK AHP")