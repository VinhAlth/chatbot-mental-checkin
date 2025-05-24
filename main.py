from flask import Flask, render_template, request, session, jsonify
import threading
import time
from src import Execcute
from src.utils import VistralChatbot
from flask_session import Session
import json
import torch

app = Flask(__name__)

# Thiết lập cấu hình cho session
app.config['SECRET_KEY'] = 'abc123'
app.config['SESSION_TYPE'] = 'filesystem'
app.config['SESSION_PERMANENT'] = False
app.static_folder = 'static'
session = dict()
session['start']  = dict({'time': time.time()})
model = VistralChatbot() 
def replace_newline_with_br(input_string):
    return input_string.replace('\n', '<br>')

@app.route("/")  # Đường dẫn mới
def home():
    global model
    session['start']  = dict({'time': time.time()})
    if 'model' not in globals():
        model = VistralChatbot()   
    return render_template("index.html")


@app.route("/get")  # Đường dẫn mới
def get_bot_response():
    global model
    userText = request.args.get('msg')
    session_id = request.args.get('user_id')  # Lấy session_id từ request
    if session_id not in session:
        session[session_id] = dict({'conv': [{'role': 'Tư vấn viên', 'content': '1. Bạn có cảm thấy không có niềm vui thích nào trong học tập hay làm việc không?.\nBạn có thể chia sẻ cảm nhận của mình về câu hỏi này không?\n\nHoặc bạn có thể viết luôn con số thể hiện điểm cho câu hỏi trên: \n0. Hầu như không\n1. Một vài ngày\n2. Hơn một nửa số thời gian\n3. Gần như mỗi ngày'}]})
    session[session_id]['time'] = time.time()
    if 'model' not in globals():
        model = VistralChatbot()
    data = request.args.get('info')
    data = json.loads(data)
    
    # Lấy thông tin người dùng từ localStorage nếu có
        
    call = Execcute(model, session[session_id]["conv"], **data)
    conv = call.execcute(userText)
    session[session_id]['conv'], user_info = call.get_session()
    transpose = replace_newline_with_br(conv)
    # print("data", data)
    print("Ra ngoài:", transpose)
    return jsonify({'conv': transpose, 'user_info': user_info})

def session_cleanup():
    global model
    while True:
        time.sleep(300)  # Kiểm tra mỗi giờ
        current_time = time.time()
        sessions_to_remove = []
        for session_id, session_info in session.items():
            print("Session_id còn lại: ", session_id)
            last_activity_time = session_info.get('time', 0)
            if current_time - last_activity_time > 3600:  # Kiểm tra nếu không hoạt động trong 1 tiếng
                sessions_to_remove.append(session_id)
        for session_id in sessions_to_remove:
            del session[session_id]
            print("Session removed:", session_id)
            print('model' in locals())
            print(len(session)==0)
        if 'model' in globals() and len(session)==0:
            print('Xóa model: ', len(session))
            del model
            torch.cuda.empty_cache()

cleanup_thread = threading.Thread(target=session_cleanup)
cleanup_thread.daemon = True
cleanup_thread.start()

@app.route('/save_info', methods=['POST'])  # Đường dẫn mới
def save_info():
    return '', 202

@app.route('/unload', methods=['POST'])
def handle_unload_event():
    print("Đã chạy vào unload")
    user_id = request.form.get('userID')
    print("User ID: ", user_id)  # In ra User ID để kiểm tra
    if user_id in session:
        del session[user_id]
        print("Xóa User ID:", user_id)
    return 'OK', 200


if __name__ == "__main__":
    app.run("127.0.0.1", port=8422)

