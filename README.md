# Item CRUD API

[Link](https://gracious-butterfly-85177.pktriot.net/) to live site.

## Endpoint

- / - views all the items e.g [gracious-butterfly-85177.pktriot.net](https://gracious-butterfly-85177.pktriot.net/)

- add/ - creates an item e.g [gracious-butterfly-85177.pktriot.net](https://gracious-butterfly-85177.pktriot.net/add/)
  
To add an item:

```json
  {
  "name": "Item <the number>",
  }
```
For more directions [link](https://github.com/JeromeMberia/project_z/blob/main/Directions.pdf)
- <int:pk> - to view an item by index e.g. [gracious-butterfly-85177.pktriot.net/1/](https://gracious-butterfly-85177.pktriot.net/1/)
- <int:pk>/update - Edits an item e.g. [gracious-butterfly-85177.pktriot.net/1/update](https://gracious-butterfly-85177.pktriot.net/1/update)

```json
  {
  "name": "Item <the number>",
  }
```

- <int:pk>/delete - Deletes an item e.g. [gracious-butterfly-85177.pktriot.net/1/update](https://gracious-butterfly-85177.pktriot.net/1/delete)

## To Run it 

Enter your terminal and type:

```powershell
git clone https://github.com/JeromeMberia/project_z.git
```

```powershell
cd project_z
```

```powershell
py -m venv venv
```

```powershell
.\venv\Scripts\activate
```

```powershell
pip install -r requirements.txt
```

```powershell
cd .\myproject\
```

```powershell
py manage.py makemigrations
```

```powershell
py manage.py py migrate
```

```powershell
py manage.py runserver
```
## On security 
I would usually add `.env` file on the root directory of the project and place the DEBUG and SECRET_KEY in it.

###If you would like to implement do this:

In your terminal `cd` to the project
```powershell
pip install python-decouple
```

To save the library in `requirements.txt` file
```powershell
python -m pip freeze > requirements.txt
```

Enter the `setting.py` file found in `.\myproject\myproject\setting.py`
At the top of the file near `from pathlib import Path` this line of code, under it add this:

```py
from decouple import config
```
Then you change `SECRET_KEY` and `DEBUG` to this:

```py
SECRET_KEY = config('SECRET_KEY')
DEBUG = config('DEBUG')
```

```
SECRET_KEY=<SECRET_KEY>
DEBUG=<True or False>
```

## Notice
This repository will be private on the 28th of July 2023. 

