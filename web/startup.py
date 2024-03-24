from django.db import IntegrityError
from web.models import Genre


def starting():
    genres = (Genre(genre_name="Фантастика"),
              Genre(genre_name="Детектив"),
              Genre(genre_name="Ужас"),
              Genre(genre_name="Приключение"),
              Genre(genre_name="Любовный роман"),
              Genre(genre_name="Бизнес"),
              Genre(genre_name="Психология"),
              Genre(genre_name="Научная литература"),
              Genre(genre_name="Компьютерная литература"),
              Genre(genre_name="История"),
              Genre(genre_name="Мемуары"),
              Genre(genre_name="Искусство и культура"),
              Genre(genre_name="Детская литература"),
              )
    for genre in genres:
        try:
            genre.save()
        except IntegrityError:
            break
