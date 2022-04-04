from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render
from .forms import SignUpClientForm

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
            return redirect('clientSignup')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


# view used for user signup
def clientSignup(request):
    if request.method == 'POST':
        form = SignUpClientForm(request.POST)
        if form.is_valid():
            client = form.save(commit=False)
            client.user = request.user
            client.save()
            return redirect('index')
    else:
        form = SignUpClientForm()
    return render(request, 'ClientSignup.html', {'form': form})



def index(request):
    if request.user.is_authenticated:
        return render(request, 'index.html')
    else:
        return redirect('/accounts/login/')
