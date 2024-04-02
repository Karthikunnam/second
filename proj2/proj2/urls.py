"""
URL configuration for proj2 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from one.views import test_view
from one.views import continuepage
from one.views import montlypass
from one.views import submit_form

urlpatterns = [
    path('admin/', admin.site.urls),
    path('karthik', test_view),
    path('unnam',continuepage),
    path('bhaskar',montlypass),
    path('nagolu/',submit_form)

]
