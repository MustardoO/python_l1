#!/usr/bin/env python3

#Nom         : DIAGNE
#Prenom      : Moustapha
#N. Etudiant : 21011573

#/* MÉTADONNÉES 
# *******************************************************
# Nom ......... : RobotIndexWeb.py
# Rôle ........ : Scrape récursivement les pages d'une page web 
# Auteur ...... : DIAGNE Moustapha
# Version ..... : V0.3 du 24/03/2022
# Licence ..... : réalisé dans le cadre du cours de méthodologie en programmation
# (../..)
# Compilation : gcc (GNU COMPILER COLLECTION)
# Usage : Python 3, script prenant comme unique argument l'url source (entre guillemets)
#******************************************************* */

import sys
import re # module 'regular expressions'
import requests

#-------------------------------------------------------------------------------------------------------------------------------

def extraire_liens(page):
    
    lien = re.compile(r'"http.+?"') # note perso : r'<a href="http[\S]+"[\s\d\w"=<>]*</a>'
        
    lstLiensPurgés = []
    
    for lien in lien.findall(page) :  
        lstLiensPurgés.append(lien.strip(chr(34)))
    
    return lstLiensPurgés
    

def nettoie_page(page):
    
    #pageSsVide = re.sub('\n|\t','',page) # pour une page sans retours chariot ni tabulation

    balise = re.compile(r'<[^>]+>') # on récupère toutes les balises HTML
    
    texteDébalisé = re.sub(balise,'',page) # on cherche les balises dans la page et on les remplace par '' (supprime)
    
    texteNettoyé = re.split("\s|\W",texteDébalisé) # on split() sur les espaces et les caractères NON alphanumériques
    
    texteNettoyé = list(set(list(filter(None,texteNettoyé)))) #on supprime les doublons, les vides
        
    return sorted(texteNettoyé) #on renvoie la liste triée

#-----------------------------------------------------------------------------------------------------------------------------

lstPonctuations = ['.',',',':',';','!','?',"'"]

lstArticles =['un','une','des','le','la',"l'",'les','au','du','à la','de la',"de l'", 'aux']

lstPrépositions =['à','dans','par','pour','en','vers','avec','de',"d'",'sans', 'sous']

lstPronomPers =['je',"j'",'tu','il','elle','on','nous','vous', 'ils', 'elles']
lstPronomComp =['me','te','se','le', 'lui','la',"l'",'les','leur','eux','moi','toi']
lstPronomPoss =['son','sa','ses','ma','mon','mes','ta','ton','tes','nos','vos','leurs','mien','mienne','miens','miennes','nôtre','nôtres','tien','tienne','tiens','tiennes','vôtre','vôtres','sien','sienne','siens','siennes', 'leur', 'leurs']
lstPronomDemo =['celui','celle','ceux','celles','ceci','cela','ce',"c'",'ça','celui-ci','celui-là', 'celle-ci', 'celle-là', 'ceux-ci', 'ceux-là', 'celles-ci','celles-là','cet','cette']
lstPronomRel =['qui','que','quoi','dont','où','lequel','laquelle','duquel','auquel','lesquelles','desquelles','auxquelles','ledit','ladite','lesdits','lesdites','dudit','desdits']

lstPronoms = lstPronomPers + lstPronomComp + lstPronomPoss + lstPronomDemo + lstPronomRel

lstAdverbeMani =['ainsi','aussi','uns','bien','mal','comme','comment','debout','ensemble','exprès','mieux','pire','pis','plutôt','avec','sans','plutôt','presque','vite','volontiers','admirablement','doucement','également','franco','gratis','impromptu','incognito','lentement','recta','adroitement','agréablement','aveuglément','adroitement','concrètement','rapidement','sauvagement','savamment','prudemment','obstinément','lentement','joyeusement','inopinément','gauchement','effrontément','concrètement','bravement']
lstAdverbeQté = ['à peine','peu','tant','absolument','à demi','assez','autant','autrement','approximativement','beaucoup','carrément','combien','complètement','davantage','diablement','divinement','drôlement','entièrement','encore','environ','fort','guère','même','moins','plus','pas mal','plutôt','presque','prou','quasi','quelque','quelques','rudement','si','suffisamment','tant','tellement','terriblement','totalement','tout','tout à fait','très','trop','un','extrêmement','grandement','infiniment','insuffisamment','passablement','quasiment','joliment','intensément','modérément','sensiblement','environ','exagérément','passablement']
lstAdverbeTemps =['alors','après','avant','après-demain',"aujourd'hui",'auparavant','aussitôt','autrefois','avant-hier','bientôt','cependant',"d'abord",'déjà','demain','depuis','derechef','désormais','dorénavant','encore','enfin','ensuite','entre-temps','hier','jadis','jamais','longtemps','lors','maintenant','naguère','parfois','plus','premièrement','puis','quand','quelquefois','sitôt','soudain','souvent','subito','tantôt','tard','tôt','toujours','actuellement','immédiatement','incessamment','présentement','prochainement','soudainement','rarement','toujours','fréquemment','occasionnellement','habituellement']
lstAdverbeLieu =['ailleurs','alentour',"jusqu'à",'alentours','autrefois','arrière','avant','ça','céans','derrière','dessous','dessus','où','outre','partout','au-delà','au-dessous','au-dessus','au-devant','autour','ci','contre','ci-contre','ci-dessus','ci-dessous','ci-joint','deçà','en-deçà','dedans','dehors','devant','ici','là','là-haut','loin','près','proche','partout','sus','y']
lstAdverbeCerti = ['effectivement','manifestement','évidemment','immanquablement','hypothétiquement','possiblement','apparemment','assurément','bon','certainement','certes','en vérité','oui','peut-être','précisément','probablement','sans doute', 'si','soit','toutefois','vraiment','vraisemblablement','invraisemblablement']
lstAdverbeNég =['aucunement','guère','jamais','ne',"n'",'non','nullement','pas','plus','aucun','aucune','aucunement','rien']
lstAdverbeCs = ['donc','alors','pourquoi','ainsi','aussi','lorsque',"lorsqu'il"]

lstAdverbes = lstAdverbeMani + lstAdverbeQté + lstAdverbeTemps + lstAdverbeLieu + lstAdverbeCerti + lstAdverbeNég + lstAdverbeCs

lstConjCoor = ['mais','ou','et','donc','or','ni','car']

stoplist = lstPonctuations + lstArticles + lstPrépositions + lstPronoms + lstAdverbes + lstConjCoor

dico = []

with open('//usr/share/dict/french','r',encoding='utf8') as df: # on récupère le dico 'french' (linux)
	dico = df.read().splitlines()

#----------------------------------------------------------------------------
def piloteRobot(url,idx):
        
    r = requests.get(url)

    if r.ok:

        lstMotsPage = nettoie_page(r.text)

        indexePage(idx,lstMotsPage,url) # on indexe les mots de l'url

    else :

        print('erreur à l\'url ',url,' : ',r.reason)
        
                
def indexePage(idx,lstMots,url):
    
    for mot in lstMots : # pour chaque mot de la liste de mots prénettoyés (vides et doublons)
        
        mot = mot.lower() # conversion en minuscule
        
        if mot and mot not in stoplist : # si le mot, n'est pas pas dans la stoplist
            
            ajouteIndex(idx, mot, url)
        

def ajouteIndex(idx,mot,url) :
    
    if url not in idx : # si l'url n'est pas encore dans l'index
        
        idx[url]=[] # on initialise une liste vide de mots
        
    if mot not in idx[url] and mot in dico : # !ATTENTION! 2e condition rallonge beaucoup le temps de traitement
        
        idx[url].append(mot) # on ajoute le mot à l'url
        
#--------------------------------------------------------------------------------------------

#OBJECTIF : à partir d'un url récupérer récursivement tous les sous-urls (avec limite fixée)

urls = [] # on initialise la liste d'urls 

#On gère le nombre maximum de récursions autorisées

limit = sys.getrecursionlimit()

print('Le nombre limite de récursion par défaut est de : ',limit)

newLimit = 30

sys.setrecursionlimit(newLimit)

limit = sys.getrecursionlimit()

print('Le nombre limite de récursion est modifié en : ',limit)

# Puis on déclare la fonction récursive scrape

def scrape(url) :
    
    #global urls #on accède à la variable globale urls (facultatif)
        
    r = requests.get(url)
    
    if r.ok : # si ok on ouvre le contenu de l'url
    
        ssUrls = extraire_liens(r.text) # stocke la récup des sous-liens (liste) grâce à la fonction dédiée

        for ssUrl in ssUrls : # itère dans la liste des sous-liens

            url = ssUrl # stocke chaque sous-lien, un à un, sous la variable url -> réutilisée pour réitérer fonction

            if url not in urls : # si l'url n'est pas encore dans la liste :

                urls.append(url) # on ajoute son nom

                print(url) # on fait un print pour l'afficher à l'écran (vérif)

                if len(urls) <= 30 : # inutile car recursionlimit = 30 (sécurité supplémentaire)

                    scrape(url) # on rappelle la fonction elle-même

    else :
        
        print('problème de récupération de page à l\'',url,' : ',r.reason)

#----------------------------------------------------------------------------------------------

# Problème : la fonction 'scrape' risque de provoquer une erreur de récursion
# Solution : on utilise try (except else) finally -> https://www.pierre-giraud.com/python-apprendre-programmer-cours/gestion-exception-try-except-else/

try:

	scrape(sys.argv[1]) #ATTENTION sys.argv est un tableau avec [0] = objet lui-même

except RecursionError :

	print('ERREUR: Le nombre de récursions maximales fixé à ', sys.getrecursionlimit(),' a été atteint. Voici la liste des urls retenues : ', urls)
	
else:

	print('AVERTISSEMENT: Le nombre de récursions maximales est fixé à', sys.getrecursionlimit(), '. Il y a ', len(urls), ' urls retenues : ', urls)

finally:

	indexFinal = {}

	for site in urls :
		piloteRobot(site,indexFinal)

	for element in indexFinal: # offre une meilleure visualisation que print(indexFinal)
		print(element,':',indexFinal[element])
