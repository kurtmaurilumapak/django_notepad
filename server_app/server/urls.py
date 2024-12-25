from django.urls import path
from .views import RegisterView, AddNoteView, UserDataView, FetchNotesView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('token/', TokenObtainPairView.as_view(), name='login'),  # JWT Token endpoint
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('add-note/', AddNoteView.as_view(), name='add_note'),
    path('user-data/', UserDataView.as_view(), name='user_data'),
    path('fetch-notes/', FetchNotesView.as_view(), name='fetch_notes'),
]
