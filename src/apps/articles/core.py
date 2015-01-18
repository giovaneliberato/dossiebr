from google.appengine.ext import ndb

from models import Article, ArticleUser, Tag, Mention, BaseTag


def find_or_create_article(url):
    return Article.find_or_create(url)


def associate_user_with_article(user, article):
    ArticleUser(origin=user, destination=article).put()


def list_by_user(user):
    articles = []
    articles_relations = ArticleUser.get_by_user(user)
    for ralation in articles_relations:
        article = ralation.destination.get()
        articles.append(article.to_dict())
    return articles


def user_has_article(user):
    return ArticleUser.find_destinations(user).count() > 0


def tag_article(user, article, tags, mentions):
    to_save = []
    for tag_name in tags:
        tag = Tag.find_by_name(tag_name, user.key, article.key)
        if not tag:
            to_save.append(
                Tag(name=tag_name, origin=user.key, destination=article.key))

    for mention_name in mentions:
        mention = Mention.find_by_name(mention_name, user.key, article.key)
        if not mention:
            to_save.append(
                Mention(name=mention_name, origin=user.key, destination=article.key))

    ndb.put_multi(to_save)


def find_tags_by_prefix(prefix):
    return BaseTag.find_by_prefix(prefix)


def search_articles(search_string):
    tags = find_tags_by_prefix(search_string)
    return [t.destination.get().to_dict() for t in tags]
