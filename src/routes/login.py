from gaepermission.facade import login_google
from gaepermission.decorator import login_not_required
from gaecookie.decorator import no_csrf
from google.appengine.api import users
from tekton.gae.middleware.redirect import RedirectResponse


@no_csrf
@login_not_required
def google(_resp, ret_path='/'):
    user = users.get_current_user()
    if user:
        login_google(user, _resp).execute()
        return RedirectResponse(ret_path)

    return RedirectResponse(
        users.create_login_url("/login/google"), ret_path=ret_path)
