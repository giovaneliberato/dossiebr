# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from google.appengine.ext import ndb
from gaegraph.model import Node


class Article(Node):
    link = ndb.StringProperty(required=True)

    @classmethod
    def get_by_link(cls, link):
        return cls.query(link=link)


class Tag(Node):
    name = ndb.StringProperty(required=True)
