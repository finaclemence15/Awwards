from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from . import views

urlpatterns=[
    url('^$',views.welcome,name = 'welcome'),
    url(r'^search/', views.search_project, name='search_project'),
    url(r'^new/title$', views.add_site, name='add_site'),
    url(r'^new/profile/(\d+)', views.profile, name='profile'),
    url(r'^new/edit_profile$', views.edit_profile, name='edit_profile'),
    url(r'^api/projectApi/$', views.ProjectsList.as_view(), name= 'projectApi'),
    url(r'^api/profileApi/$', views.ProfileList.as_view(), name= 'profileApi'),
    url(r'^grade/(\d+)',views.grade_rating,name ='grade')
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)