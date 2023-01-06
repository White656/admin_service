from .film_work import FilmWork
from .genres import GenreFilmWork, Genres
from .person import Person, PersonFilmWork

model_mapper = {
    'genre': Genres,
    'genre_film_work': GenreFilmWork,
    'person': person,
    'person_film_work': PersonFilmWork,
    'film_work': FilmWork
}  # keys correspond to the names of tables in the content schema in database.
