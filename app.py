from flask import Flask, render_template
import socketio

app = Flask(__name__)

# Configure the secret key for session management
app.config['SECRET_KEY'] = '3153'

# Initialize Socket.IO
sio = socketio.Client()

@app.route('/')
def trade_entry():
    return render_template('trade_entry.html')

@app.route('/banner')
def trade_banner():
    return render_template('trade_banner.html')

if __name__ == '__main__':
    app.run(debug=True)
