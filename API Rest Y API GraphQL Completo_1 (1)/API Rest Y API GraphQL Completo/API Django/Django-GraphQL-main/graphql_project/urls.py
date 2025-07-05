# graphql_project/urls.py

from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from graphene_django.views import GraphQLView
from api.schema import schema
from django.views.decorators.csrf import csrf_exempt
from django.contrib import admin
from django.urls import path
from api.views import post_form
from graphene_django.views import GraphQLView
from django.views.decorators.csrf import csrf_exempt
from django.urls import path
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('graphQL/', csrf_exempt(GraphQLView.as_view(graphiql=True, schema=schema))),
     path('admin/', admin.site.urls),
    path('publicar/', post_form),
    path('', post_form),  # ← Esta línea resuelve el 404 en la raíz
     path('publicaciones.html', views.publicaciones, name='publicaciones'),
]

urlpatterns += [
    path("graphql/", csrf_exempt(GraphQLView.as_view(graphiql=True))),
]