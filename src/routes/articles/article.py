from tekton.gae.middleware.json_middleware import JsonResponse

from articles import core


def save(_logged_user, url, tags=None):
    mentions = [tag for tag in tags if tag.startswith('@')]
    tags = [tag for tag in tags if tag.startswith('#')]
    article = core.find_or_create_article(url)
    core.tag_article(article, tags, mentions)
    core.associate_user_with_article(_logged_user, article)
    return JsonResponse('')


def list(_logged_user):
    articles = core.list_by_user(_logged_user)
    return JsonResponse({'articles': articles})
