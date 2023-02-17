def display_voiture(self):
        # On récupère les infos sur les voitures
        h3 = self.html.find_all("h3", {"class": "Text_Text_text Vehiculecard_Vehiculecard_title Text_Text_subtitle2"})
        annees = self.html.find_all("div", {"class": ""})
        prix = self.html.find_all("div", {"class": ""})
        km = self.html.find_all("div", {"class": ""})
        
        
        #stock les infos dans une liste
        list_cars = [i.string.strip() for i in h3]
        list_annees = [i.string.strip() for i in annees]
        list_prix = [i.string.strip().replace(' ','').replace('€','') for i in prix]
        list_km = [i.string.strip().replace('KM','').replace(' ','') for i in km]
        
        

        with open("Data.csv","a") as files:  
            csv_writer = csv.writer(files) 
            csv_writer.writerow([list_cars[i], list_annees[i], list_prix[i], list_km[i]])
