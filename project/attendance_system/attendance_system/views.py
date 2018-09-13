import MySQLdb
from django.http import HttpResponse
from django.shortcuts import redirect,render
    
def homepageview(request,errors=None):
    return render(request,'HomePage.html',{'errors':errors})