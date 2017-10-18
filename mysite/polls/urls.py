
from django.conf.urls import url
from . import views

app_name = 'polls'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
    url(r'^patient/$', views.patient, name='patient'),
    url(r'^patient/data$', views.patientdata, name='patientdata'),
    url(r'^patientlog/$', views.patientlog, name='patientlog'),
    url(r'^doctor/$', views.doctor, name='doctor'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^login/$', views.login, name='login'),
    url(r'^cleardb/$', views.cleardb, name='cleardb'),
]