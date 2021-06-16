from django.urls import path, include
from rasmapp.views import *
urlpatterns = [
    path('', allPhotos, name='all-photos'),
    path('add', addPhoto, name='add-photo'),
    path('photo', seePhoto, name='see-photo'),
    path('delete', deletePhoto, name='delete-photo'),
    path('edite', editePhoto, name='edite-photo'),

]
