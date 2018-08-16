from django.shortcuts import render
from django.contrib.auth import authenticate, login as auth_login
# from usuario.form import LoginForm
from django.views.decorators.csrf import csrf_exempt
from sala.models import Sala

@csrf_exempt
def login(request):
    if request.method == 'GET':
        return render(request, 'usuario/login.html')
    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            salas = Sala.objects.filter(usuarios=user.id)
            contexto = {'msg': "Login efetuado com sucesso", 'user': user, 'salas': list(map(lambda x: x.nome, salas))[0]}
            return render(request, "index.html", contexto)
        else:
            contexto = {'msg': 'Usuário e senha não correspondem', 'username':username, 'password':password}
            return render(request, "usuario/login.html", contexto)
