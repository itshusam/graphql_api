import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType
from models import db, Movie, Genre

class MovieType(SQLAlchemyObjectType):
    class Meta:
        model = Movie
        interfaces = (graphene.relay.Node,)

class GenreType(SQLAlchemyObjectType):
    class Meta:
        model = Genre
        interfaces = (graphene.relay.Node,)

class CreateGenre(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)

    genre = graphene.Field(GenreType)

    def mutate(self, info, name):
        genre = Genre(name=name)
        db.session.add(genre)
        db.session.commit()
        return CreateGenre(genre=genre)

class UpdateGenre(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        name = graphene.String(required=True)

    genre = graphene.Field(GenreType)

    def mutate(self, info, id, name):
        genre = Genre.query.get(id)
        if genre:
            genre.name = name
            db.session.commit()
        return UpdateGenre(genre=genre)

class DeleteGenre(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)

    success = graphene.Boolean()

    def mutate(self, info, id):
        genre = Genre.query.get(id)
        if genre:
            db.session.delete(genre)
            db.session.commit()
            return DeleteGenre(success=True)
        return DeleteGenre(success=False)

class Query(graphene.ObjectType):
    movies_by_genre = graphene.List(MovieType, genre_id=graphene.Int())
    genre_by_movie = graphene.List(GenreType, movie_id=graphene.Int())

    def resolve_movies_by_genre(self, info, genre_id):
        genre = Genre.query.get(genre_id)
        return genre.movies if genre else []

    def resolve_genre_by_movie(self, info, movie_id):
        movie = Movie.query.get(movie_id)
        return movie.genres if movie else []

class Mutation(graphene.ObjectType):
    create_genre = CreateGenre.Field()
    update_genre = UpdateGenre.Field()
    delete_genre = DeleteGenre.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)
