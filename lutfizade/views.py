from lutfizade.models import Aboutme
from blog.models import Blog
from idea.models import Idea
from django.shortcuts import redirect, render
from idea.form import IdeaForm


def MainPageView(request):
    form = IdeaForm()
    ideas = Idea.objects.all()
    blogs = Blog.objects.order_by('date')[:3]
    aboutme = Aboutme.objects.first()
    if request.method == 'POST':
        form = IdeaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main')
    context = {
        'form':form,
        'ideas':ideas,
        'blogs':blogs,
        'aboutme':aboutme
    }
    return render(request, 'index.html',context)
