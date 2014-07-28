from ...core import db
from .. import ResourceMixin
from ...helpers import JsonSerializer


roles_accounts = db.Table(
    'roles_accounts',
    db.Column('account_id', db.Integer(), db.ForeignKey('accounts.id')),
    db.Column('role_id', db.Integer(), db.ForeignKey('roles.id')))


class Role(ResourceMixin, db.Model):
    __tablename__ = 'roles'

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True, index=True)
    description = db.Column(db.String(255))

    def __eq__(self, other):
        return (self.name == other or
                self.name == getattr(other, 'name', None))

    def __ne__(self, other):
        return (self.name != other and
                self.name != getattr(other, 'name', None))


class AccountJsonSerializer(JsonSerializer):
    __json_public__ = ['id', 'email']


class Account(AccountJsonSerializer, ResourceMixin, db.Model):
    __tablename__ = 'accounts'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True, index=True)
    password = db.Column(db.String(255))
    active = db.Column(db.Boolean())

    roles = db.relationship('Role', secondary=roles_accounts,
                            backref=db.backref('users', lazy='dynamic'))

