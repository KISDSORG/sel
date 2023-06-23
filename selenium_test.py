import streamlit as st

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@st.cache_data(persist="disk")
def get_driver():
    return webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

options = Options()
options.add_argument('--disable-gpu')
options.add_argument('--headless')
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-features=NetworkService")
options.add_argument("--window-size=1920x1080")
options.add_argument("--disable-features=VizDisplayCompositor")

driver = get_driver()
driver.get('https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20230530000941')

st.code(driver.page_source)
