
# SI 507 Final Project - Tongyan Xu  
  
This project is a light website which can view some statistic data of national universities in US. Historical GDP data is also accessible and relationship between universities and GDP can be studied.  
<br>  
  
  
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
import requests  
resp = requests.get(url, headers={'User-Agent': 'Chrome/59.0.3071.115'})  
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
- Open the url above or the following url (*https://developers.google.com/places/web-service/get-api-key*), and click **< GET A KEY >**.  
- Follow the instructions until an API Key is obtained.  
- Open the local directory of this project, and open the **secret_file.py**.
	> **Local Path:** SI-507-Final-Project/project/secrets/secret_file.py  
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
>**Local Path:** SI-507-Final-Project/project/database/National_University.sqlite  
  
The program can **automatically** recognize and rebuild the database when the local database file is **lost**.   
  
The rebuilding process is **fast** when it is based on the **cache files**. If the cache files are also lost, the rebuilding process would be **very slow**.  
<br>  
  
  
# Plotting Setup  
  
**Ploy.ly** is used as the plotting API for this project. Before running the project, **Plotly API** is required. Read the following instructions for Plotly setup.  
  
## Obtain Plotly API Key  
  
1. Open https://plot.ly/. Create an account and log in.  

2. Enter **< Settings >** and find **< API Keys >**.  

3. Click **< Regenerate Key >** and copy the newly generated key.  

## Obtain Mapbox Access Token

1. Open https://www.mapbox.com/signin/?route-to=https://www.mapbox.com/studio/. Create an account and log in.

2. Enter **< Account >** and copy the Access Token.

## Enter Key & Access Token into Project  
  
1. Open local file **secret_file.py** using text editor.  
   >**Local Path:** SI-507-Final-Project/project/secrets/secret_file.py  
  
2. Paste the **Mapbox Access Token**, **Plotly API Key**, and enter the **Plotly Username** into the correct places.  

<br>  
  
  
# Project Structure  
  
## Framework & Other Sources  
  
**Framework:** Flask  
  
**Online JS Sources:**  
- Jquery  
- Plotly  
- DataTables  
  
**Online CSS Sources:**  
- BootStrap  
- DataTables  
  
## Files Structure (*Short Description*)  
  
- **SI-507-Final-Project**  
	- **documents** (*project proposal*)  
		- **SI507_Final_Project_Proposal.docx**  
		- **SI507_Final_Project_Proposal.pdf**  
		- **SI507_Final_Project_Proposal_Simple.txt**  
	- **project** (*project data & python files*)  
		- **cache** (*cache files*)  
			- **national_university_gps.json**  
			- **national_university_info.json**  
		- **database** (*organized database*)  
			- **National_University.sqlite**  
		- **rawData** (*raw data files*)  
			- **GDP_by_state.csv***  
			- **state_abbr.json***  
		- **scripts** (*main python scripts*)  
			- **cacheOperation.py** (*cache operations: load & save cache*)  
			- **classDef.py** (*class definitions: class NationalUniversity*)  
			- **dbOperation.py** (*database operations: creating table & inserting data & getting data for presentation*)  
			- **gdpData.py** (*build GDP_State table in database*)  
			- **plotFunc.py** (*functions to plot using Plotly*)  
			- **stateAbbrData.py** (*build GDP_State table in database*)  
			- **tableFunc.py** (*functions to prepare data for DataTables*)  
			- **universityData.py** (*build GDP_State table in database*)  
		- **secrets** (*secret files*)  
			- **secret_file.py** (*API keys & Access Token*)  
		- **tests** (*test files*)  
			- **test_file.py** (*unittest file*)  
	- **static** (*CSS files & JS files & images*)  
		- **css** (*CSS files*)  
			- **common.css** (*common style for title and foot in all pages*)  
			- **index.css** (*specific style for index page*)  
			- **plot-page.css** (*specific style for plot page*)  
			- **table.css** (*specific style for DataTables*)  
			- **table-page.css** (*specific style for table page*)  
		- **img** (*images*)  
			- **bar.png**  
			- **bubble.png**  
			- **gdp.jpg***  
			- **histo.png**  
			- **line.png**  
			- **map.png**  
			- **scatter.png**  
			- **um.jpg***  
			- **univ.svg***  
		- **js** (*JS files*)  
			- **jquery-3.2.1.min.js*** (*official Jquery JS file*)  
			- **plot.js** (*functions for plot page*)  
			- **plotly-latest.min.js*** (*official Plotly JS file*)  
			- **table.js** (*functions for table page*)  
	- **templates** (*HTML files*)  
		- **index.html** (*index*)  
		- **plot.html** (*plot guide page*)  
		- **table.html** (*table guide page*)  
		- **table_data.html** (*template of national university table & state GDP table*)
	- **.gitignore**  
	- **README.md**  
	- **requirements.txt** (*modules required for the project*)  
	- **run.py** (*run the whole project intelligently*)  
	- **setup.py** (*setup / run the whole project typically*)
  
## Important Python Functions (or Files)  
  
**get_national_university_data**  
This function is used to extract national university info from HTML structures that requested from US News websites. Caching mechanism is not considered in this function but is included in its parent functions.  
>**Defined at:** SI-507-Final-Project/project/scripts/universityData.py   

**plotFunc.py**  
**All functions** in this file are used to get necessary data from the database and create **HTML ``<div>``** containing information of plots, through Plotly offline plotting.  
>**Local Path:** SI-507-Final-Project/project/scripts/plotFunc.py  
  
**tableFunc.py**  
**All functions** in this file are used to get necessary data from the database and create **JSON** strings containing information for DataTables.  
>**Local Path:** SI-507-Final-Project/project/scripts/tableFunc.py  
  
## Important Python Classes (or Files)  
  
**NationalUniversity**  
Each instance represents a **national university** in US with all features extracted from the US News websites.  
While creating instances using parsed data, the class **__ init __** method will automatically make request to Google Places API and get the GPS info for the university.  
>**Defined at:** SI-507-Final-Project/project/scripts/classDef.py   

**Database**  
Each instance is a **database operator** which can create tables, insert rows, and get data for presentation purposes. Large amount of methods are defined in the class.   
Method **__ init __** will create a database **connection** and a **cursor**, and assign them to two variables of instances. **__ enter __** and **__ exit __** methods are also defined to **close** existing database connection once the instance is abandoned.  
While database operation is required, simply type the following codes:  
```python  
from project.scripts.dbOperation import Database  
with Database() as db_operator:  
 # <any method of db_operator can be used here>  
# db_operator is abandoned and the database connection is closed  
```  
>**Defined at:** SI-507-Final-Project/project/scripts/dbOperation.py   
## Important JavaScript Functions (or Files)  
  
**plot.js**  
Several **AJAX** based functions used to access data and create plots.  
>**Local Path:** SI-507-Final-Project/static/js/plot.js  
  
**table.js**  
Two **DataTables** (**AJAX** is also used) based functions used to access data and create tables.  
Ordering algorithm is re-programmed in the file due to special forms of data, which means:
- correctly order '231 - 300' & 'Unranked' in university ranking column
- keep empty cells always at the bottom regardless of whether an ascending or a descending order is applied)
>**Local Path:** SI-507-Final-Project/static/js/table.js  
  
<br>  
  
  
# User Guide  

## Project Environment  
  
This project is programmed under **Python 3.6.4**.  
All **Python3** should be fine for running the project.
  
## Module requirements
 
- **flask** -- *v0.12.2*  
- **plotly** -- *v2.5.1*  
- **requests** -- *v2.18.4*  
- **bs4** -- *v0.0.1*  

Main modules are listed above. Check **requirements.txt** for more details.
> **Local Path:** SI-507-Final-Project/requirements.txt

The project can automatically install (using pip) to install the missing required modules after getting user's permission. See **Running** for more details.
	
	

## Before Running

1. Complete **secret_file.py**.
	- **Username and API Key for Plotly** is **required** for plotting.
	- **API Key for Mapbox** is **required** for map plotting.
	- **Google Places API Key** is **suggested** to be filled in, but **not required**.
	> **Local Path:** SI-507-Final-Project/project/secrets/secret_file.py

2. Open **Terminal** and cd to the **root directory**.
		``> cd SI-507-Final-Project/``

3. Install modules before running (*Optional*).
	Two ways to install modules before running the project.
	
	1.  ``> pip3 install flask``
		``> pip3 install plotly``
		``> pip3 install requests``
		``> pip3 install bs4``
		
	2. ``> pip3 install -r requirements.txt``

## Running

- **Run the project typically** (*All modules need to be installed before*).  
   ``> python3 setup.py``  
  
- **Run the project intelligently**.  
   ``> python3 run.py``  
   1. Select mode.  
       User will be asked whether use current environment or virtual environment to run the project.  
       ``Run the project under: (1/2)``
       ``1. Current environment``
       ``2. Virtual environment``  
       If the answer is '1', see step 2.   
       If the answer is '2', see step 3.   
       If the answer is neither '1' nor '2', the project will ask again.  
       
   2. **Current Environment**: 
       The project will be run under current environment, no matter if virtual environment is using or not.
   
	   If any required module is not found, user will be asked whether or not to install the module. 

	   Example:  
       ``Module <flask> is not found. Would you like to pip install it? (y/n) ``  
       If the answer is 'y', the project will automatically install this module.   
       If the answer is 'n', the project will not install this module and but stop.   
       If the answer is neither 'y' nor 'n', the project will ask again.  
   
   3. **Virtual Environment**:
       The project will automatically create a virtual environment with all required packages in it. And then, the project will be run under newly created virtual environment.

	   If an existed virtual environment is found, user will be asked whether or not to use this virtual environment. 

	   Example:  
       ``Existing virtual environment is found. Use it? (y/n) ``
       If the answer is 'y', the project will use the existing virtual environment (may cause **ERROR** if the existing environment is not created by the project or is modified).  
       If the answer is 'n', the project will delete the existing virtual environment and create a new one.   
       If the answer is neither 'y' nor 'n', the project will ask again.  
  
- **Terminate the project**.  
   ``>  [ Ctrl + C ]``
  
  <br>