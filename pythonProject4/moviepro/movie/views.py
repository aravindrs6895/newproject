from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from . models import movie1
from . forms import movieform
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView,DeleteView


# Create your views here.
def note(request):
    a=movie1.objects.all()
    return render(request,'noted.html',{'bb':a})

def detail(request,id):
    q=movie1.objects.get(id=id)
    return render(request,'noted1.html',{'ww':q})
def happy(request):
    if request.method=="POST":
        name=request.POST.get('name',)
        year=request.POST.get('year',)
        des=request.POST.get('des',)
        image=request.FILES['image']
        z=movie1(name=name,year=year,des=des,image=image)
        z.save()
        return redirect('/')
    return render(request,'new html.html')
def update(request,id):
    m = movie1.objects.get(id=id)
    form=movieform(request.POST or None,request.FILES,instance=m)
    if form. is_valid():
        form.save()
        return redirect('/')
    else:
        form=movieform(instance=m)
    return render (request,'forms1.html',{'ww':m,'form':form})
def delete(request,id):
    if request.method=='POST':
        l=movie1.objects.get(id=id)
        l.delete()
        return redirect('/')
    return render (request,'delete.html')

class movielistview(ListView):
    model=movie1
    template_name="noted.html"
    context_object_name='bb'

class moviedetailview(DetailView):
    model=movie1
    template_name="noted1.html"
    context_object_name='ww'

class movieupdateview(UpdateView):
    model=movie1
    template_name='update.html'
    context_object_name = ''
    fields = ('name','des','image')
    def get_success_url(self):
        return reverse_lazy(('movie:ad'),kwargs={'pk':self.object.id})

class moviedeleteview(DeleteView):
    model=movie1
    template_name='delete.html'
    success_url = reverse_lazy('movie:as')