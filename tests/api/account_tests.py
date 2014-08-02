from . import ProjectApiTestCase

class AccountApiTestCase(ProjectApiTestCase):

    def test_get_current_account(self):
        r = self.send_request('/accounts/current')
        self.assertOkJson(r)

    def test_get_user(self):
        r = self.send_request('/accounts/{}'.format(self.account.id))
        self.assertOkJson(r)