from django.shortcuts import render, redirect
from.models import CategoryModel, ArticleModel

# Create your views here.
def new(request):
    if request.method == 'GET':
        all_article = ArticleModel.objects.all()
        return render(request, 'new.html', {'articles':all_article})
    elif request.method == 'POST':
        my_article = ArticleModel()
        title = request.POST.get('title','')
        content = request.POST.get('title','')
        category = request.POST.get('category', '')
        my_article.save()
        return redirect('/category.html')

