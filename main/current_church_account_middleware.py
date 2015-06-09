from django.db.models import signals
from django.utils.functional import curry
from main.models import AccountedManager


class WhodidMiddleware(object):
    def process_request(self, request):
        if not request.method in ('GET', 'HEAD', 'OPTIONS', 'TRACE'):
            if hasattr(request, 'user') and request.user.is_authenticated():
                user = request.user
            else:
                user = None
 
            mark_whodid = curry(self.mark_current_church_account, user)
            signals.pre_save.connect(mark_whodid,  dispatch_uid=(self.__class__, request,), weak = False)
 
    def process_response(self, request, response):
        signals.pre_save.disconnect(dispatch_uid =  (self.__class__, request,))
        return response
 
    def mark_current_church_account(self, user, sender, instance, **kwargs):
        if hasattr(instance, 'church_account_id') and isinstance(instance._default_manager, AccountedManager):
            instance.church_account = user.userprofile.church_account
