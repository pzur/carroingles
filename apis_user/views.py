from rest_framework import generics
from django.contrib.auth.models import User
import json
from django.http import HttpResponse
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from .models import People

from rest_framework.authtoken.models import Token
from rest_framework import permissions
from rest_framework import parsers


# Vistas Basadas en Clases Controlando todo el Modelo de Usuarios

class RegisterUsers(generics.CreateAPIView):  # Solo Registrar datos en el modelo
    permission_classes = (permissions.AllowAny,)
    parser_classes = (parsers.JSONParser,)

    def post(self, request, format=None):
        # Creando en Nuevo Usuario
        username = request.data['username']
        email = request.data['email']
        password = request.data['password']
        #first_name = request.data['first_name']
        #last_name = request.data['last_name']
        user = User.objects.create_user(username, email, password)
        #user.first_name = first_name
        #user.last_name = last_name
        user.save()

        # Esta es la informacion que llevara en el perfil
        #telefono = request.data['fono']
        #direccion = request.data['dir']
        #ruc = request.data['ruc']

        # Generando el duro el dato de la persona
        #Personas.objects.create(telefono=telefono, direccion=direccion, ruc=ruc, user=user)

        # generando el token para ese usuario se refiere a la tabla auth_token
        token = Token.objects.create(user=user)
        data = {'detail': 'User created with token:' + token.key}

        response = json.dumps(data)
        return HttpResponse(response, content_type='application/json')


class LoginView(APIView):
    permission_classes = (permissions.AllowAny,)
    parser_classes = (parsers.JSONParser,)

    def post(self, request, format=None):
        username = request.data["nickname"]
        password = request.data["password"]
        user = authenticate(username=username, password=password)
        if user:
            # trae informacion del modelo persona de acuerdo al ID
            #userpersona = Personas.objects.get(user_id=user.id)
            token = Token.objects.get(user_id=user.id)
            data = {#"nombre": user.first_name,
                    #"apellido": user.last_name,
                    #"telefono": userpersona.telefono,
                    #"ruc": userpersona.ruc,
                    "token": token.key}
        else:
            data = {"error": "No Son las Credenciales"}
        response = json.dumps(data)
        return HttpResponse(response, content_type='application/json')

# Serializar Foto
# https://stackoverrun.com/es/q/9792839
