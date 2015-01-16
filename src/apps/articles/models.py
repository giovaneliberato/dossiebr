# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from google.appengine.ext import ndb
from gaegraph.model import Node, Arc


class Article(Node):
    link = ndb.StringProperty(required=True)

    @classmethod
    def get_by_link(cls, link):
        return cls.query(cls.link == link).get()

    @classmethod
    def get_or_create(cls, link):
        article = cls.get_by_link(link)
        if not article:
            article = cls(link=link)
            article.put()
        return article


class Tag(Node):
    name = ndb.StringProperty(required=True)


class ArticleUser(Arc):
    @classmethod
    def get_by_user(cls, user, limit_by=20):
        return cls.find_destination(user).fetch(limit_by)
