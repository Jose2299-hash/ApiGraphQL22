import strawberry
from strawberry.fastapi import GraphQLRouter
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.requests import Request
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from typing import List

app = FastAPI()

# CORS para permitir fetch desde frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Modelo de publicación
@strawberry.type
class Publicacion:
    id: int
    titulo: str
    contenido: str

# Lista en memoria
publicaciones: List[Publicacion] = []

# Mutaciones
@strawberry.type
class Mutation:
    @strawberry.mutation
    def crear_publicacion(self, titulo: str, contenido: str) -> Publicacion:
        nueva = Publicacion(id=len(publicaciones) + 1, titulo=titulo, contenido=contenido)
        publicaciones.append(nueva)
        return nueva

# Consultas
@strawberry.type
class Query:
    @strawberry.field
    def obtener_publicaciones(self) -> List[Publicacion]:
        return publicaciones

# Configurar GraphQL
schema = strawberry.Schema(query=Query, mutation=Mutation)
graphql_app = GraphQLRouter(schema)
app.include_router(graphql_app, prefix="/graphql")

# Jinja2 para HTML
templates = Jinja2Templates(directory="templates")

# Formulario para crear
@app.get("/", response_class=HTMLResponse)
async def crear_publicacion_view(request: Request):
    return templates.TemplateResponse("write.html", {"request": request})

# Lista de publicaciones
@app.get("/posts_list", response_class=HTMLResponse)
async def lista_publicaciones_view(request: Request):
    return templates.TemplateResponse("posts_list.html", {"request": request, "posts": publicaciones})

