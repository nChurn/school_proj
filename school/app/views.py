from django.shortcuts import render
from .models import Project
# Create your views here.



def main(request):
    _projects = Project.objects.all()
    projects = []
    for project in _projects:
        projects.append([project, project.get_all_images()])
    
    return render(request, 'main.html', {'projects': projects})


# def partners(request):
#     _partners = Partner.objects.all()
#     partners = []
#     for partner in _partners:
#         partners.append([partner, partner.get_all_images()])
    
#     return render(request, 'partners.html', {'partners': partners})

# def partner(request, id):
#     _partner = Partner.objects.get(id=id)
#     partner = [_partner, _partner.get_all_images()]
#     return render(request, 'partner.html', {'partner': partner}) 

def projects(request):
    _projects = Project.objects.all()
    projects = []
    for project in _projects:
        projects.append([project, project.get_all_images()])

    return render(request, 'projects.html', {'projects': projects})

def project(request, id):
    _project = Project.objects.get(id=id)
    project = [_project, _project.get_all_images()]
    return render(request, 'project.html', {'project': project})


def eng(request):
    _projects = Project.objects.filter(subject='ENG')
    projects = []
    for project in _projects:
        projects.append([project, project.get_all_images()])
    return render(request, 'subjects/eng.html', {'projects': projects})

def rus(request):
    _projects = Project.objects.filter(subject='RUS')
    projects = []
    for project in _projects:
        projects.append([project, project.get_all_images()])
    return render(request, 'subjects/rus.html', {'projects': projects})
    
def math(request):
    _projects = Project.objects.filter(subject="MATH")
    projects = []
    for project in _projects:
        projects.append([project, project.get_all_images()])
    return render(request, 'subjects/math.html', {'projects': projects})

def phys(request):
    _projects = Project.objects.filter(subject="SOC")
    projects = []
    for project in _projects:
        projects.append([project, project.get_all_images()])
    return render(request, 'subjects/phys.html', {'projects': projects})

def soc(request):
    _projects = Project.objects.filter(subject="BIO")
    projects = []
    for project in _projects:
        projects.append([project, project.get_all_images()])
    return render(request, 'subjects/soc.html', {'projects': projects})

def bio(request):
    _projects = Project.objects.filter(subject="BIO")
    projects = []
    for project in _projects:
        projects.append([project, project.get_all_images()])

    return render(request, 'subjects/bio.html', {'projects': projects})

def lit(request):
    _projects = Project.objects.filter(subject="LIT")
    projects = []
    for project in _projects:
        projects.append([project, project.get_all_images()])

    return render(request, 'subjects/lit.html', {'projects': projects})

def hist(request):
    _projects = Project.objects.filter(subject="HIST")
    projects = []
    for project in _projects:
        projects.append([project, project.get_all_images()])

    return render(request, 'subjects/hist.html', {'projects': projects})

def inf(request):
    _projects = Project.objects.filter(subject="INF")
    projects = []
    for project in _projects:
        projects.append([project, project.get_all_images()])

    return render(request, 'subjects/inf.html', {'projects': projects})

def geo(request):
    _projects = Project.objects.filter(subject="GEO")
    projects = []
    for project in _projects:
        projects.append([project, project.get_all_images()])

    return render(request, 'subjects/geo.html', {'projects': projects})

def chem(request):
    _projects = Project.objects.filter(subject="CHEM")
    projects = []
    for project in _projects:
        projects.append([project, project.get_all_images()])

    return render(request, 'subjects/chem.html', {'projects': projects})

