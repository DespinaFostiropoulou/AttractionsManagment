from django.urls import path
from attractions import views
from rest_framework.urlpatterns import format_suffix_patterns
from django.conf.urls import include

urlpatterns = [
    path('attractions/', views.AttractionsList.as_view()),  # For listing snippets and creating new snippets
    path('attractions/<int:pk>/', views.AttractionsDetail.as_view()),
    # For retrieving, updating, or deleting individual snippets
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)

urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),
]
