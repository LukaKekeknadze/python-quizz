# ------------info ორგანიზაციების შესახებ--------------
# პუნქტი 1//api ის გამოძახება და რამოდენიმე ფუნქციის გამოყენება
import sqlite3

import requests
import json

domain = input('შეიყვანეთ domain საიტის(მაგ: facebook.com): ')

url = f"https://companyenrichment.abstractapi.com/v1/?api_key=40747c5835df4311bb65bf7cfb3cbee3&domain={domain}"
r = requests.get(url)
print("საიტის request-ის გაშვების შედეგიანობა(response) : ", r)
print("საიტის request-ის გაშვების შედეგიანობა : ", r.status_code)
print("API დან გადმოტანილი content-ის ინფორმაცია : ", r.headers)
print("API დან გადმოტანილი ინფორმაცია : ", r.text)

# პუნქტი 2(json-ის ფორმატიში ინფორმაციის ჩაწერა)
res = json.loads(r.text)
print(json.dumps(res, indent=4))
# პუნქტი 3//კონკრეტული ინფორმაციის დაბეჭდვა
industry = res['industry']
name = res['name']
year = res['year_founded']
print("ორგანიზაციის სახელი : ", name)
print("ორგანიზაციის მოღვაწეობის ადგილი : ", industry)
print("ორგანიზაციის დაარსების თარიღი : ", year, "წელი")

# პუნქტი 4//მონაცემების ბაზაში ჩაწერა


conn = sqlite3.connect('info.sqlite')
cursor = conn.cursor()
cursor.execute(''' CREATE TABLE IF NOT EXISTS organisation_info 
                (id integer primary key autoincrement,
                name varchar(50),
                domain varchar(50),
                year_founded integer,
                industry varchar(50),
                employees_count integer



  ) ''')
conn.commit()

name = res['name']
domain = res['domain']
year_founded = res['year_founded']
industry = res['industry']
employees_count = res['employees_count']
row = (name, domain, year_founded, industry, employees_count)

cursor.execute("insert into organisation_info(name,domain,year_founded,industry,employees_count) Values (?,?,?,?,?)",
               row)
conn.commit()
