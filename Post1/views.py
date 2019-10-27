from django.shortcuts import render
from .models import Post

# Create your views here.
from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView
# Create your views here.
class PostDetailView(DetailView):
    model = Post
    template_name= 'post/post.html'


def list(request):
    Data = {'Posts': Post.objects.all().order_by("-date")}
    return render(request, 'post/projects.html', Data)

class PostCreateView(CreateView):
    model = Post
    fields = ['title','body', 'cash', 'email']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

