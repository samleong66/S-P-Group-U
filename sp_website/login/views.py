from django.shortcuts import render, redirect
import sqlite3
from hashlib import sha256
from django.contrib.auth.models import User
import time

# Create your views here.

conn = sqlite3.connect('user.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS users (
             username TEXT PRIMARY KEY,
             password TEXT)''')
conn.commit()
conn.close()


def register(username, password):
    conn = sqlite3.connect('user.db')
    c = conn.cursor()
    # encrypt username and password
    hashed_password = sha256(password.encode()).hexdigest()
    c.execute('INSERT INTO users VALUES (?, ?)', (username, hashed_password))
    conn.commit()
    conn.close()

def authenticate(username, password):
    conn = sqlite3.connect('user.db')
    c = conn.cursor()
    hashed_password = sha256(password.encode()).hexdigest()
    c.execute('SELECT * FROM users WHERE username=? AND password=?', (username, hashed_password))
    user = c.fetchone()
    conn.close()
    return user is not None


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            # Redirect to a success page.
            return redirect('index')  # Replace 'index' with the name of your homepage URL pattern.
        else:
            # Return an 'invalid login' error message.
            return render(request, 'login.html', {'error': 'Invalid username or password'})
    else:
        return render(request, 'login.html')


def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        hashed_password = sha256(password.encode()).hexdigest()
        # Check if username already exists
        if User.objects.filter(username=username).exists():
            return render(request, 'signup.html', {'error': 'Username already exists'})
        # Create new user
        User.objects.create_user(username=username, password=hashed_password)
        return redirect('success')
    return render(request, 'signup.html')


def success(request):
    return render(request, 'success.html')