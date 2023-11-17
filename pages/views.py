from django.shortcuts import render
from django.http import HttpResponse


def homePageView(request):
    return HttpResponse("Hello, world!")


def aboutPageView(request):
    return HttpResponse("About")


def contactPageView(requeest):
    return HttpResponse("Contact")
