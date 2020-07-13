from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.views.generic import ListView
from .models import Post
from django.db.models import Q

class PostList(ListView):
    model = Post

    def get_queryset(self):
        q_word = self.request.GET.get('query')

        if q_word:
            object_list = Post.objects.filter(
                    Q(title__icontains=q_word) | Q(text__icontains=q_word))
        else:
            object_list = Post.objects.all()
        return object_list

def post_list(request):
    object_list = Post.objects.all()
    for post in object_list:
        if len(post.text)>140:
            post.text[138]='.'
            post.text[139]='.'
            post.text[140]='.'
            post.text[141]='\0'
    return render(request, 'templates\article\post_list.html', {'object_list' : object_list})
    
