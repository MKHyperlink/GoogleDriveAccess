
# GoogleDriveAccess

## Access to google spreadsheet content.**(Support Python 3 in branch python3.0)**

### Dependent module:  
(Maybe needs sudo)

1. Google APIs Client Library => pip install --upgrade google-api-python-client  
	(If you install google-api-python-client fail in macOS, try to use 'pip install --user --upgrade google-api-python-client.)

### Execute steps:

1. Create a project in Google Console(shoul be enable Drive API) and generate your own "client_secrets.json" file. 
2. \>> python googleDriveAccess.py
3. Copy Google Sheet File_ID and paste to console.
4. Copy Access Token from browser and paste to console.
5. Got exported file.

### Settings:

1. Open googleDriveAccess.py
2. Modify  
	FILE_NAME: the name what you want to save for file. Default file name is: language.csv <br>
	SAVE_PATH: the path where file to save.  Default path is: ./ <br>
	FILE_ID: Google spreadsheet file_id got from page URL. If you left this blank, you need input every time when execute googleDriveAccess.py

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
	3). Use virtualenv<br>
	4). Use pip install --user 
