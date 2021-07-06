# Phantomdron
## Proof of concept
### Design and implement a solution architecture for the new platform

![alt text](https://github.com/rakamahatta/phantomdron/blob/main/design_poc.jpg?raw=true)


Resources are based on PaaS and SaaS solutions on Azure.  

Application is installed on App Service with Docker image 4.8.4. Application backends are Storage account file share for content files and Azure Database for MySQL Server for application database.  

For the purpose of geo-redundancy Front Door with Web Application Firewall policy is deployed with backend pool of two identical App Services located in primary and secondary region in active-standby mode. Direct web access to App Services is not allowed. Both Front Door endpoint and App Services have session affinity mode enabled.  

Storage account is defined as Read-Access geo-redundant storage (RA-GRS) and production Azure Database for MySQL Server has geo-redundant replication configured in standby region. Because of this General Purpose SKU is required for the production database.  

Autoscaling requirement with up to 4 instances is configured for both region based Application Service Plans if the CPU load is greater then 70% for the defined period of time of 10 minutes. Scale in will be performed if CPU load is less then 30% for 10 minutes. Minimal number of instances is one.  

For development environment App Service Slot with same Docker image version is defined and with separate site configuration parameters. DevOps team will use this Slot to work on the application with separate development Azure Database for MySQL and file share. This database is from Basic SKU due to the cost optimization requirement.  

Because of autoscaling and 5 Application Slots requirements Standard S1 App Service Plan SKU in production is minimal option.

Application insight is configured for the production application in order to provide additional information for DevOps team.  
Function App with Consumption SKU App Service plan is deployed for the purpose of maintenance scripts.

All App Services have system managed identities enabled as requirement for Key Vault access policy where all passwords are stored as secrets. All resources have configured diagnostics settings with destination of Log Analytics Workspace.  


This template creates all resources defined for this proof of concept.  

[![Deploy to Azure](https://aka.ms/deploytoazurebutton)](https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2Frakamahatta%2Fphantomdron%2Fmain%2Fazuredeploy.json)
