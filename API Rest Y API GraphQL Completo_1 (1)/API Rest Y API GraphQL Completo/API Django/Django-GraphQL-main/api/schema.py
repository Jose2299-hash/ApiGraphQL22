import graphene
from graphene_django import DjangoObjectType
from .models import Publicacion, Category

class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = ("id", "nombre")

class PublicacionType(DjangoObjectType):
    class Meta:
        model = Publicacion
        fields = ("id", "titulo", "contenido", "categoria", "creado_en")

class CrearPublicacion(graphene.Mutation):
    publicacion = graphene.Field(PublicacionType)

    class Arguments:
        titulo = graphene.String(required=True)
        contenido = graphene.String(required=True)
        categoria_id = graphene.ID(required=True)

    def mutate(self, info, titulo, contenido, categoria_id):
        try:
            categoria = Category.objects.get(pk=categoria_id)
        except Category.DoesNotExist:
            raise Exception("Categoría no encontrada")

        publicacion = Publicacion.objects.create(
            titulo=titulo,
            contenido=contenido,
            categoria=categoria
        )
        return CrearPublicacion(publicacion=publicacion)

class Query(graphene.ObjectType):
    todas_publicaciones = graphene.List(PublicacionType)

    def resolve_todas_publicaciones(root, info):
        return Publicacion.objects.all().order_by('-creado_en')

class Mutation(graphene.ObjectType):
    crearPublicacion = CrearPublicacion.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)
