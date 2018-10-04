import MySQLdb
from django.http import HttpResponse
from django.shortcuts import redirect,render
from django import template
def homepageview(request,errors=None):
    return render(request,'HomePage.html',{'errors':errors})
    
