from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import pandas as pd


web = "https://www.bangkokpost.com/"
path = "~/downloads/chromedriver"  # introduce path here

# Creating the driver
# add headless mode
options = Options()
options.headless = True
driver_service = Service(executable_path=path)
driver = webdriver.Chrome(service=driver_service, options=options)
driver.get(web)

# Finding Elements
containers = driver.find_elements(by="xpath", value='//div[@class="list-detail"]')

titles = []
subtitles = []
links = []
for container in containers[0:5]:
    # print(container)

    title = container.find_element(by="xpath", value=".//a").text
    subtitle = container.find_element(by="xpath", value=".//p").text
    link = container.find_element(by="xpath", value=".//a").get_attribute("href")
    titles.append(title)
    subtitles.append(subtitle)
    links.append(link)


# Exporting data to a CSV file
my_dict = {"title": titles, "subtitle": subtitles, "link": links}
df_headlines = pd.DataFrame(my_dict)
df_headlines.to_csv("headline.csv")

driver.quit()
