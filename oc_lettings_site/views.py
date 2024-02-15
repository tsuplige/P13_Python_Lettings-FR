from django.shortcuts import render

# Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque molestie
# quam lobortis leo consectetur ullamcorper non id est. Praesent dictum, nulla
# eget feugiat sagittis, sem mi convallis eros,
# vitae dapibus nisi lorem dapibus sem. Maecenas pharetra purus ipsum, eget
# consequat ipsum lobortis quis. Phasellus eleifend ex auctor venenatis tempus.
# Aliquam vitae erat ac orci placerat luctus. Nullam elementum urna nisi,
# pellentesque iaculis enim cursus in. Praesent volutpat porttitor magna, non
# finibus neque cursus id.


def index(request):
    """Vue permettant d'accéder a la page index du site

    Args:
        request (request): requete passé par l'url

    Returns:
       template: retourne le template index.html
    """
    return render(request, 'index.html')


def error_404(request, exception):
    """Vue permettant d'accéder a la page custom 404

    Args:
        request (request): requete passé par l'url
        exception (exeption): exception ayant causé le 404

    Returns:
       template: retourne le template 404.html
    """

    return render(request, '404.html', status=404)


def error_500(request):
    """Vue permettant d'accéder a la page custom 500

    Args:
        request (request): requete passé par l'url
        exception (exeption): exception ayant causé le 500

    Returns:
       template: retourne le template 500.html
    """
    return render(request, '500.html', status=500)
