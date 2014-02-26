from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.contrib.auth.models import User
from django.shortcuts import render_to_response
from django.contrib.auth import logout
from django.template import RequestContext
from tasks.forms import RegistrationForm, TaskListSaveForm
from tasks.models import *


def main_page(request):
    return render_to_response(
        'main_page.html', RequestContext(request)
    )

def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')

def register_page(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password1'],
                email=form.cleaned_data['email']
            )
            return HttpResponseRedirect('/register/success/')
    else:
        form = RegistrationForm()
    variables = RequestContext(request, {
        'form': form
    })
    return render_to_response(
        'registration/register.html', variables
    )

def todolist_save_page(request):
    if request.method == 'POST':
        form = TaskListSaveForm(request.POST)
        if form.is_valid():
            task, dummy = Task.objects.get_or_create(
                title=form.cleaned_data['title']
            )
            todolist, created = TaskList.objects.get_or_create(
                user=request.user,
                task=task
            )
            todolist.title = form.cleaned_data['title']
            todolist.save()
            return HttpResponseRedirect(
                '/user/%s/' % request.user.username
            )
    else:
        form = TaskListSaveForm()
    variables = RequestContext(request, {
        'form': form
    })
    return render_to_response('todolist_save.html', variables)