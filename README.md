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

- <int:pk> - views an item by index e.g. [gracious-butterfly-85177.pktriot.net/1/](https://gracious-butterfly-85177.pktriot.net/1/) for item one
- <int:pk>/update - Edits an item e.g.[gracious-butterfly-85177.pktriot.net/1/update](https://gracious-butterfly-85177.pktriot.net/1/update) to update item one

```json
  {
  "name": "Item <the number>",
  }
```

- <int:pk>/delete - Deletes an item e.g.[gracious-butterfly-85177.pktriot.net/1/update](https://gracious-butterfly-85177.pktriot.net/1/delete) to delete an item.
