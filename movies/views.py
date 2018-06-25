from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView

from movies.add_movies_data_json_to_db import store_movie_in_db
from movies.db import get_movies_data, get_all_movies_with_charecter
from .models import Movies
from .serializer import moviesSerializer


class movieslist(APIView):

    def get(self, request):
        movies_obj = Movies.objects.all()
        serializers = moviesSerializer(movies_obj, many=True)
        return Response(serializers.data)

    parser_classes = (JSONParser,)
    # parser_classes = (FileUploadParser,)
    # media_type = 'text/plain'

    def post(self, request, format=None):
        return Response({'received data': request.data})


class MovieSearchInList(APIView):

    def get(self, request, movie_name):
        # movie_name = self.request.query_params.get('movie_name')
        q = Q(m_title__icontains=movie_name) | Q(m_director__icontains=movie_name)
        movies_obj = Movies.objects.filter(q)
        # movies_obj = Movies.objects.all()
        serializers = moviesSerializer(movies_obj, many=True)
        return Response(serializers.data)

    def post(self, request, format=None):
        pass


@csrf_protect
def home(request):
    movies_obj = get_movies_data()

    content = {
        'movies_obj': movies_obj,
    }
    return render(request, 'home.html', context=content)


@csrf_protect
def all_movies(request):
    movies_obj = get_movies_data()

    content = {
        'movies_obj': movies_obj,
    }

    return render(request, 'view_movies.html', context=content)


@csrf_protect
def load_movies(request):
    data = store_movie_in_db()

    content = {
        'data': data,
    }
    return render(request, 'home.html')


@csrf_protect
def search_movies(request):
    """
    :param request:
    :return:
    """
    movie_name = request.POST.get('myInput', None)
    movies_obj = get_all_movies_with_charecter(movie_name)
    content = {
        'movies_obj': movies_obj,
    }
    return render(request, 'view_movies.html', context=content)
