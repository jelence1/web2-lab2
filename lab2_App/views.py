from django.shortcuts import redirect, render, redirect
from . import models
from django.db import *

# Create your views here.

ENABLE_CSRF = False

def index(request):

    rows = {}
    name = {}
    error = ""
    columns = {}

    if request.method == "POST":
        enable = request.POST["enable"]
        
        if enable == "yes":
            sql = request.POST["sql"]
            sql = '''SELECT name FROM public."lab2_App_teams" WHERE nickname = '{}' '''.format(sql)
            with connection.cursor() as cursor:
                try:
                    cursor.execute(sql)
                    columns = [col[0] for col in cursor.description]
                    rows = [dict(zip(columns, row)) for row in cursor.fetchall()]
                except ProgrammingError as e:
                    error = "There was an error."
                    print(e)
                except DataError as e:
                    error = "There was an error."
                    print(e)


        elif enable == "no":
            try:
                post_nick = request.POST["sql"]
                name = models.Teams.objects.filter(nickname=post_nick)
            except ProgrammingError:
                error = "There was an error."
            except ValueError:
                error = "There was an error."

    return render(request, "index.html", context = {"name" : name, "error" : error, "columns" : columns, "rows": rows})

def csrf_yes_no(request):
    global ENABLE_CSRF

    if request.method == "POST":
        enable = request.POST["enable"]
        if enable == "yes":
            ENABLE_CSRF = True
        else:
            ENABLE_CSRF = False

        return redirect("/csrf")

    return render(request, "csrf_yes_no.html")

def csrf(request):
    global ENABLE_CSRF

    admin = models.Users.objects.get(pk=1) #admin password
    return render(request, "csrf.html", context = {"password" : admin.password, "csrf_enabled" : ENABLE_CSRF })

def change_password(request):
    global ENABLE_CSRF

    if ENABLE_CSRF == True: 
        new_password = request.GET["password"]
        redirect_url = ""

        models.Users.objects.filter(id=1).update(password=new_password)

    elif ENABLE_CSRF == False:
        if request.method == "POST":
            new_password = request.POST["password"]
            models.Users.objects.filter(id=1).update(password=new_password)

    if "redirect_url" in request.GET:
            redirect_url = request.GET["redirect_url"]

    if redirect_url != "":
            return redirect(redirect_url)

    return redirect("/csrf")
