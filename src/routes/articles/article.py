from tekton.gae.middleware.json_middleware import JsonResponse

from articles import facade


def save(_logged_user, url, tags=None):
    article = facade.get_or_create_article(url)
    facade.associate_user_with_article(_logged_user, article)
    return JsonResponse('')


def list(_logged_user):
    articles = facade.list_by_user(_logged_user)
    return JsonResponse({'articles': articles})
