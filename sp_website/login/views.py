from django.shortcuts import render, redirect
import sqlite3
from hashlib import sha256
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

conn = sqlite3.connect('user.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS users (
             username TEXT PRIMARY KEY,
             password TEXT)''')
conn.commit()


# def register(username, password):
#     c = conn.cursor()
#     # encrypt username and password
#     hashed_password = sha256(password.encode()).hexdigest()
#     c.execute('INSERT INTO users VALUES (?, ?)', (username, hashed_password))
#     conn.commit()
#     conn.close()
#
# def authenticate(username, password):
#     c = conn.cursor()
#     hashed_password = sha256(password.encode()).hexdigest()
#     c.execute('SELECT * FROM users WHERE username=? AND password=?', (username, hashed_password))
#     user = c.fetchone()
#     conn.close()
#     return user is not None


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')  # Replace 'index' with the name of your homepage URL pattern.
        else:
            return render(request, 'login.html', {'error': 'Invalid username or password'})
    else:
        return render(request, 'login.html')


def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


def success(request):
    return render(request, 'success.html')