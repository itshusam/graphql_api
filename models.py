from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, String, Float, Table, ForeignKey

db = SQLAlchemy()

movie_genre = Table(
    'movie_genre', db.metadata,
    mapped_column('movie_id', Integer, ForeignKey('movies.id'), primary_key=True),
    mapped_column('genre_id', Integer, ForeignKey('genres.id'), primary_key=True)
)

class Movie(db.Model):
    __tablename__ = 'movies'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[str] = mapped_column(String(500))
    release_year: Mapped[int] = mapped_column(Integer)

    genres = relationship('Genre', secondary=movie_genre, back_populates='movies')

    def __repr__(self):
        return f"<Movie(id={self.id}, title={self.title}, release_year={self.release_year})>"

class Genre(db.Model):
    __tablename__ = 'genres'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)

    movies = relationship('Movie', secondary=movie_genre, back_populates='genres')

    def __repr__(self):
        return f"<Genre(id={self.id}, name={self.name})>"

def get_all_movies():
    return Movie.query.all()

def get_all_genres():
    return Genre.query.all()

def create_tables():
    with db.app.app_context():
        db.create_all()
