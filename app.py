from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # Mengambil foto 1.jpg sampai 9.jpg secara otomatis
    photos = [f'{i}.jpg' for i in range(1, 10)] 
    return render_template('index.html', photos=photos)

if __name__ == '__main__':
    app.run(debug=True)