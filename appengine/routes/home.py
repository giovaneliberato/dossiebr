# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from config.template_middleware import TemplateResponse
from gaecookie.decorator import no_csrf
from gaepermission.decorator import login_not_required


@no_csrf
@login_not_required
def index():
    return TemplateResponse({}, 'home.html')
