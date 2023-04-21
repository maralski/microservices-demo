import requests
import json
import os

app_guid = ""
endpoint = "https://api.eu.newrelic.com/graphql" if os.environ['TF_VAR_NEW_RELIC_REGION'] == "EU" else  "https://api.newrelic.com/graphql"


def nerdgraph_createkeytxn_cartapp(key):
  # GraphQL query to NerdGraph
  query = """
  mutation {
    keyTransactionCreate(apdexTarget: 0.5, 
                        applicationGuid: \"""" + app_guid + """", 
                        browserApdexTarget: 7, 
                        metricName: "WebTransaction/ASP/hipstershop.CartService/AddItem", 
                        name: "WebTransaction/ASP/hipstershop.CartService/AddItem"){
    apdexTarget
    browserApdexTarget
    guid
    metricName
    name
   }
   }"""

  headers = {'API-Key': f'{key}'}
  response = requests.post(endpoint, headers=headers, json={"query": query})

  if response.status_code == 200:
    dict_response = json.loads(response.content)
    print(dict_response)

  else:
    raise Exception(f'Nerdgraph query failed with a {response.status_code}.')


def nerdgraph_createkeytxn_checkoutapp(key):
  # GraphQL query to NerdGraph
  query = """
  mutation {
    keyTransactionCreate(apdexTarget: 0.5, 
                        applicationGuid: \"""" + app_guid + """", 
                        browserApdexTarget: 7, 
                        metricName: "WebTransaction/Go/hipstershop.CheckoutService/PlaceOrder", 
                        name: "WebTransaction/Go/hipstershop.CheckoutService/PlaceOrder"){
    apdexTarget
    browserApdexTarget
    guid
    metricName
    name
   }
   }"""

  headers = {'API-Key': f'{key}'}
  response = requests.post(endpoint, headers=headers, json={"query": query})

  if response.status_code == 200:
    dict_response = json.loads(response.content)
    print(dict_response)

  else:
    raise Exception(f'Nerdgraph query failed with a {response.status_code}.')


def nerdgraph_createkeytxn_paymentapp(key):
  # GraphQL query to NerdGraph
  query = """
  mutation {
    keyTransactionCreate(apdexTarget: 0.5, 
                        applicationGuid: \"""" + app_guid + """", 
                        browserApdexTarget: 7, 
                        metricName: "WebTransaction/WebFrameworkUri/gRPC//hipstershop.PaymentService/Charge", 
                        name: "WebTransaction/WebFrameworkUri/gRPC//hipstershop.PaymentService/Charge"){
    apdexTarget
    browserApdexTarget
    guid
    metricName
    name
   }
   }"""

  headers = {'API-Key': f'{key}'}
  response = requests.post(endpoint, headers=headers, json={"query": query})

  if response.status_code == 200:
    dict_response = json.loads(response.content)
    print(dict_response)

  else:
    raise Exception(f'Nerdgraph query failed with a {response.status_code}.')


def nerdgraph_getappguid(key,appName,accountId):
  # GraphQL query to NerdGraph
  global app_guid
  query = """
  {
  actor {
    entitySearch(queryBuilder: {name: \"""" + appName + """\", tags: {key: "accountId", value: \"""" + accountId + """\"}}) {
      count
      query
      results {
        entities {
          guid
        }
      }
    }
  }
}"""

  headers = {'API-Key': f'{key}'}
  response = requests.post(endpoint, headers=headers, json={"query": query})

  if response.status_code == 200:
    dict_response = json.loads(response.content)
    app_guid = dict_response["data"]["actor"]["entitySearch"]["results"]["entities"][0]["guid"]
    print(appName)
    print(app_guid)

  else:
    raise Exception(f'Nerdgraph query failed with a {response.status_code}.')


cartapp_name = "store-cartservice"
checkoutapp_name = "store-checkoutservice"
paymentapp_name = "store-paymentservice"

nerdgraph_getappguid(os.environ['TF_VAR_NEW_RELIC_API_KEY'],cartapp_name,os.environ['TF_VAR_NEW_RELIC_ACCOUNT_ID'])
nerdgraph_createkeytxn_cartapp(os.environ['TF_VAR_NEW_RELIC_API_KEY'])
nerdgraph_getappguid(os.environ['TF_VAR_NEW_RELIC_API_KEY'],checkoutapp_name,os.environ['TF_VAR_NEW_RELIC_ACCOUNT_ID'])
nerdgraph_createkeytxn_checkoutapp(os.environ['TF_VAR_NEW_RELIC_API_KEY'])
nerdgraph_getappguid(os.environ['TF_VAR_NEW_RELIC_API_KEY'],paymentapp_name,os.environ['TF_VAR_NEW_RELIC_ACCOUNT_ID'])
nerdgraph_createkeytxn_paymentapp(os.environ['TF_VAR_NEW_RELIC_API_KEY'])
