from __future__ import print_function
import httplib2
import os
import sys
import json
import argparse



import csv

from apiclient import discovery
import oauth2client
from oauth2client import client
from oauth2client import tools
# sur python2.7 sa marche bien
try: 
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_known_args(['--foo', 'BAR', 'spam'])#parse_args()
except ImportError:
    flags = None

# If modifying these scopes, delete your previously saved credentials
# at ~/.credentials/sheets.googleapis.com-python-quickstart.json
SCOPES = 'https://www.googleapis.com/auth/spreadsheets.readonly'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'Google Sheets API Python Quickstart'


def get_credentials():
    """Gets valid user credentials from storage.

    If nothing has been stored, or if the stored credentials are invalid,
    the OAuth2 flow is completed to obtain the new credentials.

    Returns:
        Credentials, the obtained credential.
    """
    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(home_dir, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir,
                                   'sheets.googleapis.com-python-quickstart.json')

    store = oauth2client.file.Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        if flags:
            credentials = tools.run_flow(flow, store, flags)
        else: # Needed only for compatibility with Python 2.6
            credentials = tools.run(flow, store)
        print('Storing credentials to ' + credential_path)
    return credentials
    


def main():
    """Shows basic usage of the Sheets API.

    Creates a Sheets API service object and prints the names and majors of
    students in a sample spreadsheet:
    https://docs.google.com/spreadsheets/d/1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgvE2upms/edit
                                           1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs740gvE2upms"""
    
    
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    discoveryUrl = ('https://sheets.googleapis.com/$discovery/rest?'
                    'version=v4')
    service = discovery.build('sheets', 'v4', http=http,
                              discoveryServiceUrl=discoveryUrl)
    argument1 = sys.argv[1]
    spreadsheetId =argument1#'1draZmK6PY4X52VwfGUlM-tVACS_ncwDPFN-6oSVpUes' # récupere le spreadshit id
    
    porteee='A:EZ'# de A a EZ soit 156 colonnes
    result = service.spreadsheets().values().get(
        spreadsheetId=spreadsheetId,range=porteee).execute()
   
    values = result.get('values',[])# valeurs du spreadshit
    
    if not values:
        print('No data found.')
    else:
        
    # ouvre un fichier csv contenant les valeurs
        with open('output.csv', "wb") as output:
          writer = csv.writer(output) 
          writer.writerows(values)
         # convertie le fichier csv en fichier json
        f = open('output.csv','r')
        reader = csv.DictReader(f)
        out = json.dumps( [ row for row in reader ] )
        jsonfile = open('file.json', 'w')
        jsonfile.write(out)

        
        
        
if __name__ == '__main__':
    main()
