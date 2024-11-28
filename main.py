from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Получаем данные из формы
        name = request.form.get('name')
        email = request.form.get('email')
        subject = request.form.get('subject')
        message = request.form.get('message')

        # Выводим данные в консоль
        print(f"Message from: {name}")
        print(f"Email: {email}")
        print(f"Subject: {subject}")
        print(f"Message: {message}")
        print("-" * 50)  # Разделитель для читаемости

        # Можно здесь добавить дополнительную логику, например, отправку email, сохранение данных в БД и т.д.

        # Отправляем ответ на страницу с подтверждением
        return render_template("index.html", active_page='projects', success=True)

    # Если метод GET, просто отображаем форму
    return render_template("index.html", active_page='projects')

if __name__ == '__main__':
    app.run(debug=True)
