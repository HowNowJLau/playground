from flask import Flask, render_template
app = Flask(__name__)

@app.route('/play')
def play(times=3, color="cadetblue"):
    return render_template("play_times_color.html", times=times, color=color)

@app.route('/play/<int:times>')
def play_times(times=3, color="cadetblue"):
    return render_template("play_times_color.html", times=times, color=color)

@app.route('/play/<int:times>/<color>')
def play_times_color(times=3, color="cadetblue"):
    return render_template("play_times_color.html", times=times, color=color)

if __name__ == "__main__":
    app.run(debug=True)