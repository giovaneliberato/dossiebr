from models import Article, ArticleUser


def get_or_create_article(link):
    return Article.get_or_create(link)


def list_by_user(user):
    return ArticleUser.get_by_user(user)


def user_has_article(user):
    return ArticleUser.find_destinations(user).count() > 0
