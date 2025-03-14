 #curl -X POST \
 #  -H "Content-Type: application/x-www-form-urlencoded" \
 #  -d "grant_type=client_credentials&client_id=$CLIENT_ID&client_secret=$CLIENT_SECRET&scope=https://management.azure.com/.default" \
 #  https://login.microsoftonline.com/$TENANT_ID/oauth2/v2.0/token



#!/bin/bash
# filepath: /home/srinman/git/azureexamplespriv/apim/clientcredflow.sh

# Request the access token
response=$(curl -s -X POST \
   -H "Content-Type: application/x-www-form-urlencoded" \
   -d "grant_type=client_credentials&client_id=$CLIENT_ID&client_secret=$CLIENT_SECRET&scope=https://management.azure.com/.default" \
   https://login.microsoftonline.com/$TENANT_ID/oauth2/v2.0/token)

# Extract the access token using jq
access_token=$(echo "$response" | jq -r '.access_token')
echo $access_token 


# Use the access token to call your APIM endpoint
curl -X GET \
   -H "Authorization: Bearer $access_token" \
   https://apimgateway.srinman.com/echo/resource?param1=sample