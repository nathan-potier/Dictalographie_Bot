import time
import keyboard 
import bs4

html = str(input())

soup = bs4.BeautifulSoup(html, "html.parser")

text = soup.get_text()

print(text)

    
def emuler_saisie(texte):
    keyboard.write(texte, delay=0.05)


texte_a_ecrire = text

time.sleep(2)
emuler_saisie(texte_a_ecrire)




 

