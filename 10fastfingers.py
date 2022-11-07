from selenium import webdriver
from time import sleep, time
from selenium.webdriver.common.by import By

def fast_fingers():
	loginInput = input("Login: ")
	pwdInput = input("Password: ")
	secs = float(input("Seconds between words(For example: 0.6): "))
	PATH = "path to webdriver" #Path to webdriver
	driver = webdriver.Chrome(executable_path=PATH)
	try:
		driver.get("https://10fastfingers.com/login")
		driver.refresh()
		sleep(2)
		allowCookie = driver.find_element("id", "CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll")
		allowCookie.click()
		login = driver.find_element("id", "UserEmail")
		login.send_keys(loginInput) #Account email
		password = driver.find_element("id", "UserPassword")
		password.send_keys(pwdInput) #Account password
		loginBtn = driver.find_element("id", "login-form-submit")
		loginBtn.click()

		a = 0
		driver.get("https://10fastfingers.com/typing-test/english") #You can change english to another language you want
		sleep(2)
		timer = driver.find_element("id", "timer")
		getWord = driver.find_elements(By.CLASS_NAME, "highlight")
		inputField = driver.find_element("id", "inputfield")
		while timer.text != "0:00":
			try:
				getWord = driver.find_element(By.CLASS_NAME, "highlight")
				inputField.send_keys(getWord.text + " ")
				sleep(secs) #Seconds between inputs

			except Exception:
				break
	except Exception as ex:
		print(ex)
	finally:
		print("----------------------------\nThe app will close in 10 seconds\n----------------------------")
		sleep(10) #Seconds before quit
		driver.close()
		driver.quit()



def main():
	fast_fingers()


	

if __name__ == "__main__":
	main()