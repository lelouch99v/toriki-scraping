# -*- coding: utf-8 -*-

from selenium import webdriver
import pandas as pd
from selenium.webdriver.chrome.options import Options
from time import sleep

options = Options()
browser = webdriver.Chrome(
    '/usr/local/Caskroom/chromedriver/75.0.3770.8/chromedriver')

# データフレーム
columns = ['name', 'classification']
df = pd.DataFrame(columns=columns)

# 鳥貴族メニューURL
url = "https://www.torikizoku.co.jp/menu/"

# メニューリスト
MENU_NAME_LIST = [u'焼鳥', u'逸品料理', u'スピードメニュー', u'ご飯もの／デザート', u'ドリンク']

# メニューリンク
menu_link = 'a.left-arrow'

browser.get(url)

# スクレイピング処理


def scraping(menu_link_list, menu_name):
    for menu in menu_link_list:
        if menu.text == menu_name:
            menu.click()
            # title = browser.find_element_by_css_selector(
            #     'h4.yellowLineTitle').text
            # print(title)

            item_list = browser.find_elements_by_css_selector('li h5')

            for item in item_list:
                se = pd.Series([item.text, menu_name], columns)
                global df
                df = df.append(se, columns)  # データフレームに行を追加
                print(item.text)

            print('\n')
            browser.get(url)
            break


# 取得したいメニュー名と一致するメニューリンクにジャンプし、スクレイピング
for menu_name in MENU_NAME_LIST:
    # メニューリンクリストを取得
    menu_link_list = browser.find_elements_by_css_selector(menu_link)
    scraping(menu_link_list, menu_name)

browser.close()

df.to_csv('./result.csv')
print('DONE...')
