from flask import Flask, render_template
app = Flask(__name__)

@app.route('/play')
def welcome_page():
    return render_template("play.html")

@app.route('/play/<int:times>')
def play_times(times):
    return render_template("play_times.html", times=times)

@app.route('/play/<int:times>/<color>')
def play_times_color(times, color):
    return render_template("play_times_color.html", times=times, color=color)

if __name__ == "__main__":
    app.run(debug=True)