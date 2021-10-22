# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import requests
from bs4 import BeautifulSoup

r = requests.get('https://fubon-ebrokerdj.fbs.com.tw/Z/ZG/ZGK_DD.djhtm')

if r.status_code == requests.codes.ok:
    print("Web request OK!")
else:
    print("Web FAIL! (r.status_code:{})".format(r.status_code))

soup = BeautifulSoup(r.text, "html.parser")
print(soup.prettify())
print('1')
#soup.find('tr').find_all('td')
result = soup.find('tr').find_all("td")
print('1')

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
