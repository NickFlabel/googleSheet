import httplib2
import googleapiclient.discovery
from oauth2client.service_account import ServiceAccountCredentials

CREDENTIALS_FILE = 'sheet/ExternalAPI/credentials.json'
spreadsheet_id = '133naqQSTKdiMjNDL6NmrjkWqS0PoNrfh-e8xbAbd1IQ'

def get_sheet(id:str=spreadsheet_id):
    """This function fetches the sheet with the given id in form of list of lists
    """


    credentials = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_FILE,
                                                                   ['https://www.googleapis.com/auth/spreadsheets',
                                                                    'https://www.googleapis.com/auth/drive'])
    httpAuth = credentials.authorize(httplib2.Http())
    service = googleapiclient.discovery.build('sheets', 'v4', http=httpAuth)

    values = service.spreadsheets().values().get(
        spreadsheetId=id,
        range="Лист1"
    ).execute()
    return values['values'][1:]


