from project.web.api import create_app
from werkzeug.test import Headers, Client
from .. import ProjectAppTestCase, settings


class ProjectApiTestCase(ProjectAppTestCase):

    def _create_app(self):
        return create_app(settings, register_security_blueprint=True)

    def setUp(self):
        super(ProjectApiTestCase, self).setUp()
        self.token = self._login()

    def send_request(self, enpoint):
        h = Headers()
        h.add('Authorization', 'Bearer {}'.format(self.token))
        return Client.open(self.client, path=enpoint, headers=h)
