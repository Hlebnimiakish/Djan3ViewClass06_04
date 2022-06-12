from django.urls import path
from ViewClass.views import FormView

urlpatterns = [
    path('form/get/', FormView.as_view(), name='formpageget'),
    path('form/post/', FormView.as_view(), name='formpagepost'),
]