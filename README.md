
# GoogleDriveAccess
Access to google spreadsheet content.

### Dependent module:  
(Maybe needs sudo)

1. Google APIs Client Library => pip install --upgrade google-api-python-client  
	(The version of google-api-python-client above 1.4.0 will install fail on macOS El Capitan and above. <br> 
Please downgrade install => pip install -I google-api-python-client==1.3.2 <br>
reference:<http://stackoverflow.com/questions/29190604/attribute-error-trying-to-run-gmail-api-quickstart-in-python>)
2. Httplib2 => pip install httplib2

### Execute steps:

1. Create a project in Google Console(shoul be enable Drive API) and generate your own "client_secrets.json" file. <br>
	(Reference:<https://github.com/jay0lee/GAM/wiki/Creating-client_secrets.json-and-oauth2service.json>)
2. python googleDriveAccess.py
3. Copy Google Sheet File_ID and paste to console.
4. Copy Access Token from browser and paste to console.
5. Got exported file.

### Settings:

1. Open googleDriveAccess.py
2. Modify  
	FILE_NAME: file name for save  
	SAVE_PATH: the path for save file  
	FILE_ID: Google spreadsheet file_id got from page address  

### NOTICE:

1. If you got AttributeError: 'Module_six_moves_urllib_parse' on earlier versoin than macOS El Capitan. Try to execute following command  
	=> easy_install --upgrade six  
2. The "six module" was fixed in v1.4.1 in macOS default python library since El Capitan and we can not change/upgrade it.  <br>
	Referenc:<http://stackoverflow.com/questions/29485741/unable-to-upgrade-python-six-package-in-mac-osx-10-10-2>

	We can check the Six module version by following steps:  
>  	a. pip show six  
>  	b. $ python  
>		\>> import six; six.\__version__  <br>
3. The google-api-python-client use the v1.5+ of "six module" after v1.3.2, hence we have few choice: <br>
	1). Use older version google-api-python-client v1.3.2 <br>
	2). homebrew install python. (Don't use deault python on macOS install new one)<br>
	3). using a virtualenv
