'''
Authors: Willi Bobadilla & Yumi Kikuchi
Date: 13 March 2020
Description: Automation of file download and push to an specific repository.
* Run script everyday
'''

import os 
import kaggle

# using Kaggle API to download the dataset
kaggle.api.authenticate()
kaggle.api.dataset_download_files('imdevskp/corona-virus-report', path='/Users/yumikikuchi/Desktop/covid-19', unzip=True)

# git add and commit

filename = 'covid_19_clean_complete'
os.system('git add' + filename )
os.system("git commit -m 'updated data' ")
os.system('git push origin master')
