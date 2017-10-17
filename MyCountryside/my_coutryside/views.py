# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import django.contrib.auth
from django.http import HttpResponse
from django.shortcuts import render, render_to_response
from .models import User


def home(request):

    return render(request, 'registration/login.html', {})


def login(request):

    user_name = request.POST['user_name']
    password = request.POST['pwd']

    user = User.objects.get(user_name=user_name)

    if user.user_password == password:
        c_value = request.COOKIES.get(user_name)
        if c_value:
            # print "**********" + request.get_signed_cookie(user_name)
            return render_to_response('login.html', {"user": "cookie user:%s" %user_name})

        else:

            response = render_to_response('login.html', {"user":user_name})

            response.set_cookie(user_name, user_name)

            return response

    else:
        return HttpResponse("Your username and password didn't match.")

