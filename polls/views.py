from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import CreateUserForm
from .models import *


def register_page(request):
    if request.user.is_authenticated:
        return redirect('home')

    else:
        form = CreateUserForm()

        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Your account is registered')
                return redirect('login')

    context = {'form': form}
    return render(request, 'polls/register.html', context)


def login_page(request):
    if request.user.is_authenticated:
        return redirect('home')

    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, 'Username or Password is incorrect')

    context = {}
    return render(request, 'polls/login.html', context)


def logout_page(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def home(request):
    latest_question = Question.objects.all()
    content = {'latest_question': latest_question}
    return render(request, 'polls/home.html', content)


@login_required(login_url='login')
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    content = {'question': question}
    return render(request, 'polls/detail.html', content)


@login_required(login_url='login')
def result(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    content = {'question': question}
    return render(request, 'polls/result.html', content)


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except(KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error': "You didn't select any Choice",
        })

    else:
        selected_choice.votes += 1
        selected_choice.save()

        return HttpResponseRedirect(reverse('result', args=(question.id,)))
