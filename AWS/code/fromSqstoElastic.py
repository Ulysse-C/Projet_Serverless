import boto3
import requests
import ast
import datetime
import time
from requests_aws4auth import AWS4Auth
import json

region = 'eu-west-3' # e.g. us-west-1
service = 'es'
credentials = boto3.Session().get_credentials()
awsauth = AWS4Auth(credentials.access_key, credentials.secret_key, region, service, session_token=credentials.token)

host = 'https://search-trial-6afrqj4qud37xogbrl55swfqbu.eu-west-3.es.amazonaws.com/' # the Amazon ES domain, including https://
type = 'lambda-type'
headers = { "Content-Type": "application/json" }

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
    r = requests.post(host +'/'+ index + '/_search', data=query, headers=headers)
    results = json.loads(r.text)
    result = None
    for hit in results['hits']['hits']: #The index exists
        result = formatDate(hit['_source']['Date'])
    if(result == None): #There is no index as specified, we query the DB without index
        r = requests.post(host + '/_search', data=query, headers=headers)
        results = json.loads(r.text)
        for hit in results['hits']['hits']:
            result = formatDate(hit['_source']['Date'])
    return result
    
def formatDate(date):
    format = '%Y-%m-%dT%H:%M:%S' # The format 
    datetime_str = datetime.datetime.strptime(date, format)
    return datetime_str 

def testDate(latestDate, dateParam): #True if date appends later than the latest date in the DB
        if(formatDate(dateParam) < latestDate):
            return False
        else:
            return True

# Lambda execution starts here
def handler(event, context):
    Records = event.get("Records")
    body = Records[0]['body']
    d = ast.literal_eval(body)
    body2 = d['Records'][0]['body']
    liste = ast.literal_eval(body2)
    types = liste['liste']['mixtr']['type']
    datedebut = liste['liste']['date_debut']
    for ty in types:
        if (ty['@granularite'] == 'Global'):                    
            valeurs = ty['valeur']
            index = ty['@v'].lower()
            url = host + '/' + index + '/' + type
            latestDate = defineLatestDate(index)
            #print(latestDate)
            for val in valeurs:
              if (val['#text'] != 'ND'):
                    hour = time.strftime('%H:%M:%S', time.gmtime(int(val['@periode'])*15*60))
                    date = datedebut + "T" + hour
                    v = {  
                            'value': int(val['#text']),
                            'Date': date
                        }
                    print(date)
                    if (testDate(latestDate, date)): #True if date appends later than the latest date in the DB
                        r = requests.post(url, auth=awsauth, json=v, headers=headers)
                        print(r.text)
  
