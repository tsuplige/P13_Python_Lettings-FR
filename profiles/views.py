from django.shortcuts import render, get_object_or_404
from .models import Profile

# Sed placerat quam in pulvinar commodo. Nullam laoreet consectetur ex,
# sed consequat libero pulvinar eget. Fusc faucibus, urna quis auctor pharetra,
# massa dolor cursus neque, quis dictum lacus d


def index(request):
    """Vue permettant d'accéder a la page index de profile

    Args:
        request (request): requete passé par l'url

    Returns:
       template: retourne le template profiles/index.html
    """
    profiles_list = Profile.objects.all()
    context = {'profiles_list': profiles_list}
    return render(request, 'profiles/index.html', context)

# Aliquam sed metus eget nisi tincidunt ornare accumsan eget lac
# laoreet neque quis, pellentesque dui. Nullam facilisis pharetra vulputate.
# Sed tincidunt, dolor id facilisis fringilla, eros leo tristique lacus,
# it. Nam aliquam dignissim congue. Pellentesque habitant morbi tristiqu
# senectus et netus et males


def profile(request, username):
    """Vue pour afficher le détail d'un profile

    Args:
        request (request): requete passé par l'url
        username (int): username de l'objet profile a charger

    Returns:
         template: retourne le template profiles/profile.html
         avec les donné correspondant a l'objet profile
    """
    profile = get_object_or_404(Profile, user__username=username)
    context = {'profile': profile}
    return render(request, 'profiles/profile.html', context)
