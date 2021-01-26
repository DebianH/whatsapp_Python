from selenium import webdriver
import time
import os, time


driver = webdriver.Chrome(executable_path=r"C:\Users\HP\Downloads\Program\chromedriver.exe")  #La ubicacion del ejecutable de google chrome

driver.get("https://web.whatsapp.com/") #Link de whatsapp web

time.sleep(15) # <= Tiempos para ir manipulando el navegador 

#Datos

phone = "593984633111"  #Ingresa el numero con el codigo del pais

mensaje = "Aqui tu mensaje"



print("Inicia..")

driver.get("https://wa.me/"+phone+"?text="+mensaje)
time.sleep(5)

btn = driver.find_elements_by_xpath("//*[@id='action-button']")[0]
btn.click()
time.sleep(5)


btn = driver.find_elements_by_xpath("//*[@id='fallback_block']/div/div/a")[0]
btn.click()
time.sleep(10)

btn = driver.find_elements_by_xpath("//*[@id='main']/footer/div[1]/div[3]")[0]
btn.click()
time.sleep(10)

print("Bot finalizado")

time.sleep(120)


driver.close()
