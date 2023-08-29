from .models import Profile, skill
from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

def paginateProfile(request, profiles, result):
    
    page = request.GET.get('page')
    paginator = Paginator(profiles, result)

    try:
        profiles = paginator.page(page)

    except PageNotAnInteger:
        page = 1
        profiles = paginator.page(page)

    except EmptyPage:
        page = paginator.num_pages
        profiles = paginator.page(page)

    leftindex = (int(page) - 1)

    if leftindex < 1:
        leftindex = 1

    rightindex = (int(page) + 2)

    if rightindex > paginator.num_pages:
        rightindex = paginator.num_pages + 1

    custom_range = range(leftindex, rightindex)

    return custom_range, profiles


def searchProfile(request):

    search_query = ''

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

    skills = skill.objects.filter(name__icontains=search_query)

    profiles = Profile.objects.distinct().filter(
        Q(name__icontains=search_query) | 
        Q(short_intro__icontains=search_query) |
        Q(skill__in = skills))
    return profiles, search_query