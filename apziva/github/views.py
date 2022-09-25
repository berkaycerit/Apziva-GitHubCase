from operator import imod
from unicodedata import name
from django.shortcuts import render
from github.forms import PostSearchForm
from github.models import Person
# Create your views here.

def post_search(request):
    form = PostSearchForm
    results = []
    persons = Person.objects.all()

    if 'q' in request.GET:
        form = PostSearchForm(request.GET)
        if form.is_valid():
            q = form.cleaned_data['q']

            results = Person.objects.filter(skills__contains = q)
            print(results)

    return render(request, 'index.html', {'form':form, 'results': results})