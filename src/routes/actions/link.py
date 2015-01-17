from tekton.gae.middleware.json_middleware import JsonResponse

from articles import facade


def save(_logged_user, link, tags=None):
    article = facade.get_or_create_article(link)
    facade.associate_user_with_article(_logged_user, article)
    return JsonResponse('')
