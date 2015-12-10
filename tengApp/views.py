from django.shortcuts import render


def home(req):
    return render(req, 'tengApp/home.html')


def business_group(req):
    return render(req, 'tengApp/business_group.html')


def about(req):
    return render(req, 'tengApp/about.html')


def project(req):
    return render(req, 'tengApp/project.html')

