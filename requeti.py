import requests
import pandas as pd
import sqlite3
from datetime import datetime
from functions import list_dates

                                    #####reprise date de début ######
from datetime import datetime, timedelta

connexion=sqlite3.connect('bddt.db')
curseur= connexion.cursor()
    
curseur.execute("""
                    SELECT MAX(data)
                    FROM objets_trouves     
                    """)
rslt=curseur.fetchall()

a=rslt[0][0]
###conversion date au format voulu
b = datetime.strptime(a, '%Y-%m-%d')
date_bdd = b.strftime('%d%m%Y')

print(date_bdd) 

                                #######reprise date now   #######


date_now=datetime.now().strftime('%d%m%Y')
print (date_now)

list_dates_mank=list_dates(date_bdd, date_now)



# day=c[0][:2]
# month=c[0][2:4]
# year=c[0][4:]


gares_parisiennes = ["Paris Gare de Lyon", "Paris Gare du Nord","Paris Montparnasse", "Paris Est" , "Paris Saint-Lazare" , "Paris Austerlitz" , 'Paris Bercy']

for gare in gares_parisiennes:
    print (len(list_dates_mank))
    for i in list_dates_mank:
        day=i[:2]
        month=i[2:4]
        year=i[4:]
        print (year)
        print(month)
        print(day)
        response = requests.get(f"https://ressources.data.sncf.com/api/records/1.0/search/?dataset=objets-trouves-restitution&q=&rows=-1&sort=-date&facet=date&facet=gc_obo_date_heure_restitution_c&facet=gc_obo_gare_origine_r_name&facet=gc_obo_nature_c&facet=gc_obo_type_c&facet=gc_obo_nom_recordtype_sc_c&refine.gc_obo_gare_origine_r_name={gare}&refine.date={year}%2F{month}%2F{day}")
        records= response.json()                                                                                                                                                                                                                                                                                                                          #efine.date=2022%2F12%2F31
        print (records)
        for i in records['records']:
                print(i)
                dati = i['fields']['date']
                typo = i['fields']['gc_obo_type_c']
                gara = i['fields']['gc_obo_gare_origine_r_name']
                connexion = sqlite3.connect("bdi.db")
                curseur = connexion.cursor()
                curseur.execute("""
                    INSERT INTO objets_trouves (data,typo,gare)
                    VALUES
                    ('{}','{}','{}')
                """.format(dati, typo, gara))
        connexion.commit()