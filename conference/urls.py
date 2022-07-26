from django.urls import path
from conference import views

urlpatterns = [
    path('all', views.conferences, name='conferences'),
    # localhost:8000/conference/python
    # localhost:8000/conference/software-development
    path('<int:id>', views.conference_detail, name="conference-detail"),
    path('<int:id>/register', views.conference_registration, name="conf-register"),
    # localhost:8000/conference/software-development/register
    # path('<slug:name>/register', views.conference_registration),
    # path('<int:year>', views.yearly_conferences)
    path('add', views.add_conf, name='add-conference'),
]