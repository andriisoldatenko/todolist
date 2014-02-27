from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.contrib.auth import logout
from django.template import RequestContext
from tasks.forms import RegistrationForm, TaskSaveForm
from django.contrib.auth.decorators import login_required
from tasks.models import *

@login_required(login_url='/login/')
def main_page(request):
    # user = User.objects.get(username=request.user)
    tasks = Task.objects.filter(user_id=request.user)
    return render_to_response(
        'main_page.html', RequestContext(request, {'tasklist':  tasks})
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
            return HttpResponseRedirect('/')
    else:
        form = RegistrationForm()
    variables = RequestContext(request, {
        'form': form
    })
    return render_to_response(
        'registration/register.html', variables
    )

def task_save_page(request):
    if request.method == 'POST':
        form = TaskSaveForm(request.POST)
        if form.is_valid():
            task, dummy = Task.objects.get_or_create(
                title=form.cleaned_data['title'],
                user=request.user
            )
            task.save()
            return HttpResponseRedirect('/')
    else:
        form = TaskSaveForm()
    variables = RequestContext(request, {
        'form': form
    })
    return render_to_response('todolist_save.html', variables)