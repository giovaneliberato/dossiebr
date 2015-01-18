# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from google.appengine.ext import ndb
from gaegraph.model import Node, Arc


class Feedback(Node):
    text = ndb.TextProperty(required=True)


class FeedbackUser(Arc):
    pass
