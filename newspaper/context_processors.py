from newspaper import models


def category_processor(request):
    categories = models.Category.objects.all()
    return {'categories': categories}