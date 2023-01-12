from django.shortcuts import render, redirect
from django.contrib.auth.models import User

def register(request):
    if request.method == 'POST':
      # recuperando valores dos inputs no front
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if not name.strip(): #impede campo nome vazio
          print('O campo nome não pode ficar vazio')
          return redirect('register')
        if not email.strip(): #impede campo email vazio
          print('O campo nome não pode ficar vazio')
          return redirect('register')
        if password != confirm_password: #verifica se as senhas sao iguais
          print('As senhas não são iguais!')
          return redirect('register')
        if User.objects.filter(email=email).exists(): #verifica se o usuário já existe
          print('Usuário já cadastrado')
          return redirect('register')
        user = User.objects.create_user(username=name, email=email, password=password) #cria objeto do usuário
        user.save() #salva usuario na base de dados
        print('usuario Cadastrado com sucesso')
        return redirect('login')
    else:
        return render(request, 'users/register.html')

def login(request):
    return render(request, 'users/login.html')

def logout(request):
    pass

def dashboard(request):
    pass