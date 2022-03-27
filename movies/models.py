from django.db import models
from datetime import date
from django.urls import reverse

class Category(models.Model):
    name = models.CharField("Имя", max_length=150)
    description = models.TextField("Описание")
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

class Actor(models.Model):
    name = models.CharField("Имя", max_length=150)
    age = models.PositiveSmallIntegerField("Возраст", default=30)
    description = models.TextField("Описание")
    image = models.ImageField("Изображение", upload_to="actor/")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Актер и режиссер"
        verbose_name_plural = "Актеры и режиссеры"

class Genre(models.Model):
    name = models.CharField("Имя", max_length=150)
    description = models.TextField("Описание")
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"

class Movie(models.Model):
    name = models.CharField("Имя", max_length=150)
    description = models.TextField("Описание")
    tagline = models.CharField("Слоган", max_length=200, default='')
    poster = models.ImageField("Постер", upload_to="movies/")
    year = models.PositiveSmallIntegerField("Год", default=2019)
    country = models.CharField("Страна", max_length=100)
    producer = models.ManyToManyField(Actor, verbose_name="Режиссеры", related_name="movie_producer")
    actor = models.ManyToManyField(Actor, verbose_name="Актеры", related_name="movie_actor")
    premier = models.DateField("Премьера в мире", default=date.today)
    budget = models.PositiveSmallIntegerField("Бюджет", default=1000000)
    genre = models.ManyToManyField(Genre, verbose_name="Жанры")
    fees_usa = models.CharField("Сборы в США", max_length=100, help_text="Указывать сумму в долларах", default=0)
    fees_world = models.CharField("Сборы в мире", max_length=100, help_text="Указывать сумму в долларах", default=0)
    category = models.ForeignKey(Category, verbose_name="Категория", on_delete=models.SET_NULL, null=True)
    url = models.SlugField(max_length=160, unique=True)
    draft = models.BooleanField("Черновик", default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Фильм"
        verbose_name_plural = "Фильмы"

    def get_absolute_url(self):
        return reverse("movie_detail", kwargs={"slug": self.url})

class Film_Still(models.Model):
    name = models.CharField("Имя", max_length=150)
    description = models.TextField("Описание")
    image = models.ImageField("Изображение", upload_to="actor/")
    movie = models.ForeignKey(Movie, on_delete=models.SET_NULL, null=True, verbose_name="Кадр из фильма")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Кадр из фильма"
        verbose_name_plural = "Кадры из фильма"

class Stars_Rate(models.Model):
    value = models.PositiveSmallIntegerField("Значение", default=0)

    def __str__(self):
        return self.value

    class Meta:
        verbose_name = "Звезда рейтинга"
        verbose_name_plural = "Звезды рейтинга"

class Rate(models.Model):
    ip = models.CharField("IP-adress", max_length=15)
    star = models.ForeignKey(Stars_Rate, on_delete=models.CASCADE, verbose_name="Оценка")
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, verbose_name="Фильм")

    def __str__(self):
        return f"{self.star} - {self.movie}"

    class Meta:
        verbose_name = "Оценка"
        verbose_name_plural = "Оценки"

class Revies(models.Model):
    email = models.EmailField("Почта", max_length=200)
    name = models.CharField("Имя", max_length=150)
    text = models.TextField("Текст", max_length=3000)
    parent = models.ForeignKey('self', verbose_name="Родитель", on_delete=models.SET_NULL, blank=True, null=True)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, verbose_name="Фильм")

    def __str__(self):
        return f"{self.name} - {self.movie}"

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"