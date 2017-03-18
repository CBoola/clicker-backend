from django.shortcuts import render, redirect


def main_page(request):
    if not request.user.is_anonymous:
        return redirect("/game")

    return render(request, 'main_page.html')


def logout(request):
    from django.contrib.auth import logout as logout_user
    logout_user(request)
    return redirect("/")
