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
for more direction [link](https://github.com/JeromeMberia/project_z/blob/main/Directions.pdf)
- <int:pk> - to view an item by index e.g. [gracious-butterfly-85177.pktriot.net/1/](https://gracious-butterfly-85177.pktriot.net/1/)
- <int:pk>/update - Edits an item e.g. [gracious-butterfly-85177.pktriot.net/1/update](https://gracious-butterfly-85177.pktriot.net/1/update)

```json
  {
  "name": "Item <the number>",
  }
```

- <int:pk>/delete - Deletes an item e.g. [gracious-butterfly-85177.pktriot.net/1/update](https://gracious-butterfly-85177.pktriot.net/1/delete)
