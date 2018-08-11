from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
import django_filters.rest_framework
from rest_framework import status, viewsets
from . models import subjectModel, articleModel, authorModel
from . serializers import subjectSerializer, articleSerializer, authorSerializer
import requests
from bs4 import BeautifulSoup

class subjectView(viewsets.ModelViewSet):
    queryset = subjectModel.objects.all()
    serializer_class = subjectSerializer
    pagination_class = None

class articleView(viewsets.ModelViewSet):
    queryset = articleModel.objects.all()
    serializer_class = articleSerializer
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)
    filter_fields = ('subject',)

class authorView(viewsets.ModelViewSet):
    queryset = authorModel.objects.all()
    serializer_class = articleSerializer

def index(request):
    page = requests.get('https://techcrunch.com/')
    soup = BeautifulSoup(page.text, 'html.parser')
    content = soup.find(class_='content')
    articles = content.find_all(class_='post-block')
    list = []
    for art in articles:
        link = art.find(class_='post-block__title__link')
        #Article-only section
        title = link.get_text().split('\t')[-4]
        slug = link['href'].split('/')[-2]
        text = art.find(class_='post-block__content').get_text().split('\t')[-2]
        date = art.find('time')['datetime'].split('T')[0]
        hero = art.find('img')
        if hero == None:
            hero = "<img src='http://cofice.com.br/wp-content/uploads/2017/04/no-photo.jpg' width=300 height=160" #"<img src='\static\no-photo.jpg'>"
        tags = art.find('article__tags')
        #Author section
        authors = art.find(class_='river-byline__authors')
        try:
            name = authors.get_text().split('\t')[-4]
        except:
            name = "Not specified"
        list.append(tags)
    response = HttpResponse()
    response.write("Scraper</br></br>")
    response.write(list)

    return response
