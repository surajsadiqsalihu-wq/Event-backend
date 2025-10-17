from django.urls import path

from . import views


# urlpatterns = [
#     path('', views.event_list_create_view),
#     path('<int:pk>/update/', views.event_update_view),
#     path('<int:pk>/delete/', views.event_destroy_view),
#     path('<int:pk>/', views.event_detail_view),
#     path('register/', views.RegisterView.as_view(), name='register'),
#     path('public-events/', views.PublicEventListView.as_view(), name='public-events'),
# ]

urlpatterns = [
    path('', views.EventListCreateAPIView.as_view(), name='event-list-create'),
    path('<int:pk>/', views.EventDetailAPIView.as_view(), name='event-detail'),
    path('<int:pk>/update/', views.EventUpdateAPIView.as_view(), name='event-update'),
    path('<int:pk>/delete/', views.EventDestroyAPIView.as_view(), name='event-delete'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('public-events/', views.PublicEventListView.as_view(), name='public-events'),
]