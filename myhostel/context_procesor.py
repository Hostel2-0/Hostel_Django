from .models import Towns

def menu_links(request):
    links = Towns.objects.all()
    return dict(links=links)