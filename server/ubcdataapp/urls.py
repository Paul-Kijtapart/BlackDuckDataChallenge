from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^projects$', views.projects, name="projects"),
    url(r'^versions$', views.versions, name="versions"),
    url(r'^licenses$', views.licenses, name="licenses")
]
