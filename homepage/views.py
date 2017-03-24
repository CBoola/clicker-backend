from django.shortcuts import render, redirect
from api.models import Player


def main_page(request):
    if Player.is_user_logged(request.user):
        return redirect("/game")

    return render(request, 'main_page.html')


def logout(request):
    from django.contrib.auth import logout as logout_user
    logout_user(request)
    return redirect("/")
