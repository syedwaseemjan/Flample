# -*- coding: utf-8 -*-
"""
    tests.frontend
    ~~~~~~~~~~~~~~

    frontend tests package
"""

from flample.frontend import create_app

from .. import FlampleAppTestCase, settings


class FlampleFrontendTestCase(FlampleAppTestCase):
    def _create_app(self):
        return create_app(settings)

    def setUp(self):
        super(FlampleFrontendTestCase, self).setUp()
        self._login()
