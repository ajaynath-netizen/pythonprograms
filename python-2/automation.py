from selenium import webdriver
PATH='C:/Users/amarnath/Documents/python/python-2/chromedriver_win32(1)/chromedriver.exe'
chrome=webdriver.Chrome(PATH)
# # chrome.get('https://www.youtube.com/?gl=IN')
chrome.get("https://sphoorthyengg.codetantra.com/login.jsp#")
print(chrome.title)


inp=chrome.find_element_by_xpath("//input[@name='loginId']")
inp.send_keys('19N81A0531ajaynath@gmail.com')
password=chrome.find_element_by_xpath("//input[@placeholder='Password']")
password.send_keys('ajaynath630@')
btn=chrome.find_element_by_xpath("//button[@id='loginBtn']")
btn.click()

def select(x):
     a={"1":'//a[@title="Click here to view Courses"]',"3":'//a[@title="Click here to view Tests"]',"2":'//a[@title="Click here to view Labs"]',"4":'//a[@title="Click here for Support details"]'}
     choose=a.get(x,0)
     return choose
def inform():
    print("1->to go for courses")
    print("2->to go for labs")
    print("3->to go for Tests")
    print("4->to go for help and support")
    print("5->to go back")
    print("6-> to exit window")
    print('enter "break" for no control')
    while True:
       name=input('select from above : ')
       try:
          if name=="1" or name=="2" or name=="3" or name=="4":
            chose=chrome.find_element_by_xpath(select(name))
            chose.click()
            inform()

          elif name=="5":
             
             chrome.get('https://sphoorthyengg.codetantra.com/secure/home.jsp')
             inform()

          elif name=="break":

              break
          elif name=="6":
              chrome.close()
              break
          
          else:
              raise EnvironmentError
       except Exception as e:
            print("chose only given objects ",e)

if __name__ == "__main__":
    inform()


# brand.click()
# lin=chrome.find_element_by_partial_link_text('Latest Python 3')
# lin.click()
# ano=chrome.find_element_by_partial_link_text('PEP 58')
# ano.click()
# var=chrome.find_elements_by_link_text('python-dev at python.org')
# var.click()
# print(brand)