from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages

class RegisterView(View):
    def get(self, request):
        user_form = UserCreationForm()
        return render(request, 'register.html', {'user_form': user_form})
    
    def post(self, request):
        user_form = UserCreationForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            messages.success(request, 'Registro realizado com sucesso! Faça login para continuar.')
            return redirect('login')
        else:
            messages.error(request, 'Erro ao registrar. Verifique os dados e tente novamente.')
        return render(request, 'register.html', {'user_form': user_form})

class LoginView(View):
    def get(self, request):
        login_form = AuthenticationForm()
        return render(request, 'login.html', {'login_form': login_form})
    
    def post(self, request):
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Login efetuado com sucesso!')
            return redirect('cars_list')
        else:
            messages.error(request, 'Usuário ou senha incorretos. Tente novamente.')
            login_form = AuthenticationForm()
        messages.error(request, 'Usuário ou senha incorretos. Tente novamente.')
        return render(request, 'login.html', {'login_form': login_form})

class LogoutView(View):
    def get(self, request):
        logout(request)
        messages.success(request, 'Logout efetuado com sucesso!')
        return redirect('login')
