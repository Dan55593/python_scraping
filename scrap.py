# Importation des modules nécessaires
import csv
import requests as rq  
from bs4 import BeautifulSoup as bs  
# Je cree une Classe pour générer l'URL de recherche
class Url:
    def __init__(self, page):
        # J'initialise des critères de recherche
        self.energie = "dies"
        self.marque = "PEUGEOT" 
        self.km_max = 40000 
        self.km_min = 1
        self.prix_min = 10000
        self.prix_max = 60000
        self.annee_min = 2000
        self.annee_max = 2023
        self.page = page 

    # pour générer l'url de recherche
    def url(self):
   
        return "https://www.lacentrale.fr/listing?&energies={}&makesModelsCommercialNames={}&mileageMax={}&mileageMin=1{}&page={}&priceMax={}&priceMin={}&yearMax={}&yearMin={}".format(self.energie, self.marque.upper(), self.km_max, self.km_min,self.page,self.prix_max, self.prix_min, self.annee_max, self.annee_min)
#  pour scrapper les données
class ScrapData:
    def __init__(self, url):
   
        self.url = url   
        
        self.request_url = rq.get(self.url)# pour récupérer la page HTML
      
        self.response = self.request_url.content # ICI c'est le contenu de la réponse

        self.html = bs(self.response, "lxml")  #Objet BeautifulSoup pour parser le contenu
 # afficher les résultat de la recherche
    def display_cars(self):
        
        h3 = self.html.find_all("h3", {"class": "Text_Text_text Vehiculecard_Vehiculecard_title Text_Text_subtitle2"})

        list_cars = [i.string.strip() for i in h3]#ICI ON VA Stocker des titres dans une liste
 
        with open("Data.csv","a") as files:  #Ouverture du fichier CSV pour écriture
            for i in list_cars:
                csv_writer = csv.writer(files)#Initialisation du writer CSV
                csv_writer.writerow(['{}'.format(i), ''])# Écriture de chaque titre dans une ligne du CSV


