**Отчёт API Flask**

1. GET <http://127.0.0.1:3005/>

Полученная информация:

http://127.0.0.1:3005/user - Получить все данные пользователей <br/>

http://127.0.0.1:3005/user/id - Изменить данные пользователей <br/>

http://127.0.0.1:3005/music - Получить все данные о музыке <br/>

http://127.0.0.1:3005/music/id - Изменить данные о музыке <br/>

![](Aspose.Words.e73a1f10-e927-4b47-b11a-a063528e2795.001.png)

1. ` `POST <http://127.0.0.1:3005/user>

Body: JSON 

{

`    `"name" : "Владимир",

`    `"password" : "123сложный пассворд",

`    `"group" : "23пв",

`    `"email" : "marusa\_nay@twich.com",

`    `"address" : "Щетинина 23",

`    `"telephone" : "88005553535"

}

Полученная информация: Данные были успешно записаны, 200

![](Aspose.Words.e73a1f10-e927-4b47-b11a-a063528e2795.002.png)

1. Второй POST http://127.0.0.1:3005/user

Body: JSON 

{

`    `"name" : "Ясуо",

`    `"password" : "0/43/0ff15",

`    `"group" : "2инв",

`    `"email" : "tima\_racow\_ff15@feeder.lol",

`    `"address" : "RedSpawn 15",

`    `"telephone" : "84951505445"

}

Полученная информация: Данные были успешно записаны, 200

![](Aspose.Words.e73a1f10-e927-4b47-b11a-a063528e2795.003.png)

1. GET <http://127.0.0.1:3005/user>

Полученная информация:

[

`    `"Владимир 123сложный пассворд 23пв marusa\_nay@twich.com Щетинина 23 88005553535",

`    `"Ясуо 0/43/0ff15 2инв tima\_racow\_ff15@feeder.lol RedSpawn 15 84951505445"

]

![](Aspose.Words.e73a1f10-e927-4b47-b11a-a063528e2795.004.png)

1. DELETE http://127.0.0.1:3005/user/0

Полученная информация: Успех, 200

![](Aspose.Words.e73a1f10-e927-4b47-b11a-a063528e2795.005.png)

1. PUT http://127.0.0.1:3005/user/0

Body: JSON 

{

`    `"name" : "Ебрагим",

`    `"password" : "sder75893jfjjvvfgdh",

`    `"group" : "2020rsp",

`    `"email" : "simpleemail@gmail.com",

`    `"address" : "simpleadress",

`    `"telephone" : "880005552323"

}

Полученная информация: Успех, 200

![](Aspose.Words.e73a1f10-e927-4b47-b11a-a063528e2795.006.png)

1. GET <http://127.0.0.1:3005/user>

Полученная информация:

[

`    `"Ебрагим sder75893jfjjvvfgdh 2020rsp simpleemail@gmail.com simpleadress 880005552323"

]

![](Aspose.Words.e73a1f10-e927-4b47-b11a-a063528e2795.007.png)

1. PUT http://127.0.0.1:3005/user/3

`	`Body: JSON

{

`    `"name" : "Максим",

`    `"password" : "vnbjfhguryt8576",

`    `"group" : "230opi",

`    `"email" : "realmail@mail.con",

`    `"address" : "Street 45",

`    `"telephone" : "+7981998856"

}

Полученная информация: Ошибка, 500


![](Aspose.Words.e73a1f10-e927-4b47-b11a-a063528e2795.008.png)

1. POST http://127.0.0.1:3005/music

Body: JSON 

{

`    `"title" : "No Name",

`    `"artist" : "No artist",

`    `"publication\_date" : "01/01/2022",

`    `"genre" : "edm",

`    `"adult\_sign" : "yes"

}

Полученная информация: Данные были успешно записаны, 200

![](Aspose.Words.e73a1f10-e927-4b47-b11a-a063528e2795.009.png)

1. Второй POST <http://127.0.0.1:3005/music>

Body: JSON

{

`    `"title" : "Sadness",

`    `"artist" : "Den Pixel",

`    `"publication\_date" : "10/05/2021",

`    `"genre" : "electronic",

`    `"adult\_sign" : "no"

}

Полученная информация: Данные были успешно записаны, 200

![](Aspose.Words.e73a1f10-e927-4b47-b11a-a063528e2795.010.png)

1. GET http://127.0.0.1:3005/music

Полученная информация:

[

`    `"No Name No artist 01/01/2022 edm yes",

`    `"Sadness Den Pixel 10/05/2021 electronic no"

]

![](Aspose.Words.e73a1f10-e927-4b47-b11a-a063528e2795.011.png)\

1. DELETE <http://127.0.0.1:3005/music/0>

Полученная информация: Успех, 200

![](Aspose.Words.e73a1f10-e927-4b47-b11a-a063528e2795.012.png)


1. PUT <http://127.0.0.1:3005/music/0>

Body: JSON

{

`    `"title" : "The Glass Inside Your Skull",

`    `"artist" : "Mr.Kitty",

`    `"publication\_date" : "05/01/2021",

`    `"genre" : "electronic",

`    `"adult\_sign" : "no"

}

Полученная информация: Успех, 200

![](Aspose.Words.e73a1f10-e927-4b47-b11a-a063528e2795.013.png)

1. GET <http://127.0.0.1:3005/music>

Полученная информация: 

[

`    `"The Glass Inside Your Skull Mr.Kitty 05/01/2021 electronic no"

]

![](Aspose.Words.e73a1f10-e927-4b47-b11a-a063528e2795.014.png)

1. DELETE <http://127.0.0.1:3005/music/3> (попытка удалить не существующую запись)

Полученная информация: Ошибка, 500

![](Aspose.Words.e73a1f10-e927-4b47-b11a-a063528e2795.015.png)

1. PUT <http://127.0.0.1:3005/music/3>

Body: JSON

{

`    `"title" : "The Glass Inside Your Skull",

`    `"artist" : "Mr.Kitty",

`    `"publication\_date" : "05/01/2021",

`    `"genre" : "electronic",

`    `"adult\_sign" : "no"

}

Полученная информация: Ошибка, 500

![](Aspose.Words.e73a1f10-e927-4b47-b11a-a063528e2795.016.png)




