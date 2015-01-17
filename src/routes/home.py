# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from config.template_middleware import TemplateResponse
from gaecookie.decorator import no_csrf
from gaepermission.decorator import login_not_required

from articles import facade


@no_csrf
@login_not_required
def index(_logged_user):
    if _logged_user:
        context = {
            'has_article': facade.user_has_article(_logged_user)
        }
        return TemplateResponse(context, 'home.html')
    return TemplateResponse({}, 'landing.html')
