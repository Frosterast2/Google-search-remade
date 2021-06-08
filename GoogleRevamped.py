from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import cv2
from tkinter import *
import time
import webbrowser

with open("Scrolling.txt", "wt") as file:
	file.write("0")

option = webdriver.ChromeOptions()
option.add_argument("--start-maximized")
option.add_argument('window-size=1220,780')
option.add_argument("headless")
driver = webdriver.Chrome(executable_path="chromedriver.exe", options=option)

win = Tk()
kk = 0
r1 = Button(win, text="1", command=lambda:kk == kk + 1)
r2 = Button(win, text="2", command=lambda:kk == kk + 1)
r3 = Button(win, text="3", command=lambda:kk == kk + 1)
r4 = Button(win, text="4", command=lambda:kk == kk + 1)
r5 = Button(win, text="5", command=lambda:kk == kk + 1)
r6 = Button(win, text="6", command=lambda:kk == kk + 1)
r7 = Button(win, text="7", command=lambda:kk == kk + 1)
r8 = Button(win, text="8", command=lambda:kk == kk + 1)
r9 = Button(win, text="9", command=lambda:kk == kk + 1)
r10 = Button(win, text="10", command=lambda:kk == kk + 1)

scrolltop= Button(win, text="Top", command=kk == kk + 1)
scrollmid = Button(win, text="Middle", command=kk == kk + 1)
scrollbot = Button(win, text="Bottom", command=kk == kk + 1)

def gooo(urll):
	driver.get(f"https://google.com/search?q={urll}")
	def scroll(ud):
		if ud == "top":
			driver.execute_script("window.scrollTo(document.body.scrollWidth, 0)")
		elif ud == "mid":
			driver.execute_script("window.scrollTo(document.body.scrollWidth, 1100)")
		elif ud == "bot":
			driver.execute_script("window.scrollTo(document.body.scrollWidth, 2300)")


	scrolltop.configure(command=lambda: scroll("top"))
	scrollmid.configure(command=lambda: scroll("mid"))
	scrollbot.configure(command=lambda: scroll("bot"))

	time.sleep(5)
	#driver.maximize_window()
	results = driver.find_elements_by_class_name("yuRUbf")
	#a = results.find_elements_by_tag_name("a")
	r1.configure(command=lambda:webbrowser.open(results[0].find_element_by_tag_name("a").get_attribute("href")))
	r2.configure(command=lambda:webbrowser.open(results[1].find_element_by_tag_name("a").get_attribute("href")))
	r3.configure(command=lambda:webbrowser.open(results[2].find_element_by_tag_name("a").get_attribute("href")))
	r4.configure(command=lambda:webbrowser.open(results[3].find_element_by_tag_name("a").get_attribute("href")))
	r5.configure(command=lambda:webbrowser.open(results[4].find_element_by_tag_name("a").get_attribute("href")))
	r6.configure(command=lambda:webbrowser.open(results[5].find_element_by_tag_name("a").get_attribute("href")))
	r7.configure(command=lambda:webbrowser.open(results[6].find_element_by_tag_name("a").get_attribute("href")))
	r8.configure(command=lambda:webbrowser.open(results[7].find_element_by_tag_name("a").get_attribute("href")))
	r9.configure(command=lambda:webbrowser.open(results[8].find_element_by_tag_name("a").get_attribute("href")))
	r10.configure(command=lambda:webbrowser.open(results[9].find_element_by_tag_name("a").get_attribute("href")))
	
		
	while True:
		driver.save_screenshot("screeennshooot.png")
		photo = cv2.imread(("screeennshooot.png"))
		cv2.imshow("mat", photo)
		cv2.waitKey(1)
		win.update()
		

i = Entry(win)
i.pack()

Button(win, text="Search", command=lambda:gooo(i.get())).pack()
Label(win, text="Results: ").pack()

r1.pack()
r2.pack()
r3.pack()
r4.pack()
r5.pack()
r6.pack()
r7.pack()
r8.pack()
r9.pack()
r10.pack()

Label(win, text="Scrolling:").pack()

scrolltop.pack()
scrollmid.pack()
scrollbot.pack()

mainloop()