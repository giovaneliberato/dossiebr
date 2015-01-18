# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from google.appengine.ext import ndb
from gaegraph.model import Node, Arc


class Article(Node):
    url = ndb.StringProperty(required=True)

    @classmethod
    def get_by_url(cls, url):
        return cls.query(cls.url == url).get()

    @classmethod
    def find_or_create(cls, url):
        article = cls.get_by_url(url)
        if not article:
            article = cls(url=url)
            article.put()
        return article

    def find_tags(self):
        return Tag.find_origins(self)

    def find_mentions(self):
        return Mention.find_origins(self)

    def to_dict(self):
        tags = [t.name for t in self.find_tags()]
        mentions = [m.name for m in self.find_mentions()]
        return {
            'url': self.url,
            'tags': tags,
            'mentions': mentions
        }


class BaseTag(Arc):
    name = ndb.StringProperty(required=True)

    @classmethod
    def find_by_name(cls, name, origin, destination):
        return cls.query(cls.name == name,
                         cls.origin == origin,
                         cls.destination == destination).get()

    @classmethod
    def find_by_article(cls, article_key):
        return cls.find_destinations(article_key)

    @classmethod
    def find_by_prefix(cls, prefix):
        return cls.query().filter(cls.name >= prefix, cls.name < prefix + u'\ufffd')


class Tag(BaseTag):
    pass


class Mention(BaseTag):
    pass


class ArticleUser(Arc):
    @classmethod
    def default_order(cls):
        return -cls.creation

    @classmethod
    def get_by_user(cls, user, limit_by=1000):
        return cls.find_destinations(user).fetch(limit_by)
