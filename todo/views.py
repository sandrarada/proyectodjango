from django.shortcuts import render,redirect
from . models import Tarea
from .forms import TareaForm
# Create your views here.
def home(request):
    tareas= Tarea.objects.all()
    context={'tareas':tareas}
    return render(request,'home.html',context)

def agregar(request):
    if request.method=="Post":
        form=TareaForm(redirect.Post)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form=TareaForm()
    context={'form': form}
    return render(request,'agregar.html',context)