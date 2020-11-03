#!/usr/bin/env python
# -*- coding:utf-8 -*-
import unittest

from tests.common.BrowserDriver import BrowserDriver


class Model(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        driver = BrowserDriver(cls)
        cls.driver = driver.open_browser(cls)

    def setUp(self):
        pass

    def teardown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
