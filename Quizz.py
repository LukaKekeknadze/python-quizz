#------------info ორგანიზაციების შესახებ--------------
#პუნქტი 1//api ის გამოძახება და რამოდენიმე ფუნქციის გამოყენება
import requests
import json
domain = input('შეიყვანეთ domain საიტის(მაგ: facebook.com): ')
url = "https://companyenrichment.abstractapi.com/v1/?api_key=40747c5835df4311bb65bf7cfb3cbee3&domain={}".format(domain)
r = requests.get(url)
print("საიტის request-ის გაშვების შედეგიანობა(response) : ", r)
print("საიტის request-ის გაშვების შედეგიანობა : ",r.status_code)
print("API დან გადმოტანილი content-ის ინფორმაცია : ",r.headers)
print("API დან გადმოტანილი ინფორმაცია : ",r.text)

#პუნქტი 2(json-ის ფორმატიში ინფორმაციის ჩაწერა)
res = r.json()
print(json.dumps(res, indent = 4))
#პუნქტი 3//კონკრეტული ინფორმაციის დაბეჭდვა
industry = res['industry']
name = res['name']
year = res['year_founded']
print("ორგანიზაციის სახელი : ", name)
print("ორგანიზაციის მოღვაწეობის ადგილი : ", industry)
print("ორგანიზაციის დაარსების თარიღი : ", year,"წელი")

#პუნქტი 4//ფაილში ჩაწერა
f =open('organization.json', 'w', encoding="utf-8" )
json.dump(res,f, indent=4 )
