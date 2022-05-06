"""
    tests.api.user_tests
    ~~~~~~~~~~~~~~~~~~~~

    api user tests module
"""

from . import FlampleFrontendTestCase


class DashboardTestCase(FlampleFrontendTestCase):
    def test_authenticated_dashboard_access(self):
        r = self.get("/")
        self.assertOk(r)
        self.assertIn(b"section search", r.data)

    def test_unauthenticated_dashboard_access(self):
        self.get("/logout")
        r = self.get("/")
        self.assertOk(r)
        self.assertNotIn(b"section search", r.data)
