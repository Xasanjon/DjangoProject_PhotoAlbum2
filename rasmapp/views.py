from django.shortcuts import render, redirect
from .models import *
# Create your views here.


def allPhotos(request):
    category = request.GET.get('category')

    context = {}
    if category == None:
        photos = Photo.objects.all()
    else:
        photos = Photo.objects.filter(category__id=category)

    categories = Category.objects.all()
    context['categories'] = categories
    context['photos'] = photos

    return render(request, 'index.html', context)


def addPhoto(request):
    context = {}
    categories = Category.objects.all()
    context['categories'] = categories

    if request.method == 'POST':
        data = request.POST
        image = request.FILES.getlist('image')
        if data['category_selected'] != "None":
            category = Category.objects.get(id=data['category_selected'])
        elif data['category_new'] != "":
            category, created = Category.objects.get_or_create(
                name=data['category_new'])
        else:
            category = None
        for img in image:
            photo = Photo.objects.create(
                category=category, description=data['description'], image=img)
        return redirect('all-photos')
    return render(request, 'add-photo.html', context)


def seePhoto(request):
    pk = request.GET['pk']
    photo = Photo.objects.get(id=int(pk))
    return render(request, 'photo.html', {'photo': photo})


def deletePhoto(request):
    pk = request.GET['pk']
    photo = Photo.objects.get(id=int(pk)).delete()
    return redirect('all-photos')


def editePhoto(request):
    context = {}
    categories = Category.objects.all()
    context['categories'] = categories

    if request.method == 'POST':
        data = request.POST
        image = request.FILES.get('image')
        if data['category_selected'] != "None":
            category = Category.objects.get(id=data['category_selected'])
        elif data['category_new'] != "":
            category, created = Category.objects.get_or_create(
                name=data['category_new'])
        else:
            category = None
        photo = Photo.objects.get(id=data['jona'])
        photo.category = category
        if image is not None:
            photo.image = image
        else:
            photo.image = data['image_old']
        photo.description = data['description']
        photo.save()
        return redirect('all-photos')
    else:
        pk = request.GET['pk']
        photo = Photo.objects.get(id=int(pk))
        context['photos'] = photo
        context['pk_id'] = int(pk)
    return render(request, 'edite-photo.html', context)
