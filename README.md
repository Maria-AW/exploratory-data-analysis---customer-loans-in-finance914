# Exploratory Data Analysis - Customer Loans in Finance

## Overview
This project involves extracting, cleaning, and analysing loan payment data to gain insights that inform decisions about loan approvals, pricing, and risk management in a large financial institution. The analysis is organised into milestones, each addressing a specific aspect of the data analysis process. This analysis will uncover patterns, relationships, and anomalies, providing a comprehensive understanding of the risk and return associated with the loans.

## Milestones

### Milestone 1
Creating 'RDSDatabaseConnector' in 'db_utils.py' to extract the loan payment data from a database on the cloud and load into a Pandas DataFrame. 

### Milestone 2
Gaining a deeper understanding of the data and identifing patterns. 
In this milestone, the data is reviewed and transformed using a 'DataTransform' class where there is missing or incorrectly formatted data. 
A 'DataFrameInfo' class was created to extract statistical values, identify nulls, distinct values and the shape. 
To gain further insight, a data visualisation class 'Plotter' and 'DataFrameTransform' class was created to identify and analyse missing or skewed data and outliers. 

### Milestone 3 
Now that the data has been transformed, deeper insights can be drawn from the dataset. 
The following analysis can be seen in notebook 'db_analysis_visualisation'. 
- Analysing recovered loans against investor funding and the total amount funded.
- Analysing charged-off loans historically and the total amount paid towards these loans before being charged off.
- Analysing the projected loss of charged-off loans and visualisations of the loss projected over the remaining term.
- Analysing possible loss through customers with late payments, and potential loss if status changes to Charged Off. 
- Analysing late payments further and projecting the loss if customers finish the full loan term.
- Analying indicators of different loan characteristics which may contributing to loans not being paid off.

## File Structure 
Please navigate to 'db_notebook.ipynb' for Milestones 1-2
Please navigate to 'db_analysis_visualisation.ipynb' for Milestones 3

## Contributing
If you would like to contribute or suggest improvements to the project, please feel free to submit a pull request.

## License information
This project is an open-source and available under the MIT Licence

## Conclusion
In this project I have gone through the process of extracting, cleaning, and analysing loan payment data, aiming to provide valuable insights into the financial dataset. Each milestone contributes to building a comprehensive understanding of the data, ensuring robust analysis and visualisation.