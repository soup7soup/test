from __future__ import print_function
import httplib2
import os

from apiclient import discovery

def main():
    
    API_KEY = '-The Key is secret-'
    discoveryUrl = ('https://sheets.googleapis.com/$discovery/rest?'
                    'version=v4')
    service = discovery.build(
        'sheets',
        'v4',
        http=httplib2.Http(),
        discoveryServiceUrl=discoveryUrl,
        developerKey=API_KEY)

    # Call the Sheets API
    SPREADSHEET_ID =  '11BCnspCt2Mut3nhc4WMY6CYTd0zF9C3eCzsk1AEpKLM'
    RANGE_NAME = 'sales!A1:E6'
    result = service.spreadsheets().values().get(spreadsheetId=SPREADSHEET_ID,
                                                range=RANGE_NAME).execute()
    values = result.get('values', [])

    if not values:
        print('No data found.')
    else:
        for row in values:
            print('%s, %s, %s, %s, %s' % (row[0], row[1], row[2], row[3], row[4]))

if __name__ == '__main__':
    from sys import argv

    if len(argv) == 2:
        main(key=argv[1])
    else:
        main()  
# [END]
