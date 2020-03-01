from django.shortcuts import get_object_or_404, render
from .models import Song
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView, CreateView, DeleteView
from django.views.generic.list import ListView
from django.utils import html


@login_required
def special(request):
    return HttpResponse("You are logged in !")


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


def register(request):
    registered = False
    if request.method == 'POST':
        print("post")
        user_form = UserForm(data=request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user = user.save()
        else:
            print(user_form.errors)
    else:
        user_form = UserForm()
    return render(request, 'registration.html', {'user_form': user_form, 'registered': registered})


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('song_list'))
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password:{}".format(
                username, password))
            return HttpResponse("Invalid login details given")
    else:
        return render(request, 'login.html')


class SongListView(ListView):
    model = Song
    context_object_name = "song_list"
    template_name = "song_list.html"


def song_detail(request, id):
    song = get_object_or_404(Song, id=id)
    is_favourite = False
    if song.favourite.filter(id=request.user.id).exists():
        is_favourite = True
    context = {
        'song': song,
        'is_favourite': is_favourite,
    }
    if request.is_ajax():
        return JsonResponse({'form': html})
    return render(request, 'song_detail.html', context)


def song_favourite_list(request):
    user = request.user
    favourite_songs = user.favourite.all()
    context = {
        'favourite_songs': favourite_songs,
    }
    return render(request, 'song_favourite_list.html', context)


def favourite_song(request, id):
    song = get_object_or_404(Song, id=id)
    if song.favourite.filter(id=request.user.id).exists():
        song.favourite.remove(request.user)
    else:
        song.favourite.add(request.user)
    return HttpResponseRedirect(song.get_absolute_url())
