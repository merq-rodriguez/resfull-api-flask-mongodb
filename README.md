## API RESTFULL FLASK PYTHON + MONGODB + AUTH JWT + NGINX  + DOCKER

<img 
  align="right"  
  width="100"
  src="https://cdn.worldvectorlogo.com/logos/flask.svg" 
/>

<img 
  width="400"
  src="https://cdn.worldvectorlogo.com/logos/mongodb.svg" 
/>

---

Personally I did not like how flask-restful implements the controllers, it restricts the design of a restfull api a lot,
but as an example, do this exercise.

### Run Mongodb with Docker
```shell
docker run --name mongo -p 27017:27017  -d mongo:latest
```



### Clean Pycache
```bash
pyclean .
```

### Install

```bash
pip install -r requirements.txt
``` 

## Run App
```bash
python3 src/app.py
``` 

> Use **GET**

```
http://127.0.0.1:5000/users
```
### Response
```json
[
  {
    "_id": "5ff92631ede9e18c9682f343",
    "email": "jud@gmail.com",
    "name": "Stiven Stark Snow",
    "password": "1234"
  },
  {
    "_id": "5ff926fb5e3d73c972c86e8e",
    "email": "jud@gmail.com",
    "name": "Malcom Merly",
    "password": "1234"
  }
]
```
> Use **GET**

```
http://127.0.0.1:5000/users/5ff926fb5e3d73c972c86e8e
```
### Response
```json
{
  "_id": "5ff926fb5e3d73c972c86e8e",
  "email": "jud@gmail.com",
  "name": "Malcom Merly",
  "password": "1234"
}
```

> Use **POST**

```
  http://127.0.0.1:5000/users
```
### Body
```json
{
  "email": "jud@gmail.com",
  "name": "Malcom Merly",
  "password": "1234"
}
```

### Response

```json
{
  "email": "jud@gmail.com",
  "id": "5ffa034b79977dc1ecf58b29",
  "name": "Malcom Merly",
  "password": "1234"
}
```

> Use **PUT**

```
  http://127.0.0.1:5000/users/5ff926fb5e3d73c972c86e8e
```

### Body

```json
{
  "email": "jud@gmail.com",
  "id": "5ffa034b79977dc1ecf58b29",
  "name": "Malcom Merly updated",
  "password": "1234"
}
```

### Response

```json
{
  "message": "User updated"
}
```

> Use **PUT**

```
  http://127.0.0.1:5000/users/5ff926fb5e3d73c972c86e8e
```

### Response

```json
{
  "message": "User deleted"
}
```
