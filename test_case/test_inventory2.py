import json
import sys
import time
from time import sleep
from playwright.async_api import Dialog
from seldom.testdata.conversion import json_to_list
from page.inventory_page import InventoryPage
import allure
import pytest
from common.config import *
from playwright.sync_api import Playwright, sync_playwright, expect


@allure.feature('库存页测试')
class TestInventory:
    """    @pytest.mark.parametrize(
        "price, comment",
        [("1", "UI自动化上架demo正确上架数字1"),
         ("0", "UI自动化上架demo-价格为0"),
         ("啊啊啊啊", "UI自动化上架demo-价格框输入文字"),
         ("&&&¥%……&*", "UI自动化上架demo-符号"),
         ("-9", "UI自动化上架demo-负数"),
         ],
        ids=["case1", "case2", "case3", "case4", "case5"]
    )"""

    @allure.story("只卖不租-单个上架")
    def test_grounding_onleysale(self, logged_page):
        # 点击我的库存
        logged_page.locator(InventoryPage.my_inventory).click()
        # 库存加载较慢，设置一个等待时间
        logged_page.wait_for_timeout(10000)
        logged_page.locator(InventoryPage.show_all).click()
        # 点击可出售筛选项
        logged_page.locator(InventoryPage.show_can_sale).click()
        logged_page.wait_for_timeout(5000)
        # 选择商品
        logged_page.locator(InventoryPage.select_goods).click()
        logged_page.wait_for_timeout(5000)
        # 点击上架
        logged_page.locator(InventoryPage.grounding_but).click()
        logged_page.wait_for_timeout(5000)
        # 点击只卖不租
        logged_page.locator(InventoryPage.only_sale).click()
        # 输入价格
        logged_page.locator(InventoryPage.pricing_sale).fill("1")
        # 输入商品描述
        logged_page.locator(InventoryPage.add_comment).fill("UI自动化上架demo正确上架数字1")
        logged_page.wait_for_timeout(1000)
        # 点击确认上架
        logged_page.locator(InventoryPage.confirm_grounding_but).click()
        logged_page.wait_for_timeout(5000)
        # 点击确认，因确认框隐藏无法捕获，此处使用JS点击
        # page.evaluate(InventoryPage.confirm)
        # 对话框处理 监听对话框
        # page.on("dialog", lambda dialog: dialog.accept())

        logged_page.click(InventoryPage.confirm)

        logged_page.wait_for_timeout(5000)
        # 获取弹窗文字
        msg = logged_page.locator(InventoryPage.msg).text_content()
        print(msg)
        # 断言
        assert msg == "上架成功!"

    @allure.story("可租可买-单个上架")
    # 点击我的库存
    def test_grounding(self, logged_page):
        # page.locator(InventoryPage.my_inventory).click()
        # 库存加载较慢，设置一个等待时间
        logged_page.wait_for_timeout(10000)
        # 点击可出售筛选项
        # page.locator(InventoryPage.show_can_sale).click()
        # page.wait_for_timeout(5000)
        # 选择商品
        logged_page.locator(InventoryPage.select_goods).click()
        logged_page.wait_for_timeout(5000)
        # 点击上架
        logged_page.locator(InventoryPage.grounding_but).click()
        logged_page.wait_for_timeout(5000)
        # 点击只卖不租
        # 输入价格
        logged_page.locator(InventoryPage.pricing_sale).fill("2")
        # 输入商品描述
        logged_page.locator(InventoryPage.add_comment).fill("UI自动化上架demo")
        logged_page.wait_for_timeout(1000)
        logged_page.locator(InventoryPage.max_day).fill("8")
        logged_page.wait_for_timeout(1000)
        logged_page.locator(InventoryPage.short_rental).fill("0.01")
        logged_page.wait_for_timeout(1000)
        logged_page.locator(InventoryPage.antecedent_money).fill("2")
        # 点击确认上架
        logged_page.locator(InventoryPage.confirm_grounding_but).click()
        logged_page.wait_for_timeout(5000)
        # 点击确认，因确认框隐藏无法捕获，此处使用JS点击
        # page.evaluate(InventoryPage.confirm)
        # 对话框处理 监听对话框
        # page.on("dialog", lambda dialog: dialog.accept())

        logged_page.click(InventoryPage.confirm)

        logged_page.wait_for_timeout(5000)
        # 获取弹窗文字
        msg = logged_page.locator(InventoryPage.msg).text_content()
        print(msg)
        # 断言
        assert msg == "上架成功!"
