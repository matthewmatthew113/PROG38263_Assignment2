#Import Various Django Libraries and the Post model
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (ListView,DetailView,CreateView,UpdateView,DeleteView)
from .models import Post

#Defines homepage view
def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)


#Defines view for post listings
class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginated_by = 10

#Defines view for detailed post view
class PostDetailView(DetailView):
    model = Post

#Defines View for post creation
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']
    #Verifies if the form is valid
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

#Defines view for post update
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    #Verifies if the form is valid
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
	
    #Verifies if user is valid
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

#Defines view for post deletion
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    #Verifies if user is valid
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
