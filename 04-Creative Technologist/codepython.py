from machine import Pin, PWM
import time
import network
import urequests
import utime
import ujson
import json

# Configuration des pins pour la LED RGB
pin_red = PWM(Pin(18))  
pin_green = PWM(Pin(17))  
pin_blue = PWM(Pin(16))

# Configuration du réseau Wi-Fi
wlan = network.WLAN(network.STA_IF)
wlan.active(True)

ssid = "Yani"  
password = "abcdefgh"  

wlan.connect(ssid, password)

def set_color(r, g, b):
    pin_red.duty_u16(r)
    pin_green.duty_u16(g)
    pin_blue.duty_u16(b)


while not wlan.isconnected():
    print("Pas connecté au Wi-Fi...")
    utime.sleep(1)



# Fonction pour convertir une valeur de 0-255 en une valeur de 0-65535 pour PWM
def convert_to_pwm(value):
    return value * 255

# Couleurs pour les catégories
colors = {
    'bleu': (0, 0, 255),  # Bleu
    'vert': (0, 255, 0)   # Vert
}



# Fonction pour clignoter la LED en fonction de la catégorie
def blink_led(ingredient_list):
    for ingredient in ingredient_list:
        category = ingredient['categorie']
        color = colors[category]
        print(color)
        set_color(convert_to_pwm(color[0]), convert_to_pwm(color[1]), convert_to_pwm(color[2]))
        time.sleep(1)  # LED allumée pendant 1 seconde
        set_color(0, 0, 0)  # LED éteinte
        time.sleep(0.5)  # Pause de 0.5 seconde entre les clignotements

commande = urequests.get("http://172.20.10.11:3000")
array = commande.json()["commande"]
print(array)
commande.close()



# Clignoter la LED pour chaque ingrédient de la commande
blink_led(array)


