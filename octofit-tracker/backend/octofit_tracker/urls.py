"""octofit_tracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.http import JsonResponse, HttpResponseRedirect
import os
from rest_framework import routers
from .api import ActivityViewSet, LeaderboardViewSet, TeamViewSet, UserViewSet, WorkoutViewSet

def root_redirect(request):
    return HttpResponseRedirect('/api/')

def api_root(request):
    codespace_name = os.environ.get('CODESPACE_NAME', 'localhost')
    base_url = f"https://{codespace_name}-8000.app.github.dev" if codespace_name != 'localhost' else "http://localhost:8000"
    return JsonResponse({
        'activities': f"{base_url}/api/activities/",
        'users': f"{base_url}/api/users/",
        'teams': f"{base_url}/api/teams/",
        'leaderboard': f"{base_url}/api/leaderboard/",
        'workouts': f"{base_url}/api/workouts/",
    })

router = routers.DefaultRouter()
router.register(r'activities', ActivityViewSet, basename='activity')
router.register(r'leaderboard', LeaderboardViewSet, basename='leaderboard')
router.register(r'teams', TeamViewSet, basename='team')
router.register(r'users', UserViewSet, basename='user')
router.register(r'workouts', WorkoutViewSet, basename='workout')

urlpatterns = [
    path('', root_redirect),
    path('admin/', admin.site.urls),
    path('api/root/', api_root),
    path('api/', include(router.urls)),
]
