from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from .models import User


def profiles(request):
    users = User.objects.all()

    return HttpResponse(users)


def profile(request, username):
    user_profile = User.objects.get(username=username)
    data = {
        "author": user_profile
    }
    return render(request, "author/profile.html", data)


def follow_toggle(request, author):
    author_obj = User.objects.get(username=author)
    current_user_obj = User.objects.get(username=request.user.username)
    following = author_obj.following.all()

    if author != current_user_obj.username:
        if current_user_obj in following:
            author_obj.following.remove(current_user_obj.id)
        else:
            author_obj.following.add(current_user_obj.id)

    return HttpResponseRedirect(reverse(profile, args=[author_obj.username]))
