from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

# Главная страница
@app.route("/")
def home():
    return render_template("index.html")

# О приложении
@app.route("/about")
def about():
    return render_template("about.html")

# Установка
@app.route("/download")
def download():
    return render_template("download.html")

# Разработчик
@app.route("/developer")
def developer():
    return render_template("developer.html")

# Скачать release 1.0
@app.route("/download_app_1.0")
def download_app_1_0():
    return send_from_directory("static/files", "ProCrypt.1.0.7z", as_attachment=True)

# Скачать release 2.0
@app.route("/download_app_2.0")
def download_app_2_0():
    return send_from_directory("static/files", "ProCrypt.2.0.7z", as_attachment=True)

# Скачать release 2.1
@app.route("/download_app_2.1")
def download_app_2_1():
    return send_from_directory("static/files", "ProCrypt_v2.1.7z", as_attachment=True)

# Скачать release 2.2
@app.route("/download_app_2.2")
def download_app_2_2():
    return send_from_directory("static/files", "ProCrypt_v2.2.7z", as_attachment=True)

# Скачать документацию
@app.route("/download_doc")
def download_doc():
    return send_from_directory("static/files", "ProCrypt-main.zip", as_attachment=True)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)