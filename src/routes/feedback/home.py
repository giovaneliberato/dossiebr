# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from config.template_middleware import TemplateResponse
from gaecookie.decorator import no_csrf
from feedback.models import Feedback, FeedbackUser
from tekton.gae.middleware.redirect import RedirectResponse


@no_csrf
def index(_logged_user):
    return TemplateResponse({}, 'feedback.html')


def enviar(_logged_user, text):
    feedback = Feedback(text=text).put()
    FeedbackUser(origin=_logged_user, destination=feedback).put()
    return RedirectResponse('/')
