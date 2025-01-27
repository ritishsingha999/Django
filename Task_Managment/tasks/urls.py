from django.urls import path
from .views import show_task, show_specific_task
# from tasks.views import showTask
urlpatterns=[
    
    path('show_task/', show_task),
    path('show_task/<int:id>/',show_specific_task)
    # path('home/', views.home),
    # path('about/', views.about),
    # path('contact/', views.contact),
    # path('admin/', admin.site.urls),
    # path('', views.home),  # Redirect to home page if no path specified
    # path('tasks/', include('tasks.urls')),  # Include tasks app's URL patterns
    # path('accounts/', include('accounts.urls')),  # Include accounts app's URL patterns
    # path('accounts/profile/', views.profile),  # Profile view for logged-in users
    # path('accounts/logout/', auth_views.LogoutView.as_view(next_page='/')),  # Logout view for logged-in users
    # path('accounts/register/', views.register),  # Registration view for new users
    # path('accounts/activate/<uidb64>/<token>/', views.activate, name='activate'),  # Activation view for new users
]