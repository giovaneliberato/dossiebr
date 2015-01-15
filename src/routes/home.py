# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from config.template_middleware import TemplateResponse
from gaecookie.decorator import no_csrf
from gaepermission.decorator import login_not_required


@no_csrf
@login_not_required
def index(_logged_user):
    if _logged_user:
        return TemplateResponse({}, 'home.html')
    return TemplateResponse({}, 'landing.html')
