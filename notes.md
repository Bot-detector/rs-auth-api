
## api documentation
```
http://127.0.0.1:8000/docs
http://127.0.0.1:8000/redoc
```
## extra info
```
POST: to create data.
GET: to read data.
PUT: to update data.
DELETE: to delete data.
```

## setup
```
python -m venv venv
venv\Scripts\activate
python -m pip install --upgrade pip
pip install -r requirements.txt
```
# for admin purposes saving & upgrading

```
venv\Scripts\activate
pip freeze > requirements.txt
powershell "(Get-Content requirements.txt) | ForEach-Object { $_ -replace '==', '>=' } | Set-Content requirements.txt"
pip install -r requirements.txt --upgrade
pip freeze > requirements.txt
powershell "(Get-Content requirements.txt) | ForEach-Object { $_ -replace '>=', '==' } | Set-Content requirements.txt"
```
