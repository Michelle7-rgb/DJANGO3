# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect
from datetime import datetime, date
# importer les formulaires ici
# importer les modeles


def getLoggedUserFromRequest(request):
    if 'logged_user_id' in request.session:
        loged_user_id = request.session['logged_user_id']
        #if len(user.objects.filter(id=logged_user_id)) == 1
        #return user.objects.get(id=logged_user_id)

    else :
        return None 