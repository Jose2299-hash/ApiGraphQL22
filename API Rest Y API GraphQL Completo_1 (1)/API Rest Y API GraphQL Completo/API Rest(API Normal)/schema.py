import graphene
from graphene_django import DjangoObjectType
from .models import Publicacion

class PublicacionType(DjangoObjectType):
    class Meta:
        model = Publicacion
        fields = ("id", "titulo", "contenido", "fecha_creacion")

class CrearPublicacion(graphene.Mutation):
    publicacion = graphene.Field(PublicacionType)

    class Arguments:
        titulo = graphene.String(required=True)
        contenido = graphene.String(required=True)

    def mutate(self, info, titulo, contenido):
        user = info.context.user
        if user.is_anonymous:
            raise Exception("Debes iniciar sesión para crear publicaciones")
        nueva = Publicacion(titulo=titulo, contenido=contenido)
        nueva.save()
        return CrearPublicacion(publicacion=nueva)

class Query(graphene.ObjectType):
    publicaciones = graphene.List(PublicacionType)

    def resolve_publicaciones(root, info):
        return Publicacion.objects.order_by('-fecha_creacion').all()

class Mutation(graphene.ObjectType):
    crearPublicacion = CrearPublicacion.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)
