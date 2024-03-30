
from flask import Flask, request, render_template, Response
from helpers import generate_normal_frames

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/detection")
def detection():
    camera_source = request.args.get('source', default='0')
    return render_template('detection.html', camera_source=camera_source)


@app.route('/video_feed_normal')
def video_feed_normal():
    camera_source = request.args.get('source', default='0')
    camera_source = int(
        camera_source) if camera_source.isdigit() else camera_source
    return Response(generate_normal_frames(camera_source), mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':
    app.run(debug=True, threaded=True)
