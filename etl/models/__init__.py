from etl.models.film_work import FilmWork
from etl.models.genres import GenreFilmWork, Genres
from etl.models.person import Person, PersonFilmWork

model_mapper = {
    'genre': Genres,
    'genre_film_work': GenreFilmWork,
    'person': Person,
    'person_film_work': PersonFilmWork,
    'film_work': FilmWork
}  # keys correspond to the names of tables in the content schema in database.
