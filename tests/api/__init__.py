# -*- coding: utf-8 -*-
"""
    tests.api
    ~~~~~~~~~

    api tests package
"""

from flample.api import create_app

from .. import FlampleAppTestCase, settings


class FlampleApiTestCase(FlampleAppTestCase):
    def _create_app(self):
        return create_app(settings, register_security_blueprint=True)

    def setUp(self):
        super(FlampleApiTestCase, self).setUp()
        self._login()
