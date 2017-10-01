from django.conf.urls import url,include
from django.contrib import admin
from polls import views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^polls/', include('polls.urls')),
]
