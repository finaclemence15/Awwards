from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from . import views

urlpatterns=[
    url('^$',views.welcome,name = 'welcome'),
    url(r'^search/', views.search_project, name='search_project'),
    url(r'^new/title$', views.add_site, name='add_site'),
    url(r'^new/profile/(\d+)', views.profile, name='profile'),
    url(r'^myaccount/',views.myaccount,name = 'myaccount'),
    url(r'^new/edit_profile$', views.edit_profile, name='edit_profile'),
    url(r'^api/project/$', views.ProjectsList.as_view(), name= 'project'),
    url(r'^api/profile/$', views.ProfileList.as_view(), name= 'profile')
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)