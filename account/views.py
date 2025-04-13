from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages  # Import messages

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'Logged in successfully')
            return redirect('/')
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('login')
    else:
        return render(request, 'login.html')
    


def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username is already taken')  # Add error message
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'Email is already taken')  # Add error message
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
                user.save()
                messages.success(request, 'User created successfully')  # Add success message
                return redirect('login')  # Redirect to login page after successful registration
        else:
            messages.error(request, 'Passwords do not match')  # Add error message
            return redirect('register')
    else:
        return render(request, 'register.html')
    

   


def logout(request):
    auth.logout(request)
    messages.success(request, 'Logged out successfully')
    return redirect('/') 