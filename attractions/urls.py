from django.urls import path
from attractions import views
from rest_framework.urlpatterns import format_suffix_patterns
from django.conf.urls import include

urlpatterns = [
    path('', views.AttractionsList.as_view()),  # List of attractions
    path('<int:pk>/', views.AttractionsDetail.as_view()),  # Detail view of a specific attraction
]

urlpatterns = format_suffix_patterns(urlpatterns)

urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),
]
