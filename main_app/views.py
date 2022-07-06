
from django.shortcuts import render
# Add the following import
from django.views.generic.edit import CreateView
from .models import Cat

# Add UdpateView & DeleteView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# Add the following import
from django.http import HttpResponse

# Define the home view
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')



def cats_index(request):
    cats = Cat.objects.all()
    return render(request, 'cats/index.html', { 'cats': cats })



def cats_detail(request, cat_id):
  cat = Cat.objects.get(id=cat_id)
  return render(request, 'cats/detail.html', { 'cat': cat })



class CatCreate(CreateView):
  model = Cat
  fields = '__all__'
  success_url = '/cats/'


class CatUpdate(UpdateView):
  model = Cat
  # Let's disallow the renaming of a cat by excluding the name field!
  fields = ['breed', 'description', 'age']

class CatDelete(DeleteView):
  model = Cat
  success_url = '/cats/'