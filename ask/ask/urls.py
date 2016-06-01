"""ask URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import login, logout
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from qa import views as qa_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login/', login, {'template_name': 'qa/login.html'}),
    url(r'^logout/', logout, {'next_page': '/'}),
    url(r'^signup/', qa_views.signup),
    url(r'^settings',qa_views.settings_profile),
    url(r'^question/(?P<pk>(\d+))/$', qa_views.question_detail),
    url(r'^question/(?P<question_id>(\d+))/(?P<answer_id>(\d+))/correct$', qa_views.correct_answer),
    url(r'^ask/', qa_views.question_add),
    url(r'^answer/', qa_views.answer_add),
    url(r'^new/', qa_views.questions_list),
    url(r'^like/$',qa_views.like),
    url(r'^$', qa_views.popular_questions),
]

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns() + static (settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
