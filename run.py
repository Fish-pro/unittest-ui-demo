#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os
import time
import unittest
import sys

from report.HTMLTestRunner3 import HTMLTestRunner

sys.path.append("../")


def create_suite():
    test_suite = unittest.TestSuite()  # 测试集
    test_dir = "tests/testcase"

    discover = unittest.defaultTestLoader.discover(start_dir=test_dir)

    for test_case in discover:
        test_suite.addTests(test_case)
    return test_suite


def report():
    now = time.strftime("%Y-%m-%d_%H_%M_%S_")
    report_name = os.getcwd() + "/report/" + now + "result.html"
    print(report_name)
    return report_name


if __name__ == "__main__":
    test_suite = create_suite()
    fp = open(report(), "wb")
    runner = HTMLTestRunner(stream=fp, title="测试报告", description="测试用例执行情况")
    runner.run(test_suite)
    fp.close()
