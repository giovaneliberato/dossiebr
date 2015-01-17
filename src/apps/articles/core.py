from google.appengine.ext import ndb

from models import Article, ArticleUser, Tag, Mention, ArticleTag, ArticleMention


def find_or_create_article(url):
    return Article.find_or_create(url)


def associate_user_with_article(user, article):
    ArticleUser(origin=user, destination=article).put()


def list_by_user(user):
    return [a.destination.get().url for a in ArticleUser.get_by_user(user)]


def user_has_article(user):
    return ArticleUser.find_destinations(user).count() > 0


def tag_article(article, tags, mentions):
    to_save = []
    for tag_name in tags:
        tag = Tag.find_or_create(tag_name)
        to_save.append(ArticleTag(origin=tag, destination=article))

    for mention_name in mentions:
        mention = Mention.find_or_create(mention_name)
        to_save.append(ArticleMention(origin=mention, destination=article))

    ndb.put_multi(to_save)


def find_tags_by_prefix(prefix):
    return Tag.find_by_prefix(prefix)
