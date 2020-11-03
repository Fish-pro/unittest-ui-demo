#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys

from tests.page.BaiduPage import BaiduPage
from tests.testcase.case_modle import *

sys.path.append("../")


class BaiduCase(Model):
    def test_baidu1(self):
        baidu = BaiduPage(self.driver)
        baidu.input_baidu_text("selenium")
        baidu.click_baidu_btn()
        baidu.get_screent_img("baidu")
        self.assertIn("selenium", self.driver.title)
