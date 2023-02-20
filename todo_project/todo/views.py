from django.shortcuts import render ,  redirect
from .models import Todo
from .models import TodoForm
# Create your views here.
# where the whole html goes.
def home(request):
    list = Todo.objects.all()
    return render(request, 'home.html',{'list' : list})

def add (request):
    list = Todo.objects.order_by('time')
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    
    form = TodoForm()
    return render(request , 'add.html' , {"form" : form  , "list": list})
