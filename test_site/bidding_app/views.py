from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout as django_logout
from django.shortcuts import redirect, render
from django.core.paginator import Paginator
from datetime import datetime
from .models import ClientApplicationData
from .forms import ApplicationDataForm_part1, ApplicationDataForm_part2

# view used for user signup
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            # send the logged in user to the index page
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


def index(request):
    if request.user.is_authenticated:
        return render(request, 'index.html')
    else:
        return redirect('/accounts/login/')


def logout(request):
    django_logout(request)
    response = redirect('/accounts/login/')
    return response


def view_bids(request):
    if request.user.is_authenticated:
        query_results = ClientApplicationData.objects.all().order_by('-added')
        context = {"query_results": query_results}
        return render(request, 'view_bids.html', context)
    else:
        response = redirect('/accounts/login/')
        return response


def multi_stage_bid_form(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = ApplicationDataForm_part1(request.POST)
            if 'title' in request.session:
                #if form.is_valid():
                form = ApplicationDataForm_part2(request.POST)
                form.instance.user = request.user
                form.instance.title = request.session['title']
                form.instance.first_name = request.session['first_name']
                form.instance.last_name = request.session['last_name']
                form.instance.date_of_birth = datetime.strptime(request.session['date_of_birth'], "%Y/%m/%d")
                if form.is_valid():
                    form.save()
                    return render(request, 'index.html')
            else:
                form = ApplicationDataForm_part1(request.POST)
                if form.is_valid():
                    fields = ['title', 'first_name', 'last_name']
                    for field in fields:
                        request.session[field] = form.cleaned_data.get(field)
                    request.session['date_of_birth'] = form.cleaned_data.get('date_of_birth').strftime("%Y/%m/%d")
                    form = ApplicationDataForm_part2()
                    return render(request, 'create_bid.html', {'form': form})
        else:
            form = ApplicationDataForm_part1()
        return render(request, 'create_bid.html', {'form': form})
    else:
        response = redirect('/accounts/login/')
        return response