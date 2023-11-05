from django.urls import path

from tracker.views import index, about, show_post, addtask, login, contact, registration

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('post/<int:post_id>/', show_post, name='post'),
    path('addtask/', addtask, name='add_task'),
    path('login/', login, name='login'),
    path('registration/', registration, name='registration'),
    path('contact/', contact, name='contact'),
]


