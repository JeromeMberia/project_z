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

