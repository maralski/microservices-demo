terraform {
  required_providers {
    newrelic = {
      source  = "newrelic/newrelic"
    }
  }
}

provider "newrelic" {
  api_key = var.NEW_RELIC_API_KEY
  account_id = var.NEW_RELIC_ACCOUNT_ID
  region = var.NEW_RELIC_REGION
}

resource "newrelic_workload" "sko-workload" {
    name = "Online-Boutique Store Workload"
    account_id = var.NEW_RELIC_ACCOUNT_ID
    entity_search_query {
        query = "(name like '%store-%' AND type = 'APPLICATION') OR type = 'KUBERNETES_POD' OR type ='CONTAINER' OR type = 'KUBERNETESCLUSTER'" 
    }

    scope_account_ids =  [var.NEW_RELIC_ACCOUNT_ID]
}