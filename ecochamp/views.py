import os

from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.http import HttpResponse
import random
from .forms import SignUpForm
from django.contrib import messages
from .forms import SignUpForm
from django.contrib.auth.models import User
from .forms import CustomAuthenticationForm

# Start here
def start(request):
    return render(request, "ecochamp/start.html")

def create_user_view(request):
    # Create the user
    user = User.objects.create_user(username='oldUserPerson', email='olduser3354@gmail.com', password='oldchamp')
    # Save the user
    user.save()
    return render(request, 'success.html')

# Handles backend of user homepage
def home(request):

    statistics_and_challenges = {
        "Every day, Americans throw away 25 trillion Styrofoam cups!": "Replace your drink's Styrofoam cup with a paper cup or mug! (25 Points)",
        "Over 1 million marine animals are killed by plastic each year!": "Carry a reusable water bottle instead of buying bottled water! (50 Points)",
        "The average person eats 70,000 microplastics each year!": "Use a reusable shopping bag instead of single-use plastic bags! (30 Points)",
        "Approximately 8 million tons of plastic enter the ocean every year!": "Reduce your use of single-use plastic utensils by bringing your own reusable set! (40 Points)",
        "The Great Pacific Garbage Patch is estimated to be 1.6 million square kilometers in size!": "Join a local environmental organization and advocate for policies that reduce plastic pollution! (60 Points)",
        "It takes 450 years for a plastic bottle to decompose in the environment!": "Commit to using a refillable water bottle instead of buying bottled water! (75 Points)"
    }

    random_statistic = random.choice(list(statistics_and_challenges.keys()))
    corresponding_challenge = statistics_and_challenges[random_statistic]

    return render(request, 'ecochamp/home.html', {'random_statistic': random_statistic, 'corresponding_challenge': corresponding_challenge})

# Handles backend of the Sign Up page
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # Optionally, you can automatically log in the user after signup
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Redirect to the home page after successful signup
            else:
                messages.error(request, 'Failed to log in after signup.')
    else:
        form = SignUpForm()
    return render(request, 'ecochamp/signup.html', {'form': form})

# Handles backend of the Log In page
def user_login(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('home')
    else:
        form = CustomAuthenticationForm(request)
    return render(request, 'ecochamp/login.html', {'form': form})
    
# Handles backend of the User Profile page
def profile(request):

    return render(
        request,
        'ecochamp/profile.html',
        {
            'name': "Kevin",
        }
    )

# Handles backend of the Edit Avatar page
def avatar(request):
    return render(request, "ecochamp/avatar.html")

# Handles backend of the How You Can Help Us page
def help(request):
    return render(request, "ecochamp/help.html")

# Handles backend of FAQ page
def faq(request):
    module_dir = os.path.dirname(__file__)
    file_path = os.path.join(module_dir, 'example.txt')

    try:
        with open(file_path, 'r') as file:
            faq_entries = [line.strip().split('|') for line in file.readlines()]
    except FileNotFoundError:
        faq_entries = []

    query = request.GET.get('query', '')
    result = None
    error = None

    if query:
        for entry in faq_entries:
            if query.lower() in entry[0].lower():
                result = entry
                break
        else:
            error = 'No results found.'

    context = {
        'entries': faq_entries,
        'query': query,
        'result': result,
        'error': error,
    }

    return render(request, 'ecochamp/faq.html', context)
