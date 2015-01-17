from tekton.gae.middleware.json_middleware import JsonResponse

from articles import facade


def save(_logged_user, url, tags=None):
    tags = [tag for tag in tags if tag.startswith('#')]
    mentions = [tag for tag in tags if tag.startswith('@')]
    article = facade.get_or_create_article(url)
    facade.tag_article(article, tags, mentions)
    facade.associate_user_with_article(_logged_user, article)
    return JsonResponse('')


def list(_logged_user):
    articles = facade.list_by_user(_logged_user)
    return JsonResponse({'articles': articles})
