# SI 507 Final Project - Tongyan Xu

This project is a light website which can view some statistic data of national universities in US. Historical GDP data is also accessible and relationship between universities and GDP can be studied.


# Data Source

## US News < HTML >

**URL:** https://www.usnews.com/best-colleges/rankings/national-universities

**Detail:**
- Obtain interesting info of National Universities which are listed on US News site.
- 13 features are considered:  name, ranking, state, city, type, found year, endowment, tuition and fees, and etc.
- Need to parse 311 universities listed on 16 pages.
- For each university, 3 pages are required to obtain all interested features / info.
- Totally 949 pages of HTML are requested.

**Local Path:** SI-507-Final-Project/project/cache/national_university_info.json

**Access Requirement:** HTML header (*See instructions below*)

**Access Instruction:**
- Pretend to be a web browser while making a request to the website.
- Sample code:
```python
resp = requests.get(url, headers={'User-Agent': Chrome/59.0.3071.115'})
```
- For project user, nothing is required to do, since these codes are already programmed into the script. **Just use it**.

**Challenge Point:** 8 / 10

## Google Places < API >

**URL:** https://developers.google.com/places/web-service/search

**Detail**:
- Obtain latitude - longitude data for each university for plotting them on the map.
- 1 request for each university.
- 311 requests are needed totally.

**Local Path:** SI-507-Final-Project/project/cache/national_university_gps.json

**Access Requirement:** Google Places API Key (*See instructions below*)

**Access Instruction:**
- Open the url above or the following url (*https://developers.google.com/places/web-service/get-api-key*), and press the **< GET A KEY >**.
- Follow the instructions until an API Key is obtained.
- Open the local directory of this project, and open the secret_file.py (*SI-507-Final-Project/project/secrets/secret_file.py*).
- Copy and paste the API Key into the correct place in the file.
- For project user, you would be suggested to do so **only if** both the local database file and the GPS cache file are lost.

**Challenge Point:** 2 / 10

## US BEA < CSV File >

**URL:** https://www.bea.gov/iTable/iTable.cfm?reqid=70&step=1&isuri=1&acrdn=2#reqid=70&step=4&isuri=1&7003=200&7001=1200&7002=1&7090=70

**Detail:**
- Obtain GDP data for each state from 1997 to 2016. (*past 20 years, unit: million dollars*)
- Directly extract data from CSV file. (*61 rows * 22 columns*)

**Local Path:** SI-507-Final-Project/project/rawData/GDP_by_state.csv

**Access Requirement:** None

**Challenge Point:** 0 / 10

## Github < JSON File >

**URL:** https://gist.githubusercontent.com/mshafrir/2646763/raw/8b0dbb93521f5d6889502305335104218454c2bf/states_hash.json

**Detail:**
- Obtain corresponding relations between two-letter abbreviations and full names of each state.
- Directly extract data from CSV file. (*59 records*)

**Local Path:** SI-507-Final-Project/project/rawData/state_abbr.json

**Access Requirement:** None

**Challenge Point:** 0  / 10

## Local Database ##

**All Data Listed Above Can be Found in Local Database File.**
**Local Path:** SI-507-Final-Project/project/database/National_University.sqlite


# Plotting Setup

**Ploy.ly** is used as the plotting API for this project. Before running the project, **Plotly API** is required. Read the following instructions for Plotly setup.

## Obtain Plotly API Key

## Enter Key into Project


# Project Structure

## Files Structure
- SI-507-Final-Project
	- documents (*project proposal*)
		- SI507_Final_Project_Proposal.docx
		- SI507_Final_Project_Proposal.pdf
		- SI507_Final_Project_Proposal_Simple.txt
	- project (*project data & python files*)
		- cache (*cache files*)
			- national_university_gps.json
			- national_university_info.json
		- database (*organized database*)
			- National_University.sqlite
		- rawData (*raw data files*)
			- GDP_by_state.csv*
			- state_abbr.json*
		- scripts (*main python scripts*)
			- cacheOperation.py (*cache operations: load & save cache*)
			- classDef.py (*class definitions: class NationalUniversity*)
			- dbOperation.py (*database operations: creating table & inserting data & getting data for presentation*)
			- gdpData.py (*build GDP_State table in database*)
			- plotFunc.py (*functions to plot using Plotly*)
			- stateAbbrData.py (*build GDP_State table in database*)
			- tableFunc.py (*functions to prepare data for DataTables*)
			- unittestFile.py (*unittest*)
			- universityData.py (*build GDP_State table in database*)
		- secrets (*secret files*)
			- secret_file.py (*API keys*)
	- static (*CSS files & JS files & images*)
		- css (*CSS files*)
			- common.css (*common style for title and foot in all pages*)
			- index.css (*specific style for index page*)
			- plot-page.css (*specific style for plot page*)
			- table.css (*specific style for DataTables*)
			- table-page.css (*specific style for table page*)
		- img (*images*)
			- bar.png
			- bubble.png
			- gdp.jpg*
			- histo.png
			- line.png
			- map.png
			- scatter.png
			- um.jpg*
			- univ.svg*
		- js (*JS files*)
			- jquery-3.2.1.min.js* (*official Jquery JS file*)
			- plot.js (*functions for plot page*)
			- plotly-latest.min.js* (*official Plotly JS file*)
			- table.js (*functions for table page*)
	- templates (*HTML files*)
		- index.html (*index*)
		- plot.html (*plot guide page*)
		- table.html (*table guide page*)
		- table_gdp.html (*state GDP table page*)
		- table_univ.html (*national university table page*)
	- venv (*content neglected*)
	- .gitignore
	- README.md
	- setup.py (*run the whole project*)

## Virtual Environment

This project is programmed in **Python3**.

**Python 3.6.2** is included in the virtual environment.
>**Local Path:** SI-507-Final-Project/venv

**Additional packages** listed below is required and is included in the virtual environment:
- flask -- *v0.12.2*
- plotly -- *v2.5.1*
- requests -- *v2.18.4*
- bs4 -- *v0.0.1*

## Important Files

## Important Functions

## Important Classes


# User Guide