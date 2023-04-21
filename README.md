# homework_63_abylay_kuvatov

## Superuser:
login: admin@example.com
password: 123456qWe!

## Users:
1. johndoe
2. jackdoe
3. janedoe
4. susandoe

password: 123456qWe!

## API:

Для проверки API можно воспользоваться программой **Postman**
##### Примечание: 
_Для проверки метода PUT, необходимо сначала получить данные определенной публикации, скопировать данные в окно BODY -> raw (JSON), затем внести изменения в необходимые поля и нажать на кнопку **Send**_

Также следует учесть, что права доступа разграничены согласно ТЗ, поэтому необходимо добавить в HEADERS следующие параметры: 
Key: Authorization
Value: Token _token_, где вместо _token_ необходимо вставить токен пользователя

#### tokens:
1. admin: 2e89c8e18b5fc6006e3088715d1e70c482ebebce
2. johndoe: 087bc1e894be5d208ee3eac6449587a011356a28
3. jackdoe: f05ad37580ce9d96f24df719778e14a773075237
4. janedoe: 3598052738f7da44066c360d0aff8d196076830e
5. susandoe: 9a4d05ee0d50dc96f78c9070818a935bf4c5c6bf

В случае, если указанные токены не сработают, нужно заново сгенерировать токены следующим образом:
В **Postman**, в окно BODY -> raw (JSON) добавить логин/пароль для пользователя в формате JSON:
{
    "username": _username_,
    "password": _password_
}
URL: POST http://localhost:8000/api/login/

Ниже указаны методы и пути к API:

### Publications
#### detail
GET _hostname_/api/publications/id
#### update
PUT _hostname_/api/publications/id
#### delete
DELETE _hostname_/api/publications/id

### Likes
#### detail
GET _hostname_/api/likes/id
#### update
PUT _hostname_/api/likes/id
#### delete
DELETE _hostname_/api/likes/id

### Сomments
#### detail
GET _hostname_/api/comments/id
#### update
PUT _hostname_/api/comments/id
#### delete
DELETE _hostname_/api/comments/id
