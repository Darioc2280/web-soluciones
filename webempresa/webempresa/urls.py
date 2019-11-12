"""webempresa URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings

urlpatterns = [
    # Paths del core
    path('', include('core.urls')),
    # Paths del admin
    path('admin/', admin.site.urls),
    #path del solutions
    path('solution/', include('solution.urls')),

     #Paths de services
     path('****kjsdljasdkjs********kdslkjldskjf*12121215466541*165aldjlskjdas****/', include('services.urls')),
     #Paths de blog
    path('****kjsdljasdkjs********kdslkjldskjf*12121215466541*165aldjlskjdas****/', include('blog.urls')),
     #Paths de pages
    path('****kjsdljasdkjs********kdslkjldskjf*12121215466541*165aldjlskjdas****/', include('pages.urls')),
     #Paths de pages
    path('****kjsdljasdkjs********kdslkjldskjf*12121215466541*165aldjlskjdas****/', include('contact.urls')),

]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
