from models import Article, ArticleUser


def get_or_create_article(url):
    return Article.get_or_create(url)


def associate_user_with_article(user, article):
    ArticleUser(origin=user, destination=article).put()


def list_by_user(user):
    return [a.destination.get().url for a in ArticleUser.get_by_user(user)]


def user_has_article(user):
    return ArticleUser.find_destinations(user).count() > 0
