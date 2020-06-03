import json
import time
import datetime
import requests

host = "https://quickstart-es-http:9200"
typeData = 'lambda-type'
headers = { "Content-Type": "application/json" }
password = "XXXX"


def defineLatestDate(index):
    query = json.dumps( {
      "query": {
        "match_all": {}
        },
        "size": 1,
        "sort": [
            {
                "Date": {
                    "order": "Desc"
                    }
            }
        ] 
    })
    r = requests.post(host +'/'+ index + '/_search', auth=('elastic', password), data=query, headers=headers, verify=False)
    results = json.loads(r.text)
    result = None
    if(list(results.keys())[0] == "error"):
        return datetime.datetime.strptime('2000-01-01T00:00:00', '%Y-%m-%dT%H:%M:%S')
    for hit in results['hits']['hits']: #The index exists
        result = formatDate(hit['_source']['Date'])
    if(result == None): #There is no index as specified, we query the DB without index
        r = requests.post(host +'/'+ index + '/_search', auth=('elastic', password), data=query, headers=headers, verify=False)
        results = json.loads(r.text)
        for hit in results['hits']['hits']:
            result = formatDate(hit['_source']['Date'])
    return result
    

def formatDate(date):
    format = '%Y-%m-%dT%H:%M:%S' # The format 
    datetime_str = datetime.datetime.strptime(date, format)
    return datetime_str 


def testDate(latestDate, dateParam): #True if date appends later than the latest date in the DB
    if(formatDate(dateParam) <= latestDate):
        return False
    else:
        return True




  
    
def handler(event, context):
    liste = event['data']
    types = liste['liste']['mixtr']['type']
    datedebut = liste['liste']['date_debut']
    for ty in types:
        if (ty['granularite'] == 'Global'):                    
            valeurs = ty['valeur']
            index = ty['v'].lower()
            url = host+ '/' + index + '/' + typeData
            latestDate = defineLatestDate(index)
            for val in valeurs:
              if (val['$t'] != 'ND'):
                hour = time.strftime('%H:%M:%S', time.gmtime(int(val['periode'])*15*60))
                date = datedebut + "T" + hour
                v = {  
                            'value': int(val['$t']),
                            'Date': date
                        }
                if (testDate(latestDate, date)): #True if date appends later than the latest date in the DB
                    r = requests.post(url, auth=('elastic', password), json=v, headers=headers, verify=False)
