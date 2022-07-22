from django.urls import path
from conference import views

urlpatterns = [
    path('all', views.conferences, name='conferences'),
    # localhost:8000/conference/python
    # localhost:8000/conference/software-development
    path('<slug:name>', views.conference_detail),
    # localhost:8000/conference/software-development/register
    path('<slug:name>/register', views.conference_registration),
    # path('<int:year>', views.yearly_conferences)
]