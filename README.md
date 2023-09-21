<p align='center'>
<img src='https://github.com/waqarg2001/earthquake-etl-pipeline/blob/main/Resources/logo.png' width=630 height=290 >
</p>

---

<h4 align='center'> Leveraging <a href='https://azure.microsoft.com/en-us' target='_blank'>Azure Cloud Services,</a> a daily data pipeline is in action, fetching and transforming earthquake data with a magnitude of 4.5 or higher. The pipeline taps into the <a href='https://earthquake.usgs.gov'>United States Geological Survey (USGS) </a> as its source, delivering real-time insights into earthquake activity over the past 7 days.</h4>

<p align='center'>
<img src="https://i.ibb.co/KxfMMsP/built-with-love.png" alt="built-with-love" border="0">
<img src="https://i.ibb.co/MBDK1Pk/powered-by-coffee.png" alt="powered-by-coffee" border="0">
<img src="https://i.ibb.co/CtGqhQH/cc-nc-sa.png" alt="cc-nc-sa" border="0">
</p>

<p align="center">
  <a href="#overview">Overview</a> •
  <a href="#tools">Tools</a> •
  <a href="#architecture">Architecture</a> •
  <a href="#dashboard">Dashboard</a> •
  <a href="#support">Support</a> •
  <a href="#license">License</a>
</p>


## Overview


Earthquake Data Analysis is an extensive project leveraging the capabilities of Azure services and GitHub to streamline the collection, processing, and analysis of critical earthquake data. Drawing inspiration from similar projects, this endeavor seamlessly acquires data from the United States Geological Survey (USGS) and applies Azure Data Factory for efficient ETL (Extract, Transform, Load) operations. The data is then deposited into Azure Data Lake Storage Gen2 for centralized storage and further undergoes transformations and exploratory analysis using Azure Databricks. Azure Key Vault plays a pivotal role in ensuring the security of sensitive credentials and secrets. Processed data is stored in an Azure SQL Database for optimized querying, with Azure Data Lake Gen2 serving as an intermediary and repository for refined datasets. Ultimately, the project utilizes Tableau to create dashboards that offer valuable insights into recent seismic activities.



The repository directory structure is as follows:

```
├── Dashboards            <- Includes tableau dashboards. 
|   ├── historical_dashboard.twb      <- historical earthquakes dashboard
│   │
│   ├── usgs_dashboard.twb            <- past 7 days earthquakes dashboard
│
|
├── Resources             <- Contains resources for this readme file.
│
│  
├── databricks notebooks             <- Scripts to aggregate and transform data
|   ├── Configurations           <- configurations used for mounting ADLS and for key vault.
│   │ 
│   ├── Transformations          <- transformation notebooks 
│   
|         
├── dataset         <- Includes datasets created in ADF.
│   
├── linkedService    <- Includes linkedServices created in ADF.
│
├── pipeline    <- Holds pipelines created in ADF.
│
├── trigger    <- Holds scheduled trigger(daily) created in ADF
│
├── README.md    <-The top-level README for developers using this project
```

## Tools 

To build this project, the following tools were used:

- Azure Databricks
- Azure KeyVault
- Azure Active Directory
- Azure DataLake Gen 2
- Azure Blob Storage
- Azure Data Factory
- Azure SQL Database
- Azure Monitor
- Azure Cost & Billing
- Tableau
- Pyspark
- SQL
- Git

## Architecture

Following is the architecture of the project.

<p align='center'>
  <img src='https://github.com/waqarg2001/earthquake-etl-pipeline/blob/main/Resources/architecture.png' height=385 width=1100>
</p>  

## Dashboard

These are the dashboards made in Tableau. 

Tableau Public Links: 

<a href='https://public.tableau.com/app/profile/muhammad.waqar.gul/viz/earthquake_dashboard_16952292430070/Dashboard1'>USGS Earthquake Dashboard</a>

<a href='https://public.tableau.com/app/profile/muhammad.waqar.gul/viz/historical_earthquake_dashboard/Dashboard12'>Historical Earthquake Dashboard</a>

<p align='center'>
  <img src='https://github.com/waqarg2001/earthquake-etl-pipeline/blob/main/Resources/usgs_dashboard.png' height=400 width=650>
</p>  

<p align='center'>
  <img src='https://github.com/waqarg2001/earthquake-etl-pipeline/blob/main/Resources/hist_dashboard.png' height=400 width=650>
</p>  


## Support

If you have any doubts, queries, or suggestions then, please connect with me on any of the following platforms:

[![Linkedin Badge][linkedinbadge]][linkedin] 
[![Gmail Badge][gmailbadge]][gmail]


## License

<a href = 'https://creativecommons.org/licenses/by-nc-sa/4.0/' target="_blank">
    <img src="https://i.ibb.co/mvmWGkm/by-nc-sa.png" alt="by-nc-sa" border="0" width="88" height="31">
</a>

This license allows reusers to distribute, remix, adapt, and build upon the material in any medium or format for noncommercial purposes only, and only so long as attribution is given to the creator. If you remix, adapt, or build upon the material, you must license the modified material under identical terms.



<!--Profile Link-->
[linkedin]: https://www.linkedin.com/in/waqargul
[gmail]: mailto:waqargul6@gmail.com

<!--Logo Link -->
[linkedinbadge]: https://img.shields.io/badge/waqargul-0077B5?style=for-the-badge&logo=linkedin&logoColor=white
[gmailbadge]: https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white
