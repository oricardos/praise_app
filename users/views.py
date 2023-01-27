from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import auth, messages
from artists.models import Artist
from songs.models import Song

def register(request):
    if request.method == 'POST':
      # recuperando valores dos inputs no front
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if void_field(name): #impede campo nome vazio
          messages.error(request,'O campo nome não pode ficar vazio')
          return redirect('register')
        if void_field(email): #impede campo email vazio
          messages.error(request,'O campo nome não pode ficar vazio')
          return redirect('register')
        if password != confirm_password: #verifica se as senhas sao iguais
          messages.error(request, 'As senhas não são iguais!')
          return redirect('register')
        if User.objects.filter(email=email).exists(): #verifica se o usuário já existe
          messages.error(request,'Usuário já cadastrado')
          return redirect('register')
        if User.objects.filter(username=name).exists(): #verifica se o usuário já existe
          messages.error(request,'Usuário já cadastrado')
          return redirect('register')
        user = User.objects.create_user(username=name, email=email, password=password) #cria objeto do usuário
        user.save() #salva usuario na base de dados
        messages.success(request, 'Cadastro realizado com sucesso')
        return redirect('login')
    else:
        return render(request, 'users/register.html')

def login(request):
    if request.method == 'POST':
        # recuperando valores dos inputs no front
        email = request.POST['email']
        password = request.POST['password']
        if void_field(email) or void_field(password): #verifica se os campos estao preenchidos
            messages.error(request,'Os Campos não podem ficar em branco.')
            return redirect('login')
        if User.objects.filter(email=email).exists():
            name = User.objects.filter(email=email).values_list('username', flat=True)[0]
            user = auth.authenticate(request, username=name, password=password)
            if user is not None:
                auth.login(request, user)
        messages.success(request, 'Bem-vindo(a) de volta!')
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
  song = Song.objects.all()
  context = {
    'artists': Artist.objects.all(),
    # 'spotify_help_text': song[0].spotify,
  }
  
  if request.method == 'POST':
    if is_posted := request.POST.get('is_posted', False) == 'on':
      is_posted = True
    song_name = request.POST['song_name']
    artist = get_object_or_404(Artist, pk=request.POST['artist'])
    matters = request.POST['matters']
    video = request.POST['video']
    playback = request.POST['playback']
    spotify = request.POST['spotify']
    ytmusic = request.POST['ytmusic']
    featured_image = request.POST['featured_image']
    note = request.POST['note']
    lyric = request.POST['lyric']
    voices = request.POST['voices']
    extra_voice = request.POST['extra_voice']
    voice_file = request.FILES.get('voicefile', None)
    tone = request.POST['tone']
    cipher = request.POST['cipher']
    bpm = request.POST['bpm']
    acoustic_guitar = request.POST['acoustic_guitar']
    electric_guitar = request.POST['electric_guitar']
    keyboard = request.POST['keyboard']
    bass = request.POST['bass']
    drums = request.POST['drums']
    instrumental_file = request.FILES.get('instrumentalfile', None)

    song = Song.objects.create(is_posted=is_posted, song_name=song_name, 
      artist=artist, matters=matters, video=video,
      playback=playback, spotify=spotify, ytmusic=ytmusic,featured_image=featured_image,
      note=note, lyric=lyric, voices=voices, extra_voice=extra_voice,
      voice_file=voice_file, tone=tone,
      cipher=cipher, bpm=bpm, acoustic_guitar=acoustic_guitar,
      electric_guitar=electric_guitar, keyboard=keyboard, bass=bass,
      drums=drums, instrumental_file=instrumental_file)

    song.save()
    messages.success(request, 'Música adicionada com sucesso, confira na lista de músicas ou faça uma busca.')
    return redirect('index')
  else:
    return render(request, 'new_song.html', context)

def void_field(field):
  return not field.strip()

def user_settings(request, id):
  user = User.objects.get(pk=id)

  if request.method == 'POST':
    name = request.POST['name']
    user.username = name
    print(name)
    user.save()
    messages.success(request, 'Informações atualizadas')
    return redirect('index')

  context = {
    'user': user,
  }

  return render(request, 'users/settings.html', context)