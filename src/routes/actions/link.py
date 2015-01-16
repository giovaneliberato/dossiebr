from tekton.gae.middleware.json_middleware import JsonResponse

from articles import core


def save(_logged_user, link, tags=None):
    article = core.get_or_create_article(link)
    return JsonResponse('')
