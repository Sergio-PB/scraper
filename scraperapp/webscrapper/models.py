from django.db import models
from django.contrib import admin

class subjectModel(models.Model):
    '''
    Subject model class:

    name(CharField) -> Outlet/Subject's name
    color(CharField) -> color in HEX
    '''
    name = models.CharField(max_length=255)
    color = models.CharField(max_length=7)

    def __str__(self):
        return self.name

class authorModel(models.Model):
    '''
    Author model class:

    name(CharField) -> author's name
    picture(ImageField) -> author's picture
    '''
    name = models.CharField(max_length=255)
    picture = models.ImageField(upload_to='webscrapper/imgs/author')

    def __str__(self):
        return self.name

class articleModel(models.Model):
    '''
    Article model class:

    title(CharField) -> article's title
    slug(CharField) -> article's slug(short title so that devs can find them)
    author(CharField) -> article's author
    subject(CharField) -> article's subject
    hero_image(ImageField) -> article's hero image (head banner)
    pub_date(DateField) -> article's published date
    text(CharField) -> article's brief description
    '''
    title = models.CharField(max_length=30)
    slug = models.SlugField(max_length=10)
    author = models.CharField(max_length=20)
    subject = models.CharField(max_length=10)
    hero_image = models.ImageField(upload_to='webscrapper/imgs/article')
    pub_date = models.DateField('date published')
    text = models.CharField(max_length=200)

    def __str__(self):
        return str(self.id) + ' - ' + self.title + ' - ' + self.subject + ' - ' + str(self.pub_date) + ' - ' + self.author
