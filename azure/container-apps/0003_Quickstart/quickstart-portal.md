### Deploy your first container app using the Azure portal


https://learn.microsoft.com/en-us/azure/container-apps/quickstart-portal



### Deploy your first container app using the cmd line

az login

az upgrade


az extension add --name containerapp --upgrade


az extension add --name containerapp --upgrade --allow-preview true


az provider register --namespace Microsoft.App

az provider register --namespace Microsoft.OperationalInsights

```
az containerapp up \
  --name my-container-app \
  --resource-group my-container-apps \
  --location centralus \
  --environment 'my-container-apps' \
  --image mcr.microsoft.com/k8se/quickstart:latest \
  --target-port 80 \
  --ingress external \
  --query properties.configuration.ingress.fqdn
``` 


az group delete --name my-container-apps


### Build and deploy from local source code to Azure Container Apps