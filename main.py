from flask import Flask, request, jsonify

app = Flask(__name__)

user = []
music = []


@app.route('/')
def web():
    web = "http://127.0.0.1:3005/user - Получить все данные пользователей <br/> \n" \
          "http://127.0.0.1:3005/user/id - Изменить данные пользователей <br/> \n" \
          "http://127.0.0.1:3005/music - Получить все данные о музыке <br/> \n" \
          "http://127.0.0.1:3005/music/id - Изменить данные о музыке <br/> \n"
    return web


@app.route('/user', methods=['POST', 'GET'])
def Users():
    if request.method == 'POST':
        data = request.get_json()

        name = data['name']
        password = data['password']
        group = data['group']
        email = data['email']
        address = data['address']
        telephone = data['telephone']
        user.append(name + " " + password + " " + group + " " + email + " " + address + " " + telephone)
        return "Данные были успешно записаны, 200"
    if request.method == 'GET':
        return user


@app.route('/user/<id>', methods=['PUT', 'DELETE'])
def UsersChange(id):
    if request.method == 'DELETE':
        try:
            user.pop(int(id))
            return "Успех, 200"
        except:
            return "Ошибка, 500"
    if request.method == 'PUT':
        try:

            data = request.get_json()
            name = data['name']
            password = data['password']
            group = data['group']
            email = data['email']
            address = data['address']
            telephone = data['telephone']
            change = name + " " + password + " " + group + " " + email + " " + address + " " + telephone

            user[int(id)] = change
            return "Успех, 200"
        except:
            return "Ошибка, 500"


@app.route('/music', methods=['POST', 'GET'])
def Musics():
    if request.method == 'POST':
        data = request.get_json()

        title = data['title']
        artist = data['artist']
        publication_date = data['publication_date']
        genre = data['genre']
        adult_sign = data['adult_sign']
        music.append(title + " " + artist + " " + publication_date + " " + genre + " " + adult_sign)
        return "Данные были успешно записаны, 200"
    if request.method == 'GET':
        return music


@app.route('/music/<id>', methods=['PUT', 'DELETE'])
def MusicsChange(id):
    if request.method == 'DELETE':
        try:
            music.pop(int(id))
            return "Успех, 200"
        except:
            return "Ошибка, 500"
    if request.method == 'PUT':
        try:

            data = request.get_json()

            title = data['title']
            artist = data['artist']
            publication_date = data['publication_date']
            genre = data['genre']
            adult_sign = data['adult_sign']
            change = title + " " + artist + " " + publication_date + " " + genre + " " + adult_sign

            music[int(id)] = change
            return "Успех, 200"
        except:
            return "Ошибка, 500"


if __name__ == '__main__':
    app.run(port=3005)
