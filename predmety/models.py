from django.db.models import *

class Predmet(Model):
    id = IntegerField(primary_key=True, blank=True)
    title = CharField('Предмет', max_length=200)
    image = ImageField('Фото', upload_to='photos', blank=True)
    text = TextField('Текст')

    def __str__(self):
        return self.title

class Comment(Model):
    predmet = ForeignKey(Predmet, on_delete=CASCADE)
    author = CharField('Автор', max_length=50)
    text = TextField('Текст комментария')