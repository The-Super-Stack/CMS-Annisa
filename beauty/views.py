from django.shortcuts import render, get_object_or_404
from django.views.generic import *
from backend.models import Profile, Post
from .forms import *
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.db.models import Q as __

links = 'link'


class MainPage(TemplateView):
    template_name = 'beauty/main.html'

    def get_context_data(self, **kwargs):
        context = super(MainPage, self).get_context_data(**kwargs)
        profile = get_object_or_404(Profile, pk=1)
        latest = Post.objects.all()[:3]

        context['profile'] = profile
        context['latest'] = latest
        return context


class AddSubscriber(CreateView):
    model = Subscriber
    form_class = AddSubscriberForm
    template_name = 'beauty/sub.html'


class PageDetail(DetailView):
    model = Post
    template_name = 'beauty/detail.html'
    context_object_name = 'post'
    query_pk_and_slug = True
    slug_field = links
    slug_url_kwarg = links

    def get_context_data(self, **kwargs):
        context = super(PageDetail, self).get_context_data(**kwargs)
        form = AddCommentForm
        comments = PostComment.objects.all()

        context['form'] = form
        context['comments'] = comments
        return context


class PageListView(ListView):
    model = Post
    context_object_name = 'post'
    template_name = 'beauty/list.html'
    ordering = '-id'
    paginate_by = 5

    def get_queryset(self):
        q = self.request.GET.get('q')

        if q is not None:
            post = Post.objects.filter(
                __(title__icontains=q) | __(content__icontains=q) |
                __(desc__icontains=q) | __(keyword__icontains=q)
            ).order_by(self.ordering)
            return post

        return Post.objects.all()


class AddComment(CreateView):
    model = PostComment
    form_class = AddCommentForm

    def get_success_url(self):
        return reverse('beauty:detail', kwargs={'link': self.kwargs[link]})

    def form_valid(self, form):
        def current_pk():
            comment = PostComment.objects.all().order_by('-id').first()
            if comment is None:
                return 0
            return int(comment.pk)
        
        if not self.request.POST.get('name'):
            form.instance.name = f"Anonymous{current_pk()}"
        else:
            form.instance.name = self.request.POST.get('name')
            
        post = get_object_or_404(Post, link=self.kwargs['link'])
        form.instance.post = post
        return super(AddComment, self).form_valid(form)


def add_likes(request, link):
    if request.method == 'POST':
        post = get_object_or_404(Post, link=link)
        if post:
            post.likes += 1
            post.save()
    return HttpResponseRedirect(reverse('beauty:detail', args=[link]))



