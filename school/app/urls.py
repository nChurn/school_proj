from django.urls import path
from .views import *


app_name = 'app'
urlpatterns = [
    path('', main, name='main_page'),
    # path('partners', partners, name='partners'),
    # path('partners/<int:id>', partner, name='partner'),
    path('projects', projects, name='projects'),
    path('projects/<int:id>', project, name='project'),

    path('projects/english', eng, name='eng'),
    path('projects/russian', rus, name='rus'),
    path('projects/math', math, name='math'),
    path('projects/physics', phys, name='phys'),
    path('projects/social_science', soc, name='soc'),
    path('projects/biology', bio, name='bio'),
    path('projects/literature', lit, name='lit'),
    path('projects/history', hist, name='hist'),
    path('projects/informatics', inf, name='inf'),
    path('projects/geography', geo, name='geo'),
    path('projects/chemistry', chem, name='chem'),
]