from os import system
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import pandas as p
from datetime import date, timedelta
import argparse
from random import randint

dictionaries = open("helper.help", "r+")
ap = argparse.ArgumentParser()
URL = 'https://www.thantai.net/so-ket-qua'
exec_path = '/usr/local/bin/chromedriver'
current_date = date.today()
data = []
VALUES = []
ACCEPT_PROVINCE = [
    "mb",
    "ag",
    "bl",
    "bdu",
    "bdi",
    "bp",
    "bth",
    "btr",
    "cm",
    "ct",
    "dlt",
    "dna",
    "dlc",
    "dno",
    "dni",
    "dt",
    "gl",
    "hg",
    "hcm",
    "kg",
    "kh",
    "kt",
    "la",
    "nt",
    "py",
    "qb",
    "qna",
    "qng",
    "qt",
    "st",
    "tn",
    "tth",
    "tg",
    "tv",
    "vl",
    "vt"
]
index: int = 0
ap.add_argument("-p", "--province", type=str,
                required=True, help=f"Choose the province, value is: {dictionaries.readlines()}")
# ap.add_argument("-nv", "--numval", required=True, type=int,
#                 help="Number of reading values, recommend should be around 3600-4000 values")
args = ap.parse_args()

if __name__ == "__main__":

    if args.province not in ACCEPT_PROVINCE:
        print("Value not in the list, please select again !")
        quit()
    else:
        system('clear')
        print("[INFO]: IS INITIALIZING\n")
        print("[INIT]: 0%\n")
        sleep(1.2)
        print("[INIT]: 20% ==>\n")
        sleep(1.2)
        print("[INIT]: 40% ====>\n")
        sleep(1.2)
        print("[INIT]: 60% ======>\n")
        sleep(1.2)
        print("[INIT]: 80% ========>\n")
        sleep(1.2)
        print("[INIT]: 100% ==============>\n")
        sleep(1.2)
        print("[INFO]: INIT FINISHED, START THE READ!\n")
        browser = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()))
        browser.get(URL)
        province = Select(browser.find_element(By.ID, "province"))
        province.select_by_value(args.province)
        isRunning = True
        while isRunning:
            print(
                f'[INFO]: Process 300 days from {current_date.day}-{current_date.month}-{current_date.year}')

            elm_end = browser.find_element(By.ID, "end")
            elm_end.clear()
            elm_end.send_keys(
                f"{current_date.day}-{current_date.month}-{current_date.year}")

            button = browser.find_element(
                By.XPATH, "/html/body/div[2]/main/div/form/div[2]/div/button[9]")
            button.click()

            results = browser.find_elements(
                By.CLASS_NAME, "font-weight-bold.text-danger.col-12.d-block.p-1.m-0")

            for r in results:
                print(f"[DATA]: {r.text}")
                index += 1
                data.append(r.text)
            print(f"[INFO]: Total number of index: {index}")
            current_date -= timedelta(days=300)

            if index > 4000:
                print("[INFO] Training process has completed...")
                sleep(0.5)
                system('clear')
                break

    data_frame = p.DataFrame(data, columns=["Results"])
    data_frame.to_csv(
        f"./CSVs/XS_{str(args.province).upper()}_Do_Tai.csv", index=False)
    print(
        f"[INFO]: FINISHED THE COLLECTING PROCESS, the file is: XS_{str(args.province).upper()}_Do_Tai.csv!\n")
    browser.close()
