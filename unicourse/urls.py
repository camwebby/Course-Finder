from django.conf.urls import url
from django.contrib import admin
from juan import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home, name='home'),
    url(r'^home', views.home, name='home'),
    url(r'^course/(\d+)/', views.course_detail, name="course_detail"),
]
