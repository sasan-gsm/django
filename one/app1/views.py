from django.http.response import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Tag, Post
from django.views.generic import View


def homepage(request):
    tag_list = Tag.objects.all()
    output = ", ".join([tag.name for tag in tag_list])
    return HttpResponse(output)

class PostList(View):
    template_name = 'app1/post_list.html'
    def get(self, request, parent_template=None):
        return render(request, self.template_name, {'post_list': Post.objects.all()})

def post_detail(request, year, month, slug, parent_template=None):
    post = get_object_or_404(Post, pub_date__year=year, pub_date__month=month, slug=slug)
    return render(request, 'app1/post_detail.html', {'post': post, 'parent_template': parent_template})


