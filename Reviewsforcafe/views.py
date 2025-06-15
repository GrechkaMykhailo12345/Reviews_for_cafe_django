from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm, ReviewForm
from .models import Review
from django.contrib import messages

def review_list(request):
    reviews = Review.objects.all()
    return render(request, 'Reviewsforcafe/review_list.html', {'reviews': reviews})

@login_required
def add_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.author = request.user
            review.save()
            messages.success(request, 'Ваш відгук успішно додано!')
            return redirect('review_list')
        else:
            messages.error(request, 'Будь ласка, виправте помилки у формі.')
    else:
        form = ReviewForm()
    return render(request, 'Reviewsforcafe/add_review.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f'Вітаємо, {user.username}! Ви успішно зареєстровані.')
            return redirect('review_list')
        else:
            messages.error(request, 'Помилка реєстрації. Перевірте дані.')
    else:
        form = CustomUserCreationForm()
    return render(request, 'Reviewsforcafe/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Вітаємо, {username}! Ви успішно увійшли.')
                return redirect('review_list')
            else:
                messages.error(request, 'Невірне ім\'я користувача або пароль.')
        else:
            messages.error(request, 'Невірне ім\'я користувача або пароль.')
    else:
        form = AuthenticationForm()
    return render(request, 'Reviewsforcafe/login.html', {'form': form})

@login_required
def user_logout(request):
    logout(request)
    messages.info(request, 'Ви успішно вийшли з системи.')
    return redirect('review_list')