import requests
import pandas as pd
import sqlite3
from datetime import datetime

now = datetime.now()
print("Date et heure du jour :", now)
print(now.hour)
print(now.minute)



gares_parisiennes = ["Paris Gare de Lyon", "Paris Gare du Nord", "Paris Est" ,"Paris Montparnasse", "Paris Saint-Lazare" , "Paris Austerlitz" , 'Paris Bercy']
annees = [now.year]
%2F04%2F12 
url_actu+ "%2F"{now.month}"%2F"{now.day}
# Création d'un DataFrame vide
df = pd.DataFrame()
i = 0
for gare in gares_parisiennes:
    for annee in annees:
        print(i)                                                                                                                                                                                                                        
        response = requests.get(f"https://ressources.data.sncf.com/api/records/1.0/search/?dataset=objets-trouves-restitution&q=&rows=-1&sort=-date&facet=date&facet=gc_obo_date_heure_restitution_c&facet=gc_obo_gare_origine_r_name&facet=gc_obo_nature_c&facet=gc_obo_type_c&facet=gc_obo_nom_recordtype_sc_c&refine.gc_obo_gare_origine_r_name={gare}&refine.date={annee}")
        response = requests.get(f"https://ressources.data.sncf.com/api/records/1.0/search/?dataset=objets-trouves-restitution&q=&rows=-1&sort=-date&facet=date&facet=gc_obo_date_heure_restitution_c&facet=gc_obo_gare_origine_r_name&facet=gc_obo_nature_c&facet=gc_obo_type_c&facet=gc_obo_nom_recordtype_sc_c&refine.gc_obo_gare_origine_r_name={gare}&refine.date={annee}%2F{now.month}%2F{now.day}")
        records= response.json()

        for i in records['records']:
            dati = i['fields']['date']
            typo = i['fields']['gc_obo_type_c']
            gara = i['fields']['gc_obo_gare_origine_r_name']
            connexion = sqlite3.connect("bddd.db")
            curseur = connexion.cursor()
            curseur.execute("""
                INSERT INTO objets_trouves (data,typo,nom_gare)
                VALUES
                ('{}','{}','{}')
            """.format(dati, typo, gara))
            connexion.commit()
            
            

a=['31122022',
 '01012023',
 '02012023',
 '03012023',
 '04012023',]
day=a[0][:2]
month=a[0][2:4]
year=a[0][4:]


gares_parisiennes = ["Paris Gare de Lyon", "Paris Gare du Nord", "Paris Est" , "Paris Saint-Lazare" , "Paris Austerlitz" , 'Paris Bercy']

for gare in gares_parisiennes:
    for i in a:
        day=i[0][:2]
        month=i[0][2:4]
        year=i[0][4:]
        response = requests.get(f"https://ressources.data.sncf.com/api/records/1.0/search/?dataset=objets-trouves-restitution&q=&rows=-1&sort=-date&facet=date&facet=gc_obo_date_heure_restitution_c&facet=gc_obo_gare_origine_r_name&facet=gc_obo_nature_c&facet=gc_obo_type_c&facet=gc_obo_nom_recordtype_sc_c&refine.gc_obo_gare_origine_r_name={gare}&refine.date={year}%2F{month}%2F{day}")
        records= response.json()
        for i in records['records']:
                dati = i['fields']['date']
                typo = i['fields']['gc_obo_type_c']
                gara = i['fields']['gc_obo_gare_origine_r_name']
                connexion = sqlite3.connect("bddd.db")
                curseur = connexion.cursor()
                curseur.execute("""
                    INSERT INTO objets_trouves (data,typo,nom_gare)
                    VALUES
                    ('{}','{}','{}')
                """.format(dati, typo, gara))
                connexion.commit()