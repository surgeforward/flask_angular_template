from ...core import  Service
from .models import Account, Role


class AccountsService(Service):
    __model__ = Account

class RolesService(Service):
    __model__ = Role

