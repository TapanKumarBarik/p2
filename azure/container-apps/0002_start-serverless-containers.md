# Azure Container Apps: Key Features

Azure Container Apps makes it easy to manage the following:

## 1. Automatic scaling

As requests for your applications fluctuate, Container Apps keeps the system running even during periods of high demand. It automatically creates new copies of your container, called replicas, to handle the traffic. When demand decreases, it removes the unnecessary replicas.

## 2. Security

Application security is enforced at multiple layers, from authentication and authorization to network-level protection. Container Apps lets you control which users and requests are allowed into your system.

## 3. Monitoring

You can easily monitor the health of your container app using built-in observability tools in Azure Container Apps.

## 4. Deployment flexibility

You can deploy your app from GitHub, Azure DevOps, or your local machine.

## 5. Version control and rollback

As your containers evolve, Azure Container Apps stores each change as a revision. If a deployment causes issues, you can easily roll back to an earlier version.

## Summary

Azure Container Apps helps you run containerized apps with automatic scaling, strong security, monitoring, flexible deployment options, and easy rollback support.




#  Build and deploy from local source code to Azure Container Apps


export RESOURCE_GROUP="album-containerapps"
export LOCATION="canadacentral"
export ENVIRONMENT="env-album-containerapps"
export API_NAME="album-api"

git clone https://github.com/azure-samples/containerapps-albumapi-python.git
cd containerapps-albumapi-python/src

az group create --name $RESOURCE_GROUP --location $LOCATION

az containerapp up \
  --name $API_NAME \
  --resource-group $RESOURCE_GROUP \
  --location $LOCATION \
  --environment $ENVIRONMENT \
  --source .


az group delete --name $RESOURCE_GROUP