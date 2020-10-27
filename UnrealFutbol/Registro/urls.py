from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
<<<<<<< HEAD
    path('usuario/<int:pk>', views.UsuarioDetailView.as_view(), name='usuario-detail'),
]

urlpatterns+=[
    path('usuario/create/', views.UsuarioCreate.as_view(), name='usuario_create'),
    path('usuario/<int:pk>/update/', views.UsuarioUpdate.as_view(), name='usuario_update'),
    path('usuario/<int:pk>/delete/', views.UsuarioDelete.as_view(), name='usuario_delete'),
    

=======
>>>>>>> f0a3373852944327dde91fd3c481cbd19cc5a3a0
]
