import gradio as gr
import datetime

# Dữ liệu người dùng giả lập
default_user_data = {
    'start': 0,
    'score': [],
    'state': True,
    'check_info': False,
    'student_id': "",
    'full_name': "",
    'birth_year': "",
    'class_name': ""
}
user_data = default_user_data.copy()

# Hàm xử lý phản hồi của bot
def bot_response(msg, user_data):
    response = f"Bot đã nhận: {msg}"
    user_data['state'] = not user_data['state']
    return response, user_data

# Giao diện chat
def chat_interface(user_message, chat_history, user_data):
    bot_message, user_data = bot_response(user_message, user_data)
    chat_history.append(("You", user_message))
    chat_history.append(("Bot", bot_message))
    return chat_history, user_data

# Xử lý thông tin người dùng
def save_user_info(student_id, full_name, birth_year, class_name):
    global user_data
    user_data.update({
        'student_id': student_id,
        'full_name': full_name,
        'birth_year': birth_year,
        'class_name': class_name,
        'check_info': True
    })
    return "Thông tin đã được lưu thành công!"

# Khởi tạo giao diện Gradio
with gr.Blocks() as demo:
    gr.Markdown("# Mental Health Chatbot")
    
    with gr.Row():
        with gr.Column():
            chatbot = gr.Chatbot()
            msg = gr.Textbox(placeholder="Hãy nhập câu trả lời của bạn...")
            send_button = gr.Button("Gửi")
            state = gr.State(default_user_data)
        
        with gr.Column():
            gr.Markdown("## Thông tin cá nhân")
            student_id = gr.Textbox(label="Mã số sinh viên")
            full_name = gr.Textbox(label="Họ và tên")
            birth_year = gr.Textbox(label="Năm sinh")
            class_name = gr.Textbox(label="Lớp")
            save_button = gr.Button("Xác nhận thông tin")
            save_output = gr.Textbox(label="Thông báo", interactive=False)
    
    send_button.click(chat_interface, [msg, chatbot, state], [chatbot, state])
    save_button.click(save_user_info, [student_id, full_name, birth_year, class_name], save_output)

demo.launch()
