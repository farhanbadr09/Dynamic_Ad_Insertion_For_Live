from flask import Flask, jsonify, render_template
import time
from load import automate_update


app = Flask(__name__)

stream_response = [
    {
        'id': 1,
        'status': u'streaming started'
    },
]

@app.route('/dash/start_stream/', methods=['GET'])
def get_tasks():
    # return jsonify({"stream": stream_response})
    while True:
        url = "https://demo.daiconnect.com/live/dash/usp/dash_blue/.mpd?requestuid=bbd47347-840b-44e3-bb47-2d3bd57b7d6b"
        automate_update(url)
        time.sleep(3)
	


	
if __name__ == '__main__':
    app.run(debug=True)
