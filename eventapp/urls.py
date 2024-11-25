from django.contrib import admin
# from django.urls import path
# from . import views as user_views
# from django.contrib.auth import views as auth_views
from django.urls import path
from . import views


urlpatterns = [
     path('admin/', admin.site.urls),
    path('', views.index, name='home-page'),
    # path('add_event/', user_views.add_event, name='add-event-page'),
    # path('events/', user_views.events, name='my-events'),
    # path('delete_event/<id>/', user_views.delete_event, name='del-event'),
    # path('update_event/<id>/', user_views.update_event, name='update-event'),
    # path('add_participant/', user_views.add_participant, name='add-participant-page'),
    # path('participants/', user_views.participants, name='participants-page'),
    # path('delete_participant/<id>/', user_views.delete_participant, name='del-participant'),
    # path('update_participant/<id>/', user_views.update_participant, name='update-participant'),
    # path('login/', auth_views.LoginView.as_view(template_name='delete_participant.html'), name='user-login'),
    # path('register/', user_views.register, name='user-registration'),

    # Event URLs
    path('events/', views.event_list, name='event-list'),
    path('events/create/', views.create_event, name='create-event'),
    path('events/update/<int:event_id>/', views.update_event, name='update-event'),
    # path('events-update/<event_id>/', views.update_event, name='update-event'),
    path('events/delete/<int:event_id>/', views.delete_event, name='delete-event'),

    # Participant URLs
    path('participants/', views.participant_list, name='participant-list'),
    path('participants/create/', views.create_participant, name='create-participant'),
    path('participants/update/<int:participant_id>/', views.update_participant, name='update-participant'),
    path('participants/delete/<int:participant_id>/', views.delete_participant, name='delete-participant'),
]


