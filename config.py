import os
from common.config import *

"""
运行测试配置
"""


class RunConfig:
    # 运行测试用例的目录或文件
    # cases_path = os.path.join(case_path, "test_case")
    cases_path = os.path.join(case_path)
    #

    # 配置浏览器驱动类型(chromium, firefox, webkit)。
    browser = "chromium"

    # 运行模式（headless, headful）
    # mode = "headless"
    mode = "headful"

    # 配置运行的 URL
    baseUrl = "https://testwww.youpin898.com/"
    baseUrl_baidu = "https://www.baidu.com"

    # 失败重跑次数
    rerun = "0"

    # 当达到最大失败数，停止执行
    max_fail = "5"

    # 报告路径（不需要修改）
    NEW_REPORT = None
