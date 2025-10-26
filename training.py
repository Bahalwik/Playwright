import os
import time
import re
from playwright.sync_api import Playwright, sync_playwright
import pytest


# @pytest.fixture()
# def browser_fixture():
#     with sync_playwright() as playwright:
#         browser = playwright.chromium.launch(headless=True)
#         context = browser.new_context()
#         page = context.new_page()
#         yield page
#         page.close()
#         browser.close()


# def test_checkbox(page):
#     page.goto("https://webdriveruniversity.com/Dropdown-Checkboxes-RadioButtons/index.html")
#     page.select_option("#dropdowm-menu-1", value='Python')
#     page.select_option("#dropdowm-menu-2", value='Maven')
#     page.select_option("#dropdowm-menu-3", value='CSS')
#
#     page.locator('text=Option 1').check()
#     page.locator('text=Option 2').check()
#
#     # page.locator("input[name=\"color\"]").nth(1).check()
#     # page.locator("input[name=\"color\"]").nth(3).check()
#     page.locator("#radio-buttons input[value='green']").check()
#     page.locator('.section-title input[name="vegetable"][value="lettuce"]').check()
#     page.select_option('#fruit-selects', value='Apple')


# def test_checkbox_2(page):
#     page.goto("https://demoqa.com/checkbox", wait_until="commit")
#     #page.get_by_role("button", name='Toggle').click()
#     page.locator('button[title="Toggle"]').click()
#     page.locator('#tree-node ol ol button').nth(0).click()
#     page.locator('#tree-node ol ol ol li [class="rct-checkbox"]').nth(0).click()

# def test_select(page):
#     page.goto("https://the-internet.herokuapp.com/dropdown")
#     page.select_option('#dropdown', value='Option 1')

# def test_button(page):
#     page.goto("https://demoqa.com/buttons", wait_until="commit")
#
#     page.locator('#doubleClickBtn').dblclick()
#     page.locator('#rightClickBtn').click(button='right')
#     page.get_by_text("Click Me", exact=True).click()

# def test_upload_download_1(page):
#     page.goto("https://demoqa.com/upload-download", wait_until="commit")
#
#     with page.expect_download() as download_info:
#         page.locator('#downloadButton').click()
#
#     download = download_info.value
#     path = './my_test_download_path/'
#     file_name = download.suggested_filename
#     download.save_as(os.path.join(path, file_name))
#
#     page.set_input_files("#uploadFile", "hello.txt")

# def test_upload(page):
#     page.goto("https://practice-automation.com/file-download/", wait_until="commit")
#     page.on("dialog", lambda dialog: dialog.accept("automateNow"))
#     page.locator("div .media [data-package='921']").click()
#     time.sleep(1)
    #page.wait_for_selector('div .modal-content', timeout=500)
    # page.get_by_role("textbox", name="Enter Password").fill("automateNow")
    # page.locator('span [value="Submit"]').click()
    # time.sleep(1)


# def test_alerts(page):
#     page.goto("https://webdriveruniversity.com/Popup-Alerts/index.html")
#
#     page.once("dialog", lambda dialog: dialog.accept())
#
#     page.locator("#button1 p").click()
#
#     page.once("dialog", lambda dialog: dialog.dismiss())
#     page.locator("#button2 p").click()
#
#     page.once("dialog", lambda dialog: dialog.default_value())
#     page.locator("#button4 p").click()
#
#     page.once("dialog", lambda dialog: dialog.dismiss())
#     page.locator("#button3 p").click()
#     page.wait_for_selector('#myDiv p').click()
#
#     time.sleep(3)


# def test_data_tables(page):
#     page.goto("https://the-internet.herokuapp.com/tables")
#
#     row = page.locator('#table1').inner_text()
#     print('\n', row)
#     b = row.split('\t' or '\n')
#     print(b)
#     a = ' '.join(b)
#
#     for i_string in b:
#         # if b.index(i_string) % 6 == 0:
#         #     print('\n')
#         print(i_string, end=' ')
#         #print('\n')



