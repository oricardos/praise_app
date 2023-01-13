from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth 
from artists.models import Artist

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
    if request.method == 'POST':
        # recuperando valores dos inputs no front
        email = request.POST['email']
        password = request.POST['password']
        if email == '' or password == '': #verifica se os campos estao preenchidos
            print('Os Campos não podem ficar em branco')
            return redirect('login')
        if User.objects.filter(email=email).exists():
            name = User.objects.filter(email=email).values_list('username', flat=True)[0]
            user = auth.authenticate(request, username=name, password=password)
            if user is not None:
                auth.login(request, user)
        return redirect('index') #se o login for realizado com sucesso, redireciona para tela de listagem / index
    return render(request, 'users/login.html')

def logout(request):
    auth.logout(request)
    return redirect('login')


def dashboard(request):
  if request.user.is_authenticated:
    return render(request, 'users/dashboard.html')
  else: 
    return redirect('login')

def new_song(request):
  artists_data = Artist.objects.all()
  artists = {
    'artists': artists_data
  }
  return render(request, 'new_song.html', artists)
