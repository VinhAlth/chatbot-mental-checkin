import json
from datetime import datetime
import sys
sys.path.append('/workspace/vinhnq/nckh_2024_mentalhealth_chatbot/result/run') 
# Dữ liệu bạn muốn lưu
def save(conv):
    data_to_save = {conv}

    # Tạo tên file dựa trên ngày giờ
    current_datetime = datetime.now()
    file_name = f"data_{current_datetime.strftime('%Y-%m-%d_%H-%M-%S')}.json"

    # Đường dẫn tới file bạn muốn lưu
    file_path = f"{file_name}"

    # Lưu dữ liệu vào file JSON
    with open(file_path, 'w', encoding='utf-8') as json_file:
        json.dump(data_to_save, json_file, ensure_ascii=False)

    print(f"File JSON đã được lưu thành công với tên: {file_name}")