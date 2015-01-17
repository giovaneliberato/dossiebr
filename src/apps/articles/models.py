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
    def get_or_create(cls, url):
        article = cls.get_by_url(url)
        if not article:
            article = cls(url=url)
            article.put()
        return article


class Tag(Node):
    name = ndb.StringProperty(required=True)


class ArticleUser(Arc):
    @classmethod
    def get_by_user(cls, user, limit_by=20):
        return cls.find_destinations(user).fetch(limit_by)
