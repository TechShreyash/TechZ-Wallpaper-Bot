import asyncio
import requests
from bs4 import BeautifulSoup as bs
from time import sleep
import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from pyrogram.types import Message


async def scrap_mkv(link, message: Message):
    r = requests.get(link)
    soup = bs(r.content, 'html.parser')
    mealob = soup.find_all('a', 'gdlink')
    await message.edit('⛩ Found {} links\n\n'.format(len(mealob)))
    x = message.text

    chromedriver_autoinstaller.install()
    generater = '//*[@id="generater"]'
    showlink = '//*[@id="showlink"]'
    landing = '//*[@id="landing"]/div[2]/center/img'
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-dev-shm-usage")

    wd = webdriver.Chrome(options=chrome_options)
    gdtot = []

    await message.edit(x+'Scraping Gdtot Links...\n')

    pos = 1

    for i in mealob:
        wd.get(i['href'])
        sleep(3)
        WebDriverWait(wd, 10).until(
            ec.element_to_be_clickable((By.XPATH, landing))
        ).click()
        WebDriverWait(wd, 10).until(
            ec.element_to_be_clickable((By.XPATH, generater))
        ).click()
        WebDriverWait(wd, 10).until(
            ec.element_to_be_clickable((By.XPATH, showlink))
        ).click()
        IItab = wd.window_handles[1]
        wd.close()
        wd.switch_to.window(IItab)
        gdtot.append(wd.current_url)
        await message.edit(message.text+f'\n{pos} : {wd.current_url}')
        pos += 1

    wd.quit()
