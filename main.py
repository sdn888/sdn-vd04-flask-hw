from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    current_time = datetime.now()
    # Передача текущей даты и времени в шаблон
    return render_template('index.html', current_time=current_time)

if __name__ == '__main__':
    app.run(debug=True)