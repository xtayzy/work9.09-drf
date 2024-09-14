from django.urls import path

from test_drf import views

urlpatterns = [
    path('models/', views.ModelListView.as_view()),
    path('models/<int:pk>/', views.ModelDetailView.as_view()),
    path('models/create/', views.ModelCreateView.as_view()),
    path('models/update/<int:pk>/', views.ModelUpdateView.as_view()),
    path('models/delete/<int:pk>/', views.ModelDeleteView.as_view())
]

