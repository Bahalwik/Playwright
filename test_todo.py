import os
import time

from playwright.sync_api import Playwright, sync_playwright
import pytest
from playwright.sync_api import expect

@pytest.fixture
def browser_fixture():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        yield page
        page.close()
        browser.close()


# def test_add_todo(page) -> None:
#     page.goto("https://demo.playwright.dev/todomvc/#/")
#     page.get_by_role("textbox", name="What needs to be done?").click()
#     page.get_by_role("textbox", name="What needs to be done?").fill("Создать первый сценарий playwright")
#     page.get_by_role("textbox", name="What needs to be done?").press("Enter")
#     page.get_by_role("link", name="Completed").click()


# def test_checkbox(page):
#     page.goto('https://zimaev.github.io/checks-radios/')
#     page.locator("text=Default checkbox").check()
#     page.locator("text=Checked checkbox").check()
#     page.locator("text=Default radio").check()
#     page.locator("text=Default checked radio").check()
#     page.locator("text=Checked switch checkbox input").check()
#     time.sleep(1)

# def test_drag_and_drop(page):
#     page.goto('https://zimaev.github.io/draganddrop/')
#     page.drag_and_drop("#drag", "#drop")

# def test_dialogs(page):
#     page.goto("https://zimaev.github.io/dialog/")
#     page.on("dialog", lambda dialog: dialog.accept())
#     page.get_by_text("Диалог Confirmation").click()
#
# def test_download(page):
#     page.goto('https://demoqa.com/upload-download', wait_until="commit")
#
#     with page.expect_download() as download_info:
#         page.locator("#downloadButton").click()
#
#     download = download_info.value
#     file_name = download.suggested_filename
#     download_path = './download_files/'
#     download.save_as(os.path.join(download_path, file_name))

# def test_screenshot(page):
#
#     page.goto('https://zimaev.github.io/table/')
#     page.screenshot(path="transparent_background.png", omit_background=True)
    #page.screenshot(path="./download_files/clipped_image.png", clip={"x": 50, "y": 0, "width": 400, "height": 300})


# def test_new_tab(page):
#     page.goto("https://zimaev.github.io/tabs/")
#     with page.context.expect_page() as tab:
#         page.get_by_text("Переход к Dashboard").click()
#
#     new_tab = tab.value
#     assert new_tab.url == "https://zimaev.github.io/tabs/dashboard/index.html?"
#     sign_out = new_tab.locator('.nav-link', has_text='Sign out')
#     assert sign_out.is_visible()

# def test_train(page):
#     page.goto('https://demo.playwright.dev/todomvc/#/')
#     expect(page).to_have_url("https://demo.playwright.dev/todomvc/#/")
#
#     text_field = page.get_by_placeholder("What needs to be done?")
#     expect(text_field).to_be_empty()
#
#     text_field.fill('first')
#     text_field.press('Enter')
#
#     text_field.fill('second')
#     text_field.press('Enter')
#     page.pause()
#     todo_item = page.get_by_test_id('todo-item')
#     expect(todo_item).to_have_count(2)
#
#     todo_item.get_by_role('checkbox').nth(0).click()
#     expect(todo_item.nth(0)).to_have_class('completed')

# def test_network(page):
#     page.goto('https://reqres.in/')
#     page.route("**/register", lambda route: route.continue_(post_data='{"email": "eve.holt@reqres.in","password": "pistol"}'))
#     page.goto('https://reqres.in/')
#     page.get_by_text(' Register - successful ').click()
#
#     page.pause()


# def test_replace_from_har(page):
#     page.goto("https://reqres.in/")
#     page.route_from_har("example.har")
#     users_single = page.locator('li[data-id="users-single"]')
#     users_single.click()
#     response = page.locator('[data-key="output-response"]')
#     #expect(response).to_contain_text("Open Solutions")
#     page.pause()