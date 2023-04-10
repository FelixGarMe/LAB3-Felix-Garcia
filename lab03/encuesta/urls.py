from django.urls import path
from django.urls import include, path
from . import views

app_name = 'encuesta'


urlpatterns = [
    path('encuesta/', include('encuesta.urls')),
    path('admin/', admin.site.urls),

    #path('', views.index,name='index'),
    #path('<int:pregunta_id>/',views.detalle,name='detalle'),
    #path('<int:pregunta_id>/votar',views.votar,name='votar')

]
