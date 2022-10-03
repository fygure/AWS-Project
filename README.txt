Hello

#create venv

$pip install boto3

#save dependencies in requirements.txt
$pip freeze >> requirements.txt


#If accidentally pushed .env file do below
$git filter-branch --index-filter "git rm -rf --cached --ignore-unmatch .env" HEAD


#If accidentally added .env file to git do below
$git rm -r --cached .env
