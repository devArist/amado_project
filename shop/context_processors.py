from shop import models as shop_models

def data(request):
    categories = shop_models.Category.objects.filter(status=True)

    return locals()