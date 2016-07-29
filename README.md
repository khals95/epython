# epython

Première étape: créer un compte gmail et avoir le script spreadsheet.py

Deuxième étape:  télécharger et installer l'IDE spyder (2.7)

Troisième étape: Activer le google sheet 

a.Aller dans le site des API google (console des API google) et créer un projet

b.Aller dans l'onglet identifiant et cliquer sur "créer des identifiants", "créer un ID client" , "Autre" et ecrire "Google Sheet API Quickstart" 

c.Cliquer sur l'icone "télécharger json" et renommer se fichier "client_secret.json"

d.Aller dans l'onglet "Ecrant d'autorisation OAuth" et assurer vous qu'il y a votre adresse mail et indiquer le nom de votre projet 

Quatriéme étape: opératons sur le terminal

a.Installer les librairies manquants en ecrivant sudo pip (ou pip2 ouo pip2.7 pour étre sur d'utiliser python 2.7) install oauth2client, pour installer oauth2client par exemple et pip install --upgrade google-api-python-client pour google api client

b.Executer python2.7 spreadsheed.py spreadsheetId

c.Le résultat se trouve dans le fichier file.json
