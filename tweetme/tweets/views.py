from django.shortcuts import render
from .models import Tweet


def home_view(request, *args, **kwargs):
    return render(request, 'pages/home.html', context={}, status=200)


def tweet_list_view(request, *args, **kwargs):
    qs = Tweet.objects.all()
    tweet_list = [{'id': x.id, 'content': x.content} for x in qs]
    data = {
        'response': tweet_list
    }
    return JsonResponse(data)
