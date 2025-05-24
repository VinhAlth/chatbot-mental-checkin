from .prompt import prompt_next, prompt_continue, prompt_assess, dass21, state, conv_class
import re
from datetime import datetime
from pathlib import Path
import csv

RESULT_PATH = Path("/workspace/vinhnq/nckh_2024_mentalhealth_chatbot/result/run")
# question = dass21[1] + "\nĐánh giá trên thang điểm từ 0 đến 3, trong đó 0 là \"không hề\" và 3 là \"rất nhiều.\""
question = dass21[1] + "\n\nBạn có thể chia sẻ cảm nhận của mình về câu hỏi này không?\n\nHoặc bạn có thể viết luôn con số thể hiện điểm cho câu hỏi trên: \n0. Hầu như không\n1. Một vài ngày\n2. Hơn một nửa số thời gian\n3. Gần như mỗi ngày"

class Execcute:
    def __init__(
        self, 
        model,
        conv = [{"role": "Tư vấn viên", "content": question}],
        start = 0,
        score = [],
        state = True,
        check_info = False,
        student_id = "",
        full_name = "",
        birth_year = "", 
        class_name = "",
        ):
        """Hàm này để chạy chatbot thôi
        """
        
        self.vistral = model
        self.conv = conv
        self.start = start
        self.score = score
        self.state = state
        self.check_info = check_info
        self.student_id = student_id
        self.full_name = full_name
        self.birth_year = birth_year
        self.class_name = class_name
        # print("check", self.conv)
        
    def get_info(self, student_id, full_name, birth_year, class_name):
        self.student_id = student_id
        self.full_name = full_name
        self.birth_year = birth_year
        self.class_name = class_name
        self.check_info = True
    
    def get_session(self):
        # print("check1", self.conv)
        return self.conv, {
            "start" : self.start,
            "score" : self.score,
            "state" : self.state,
            "check_info" : self.check_info,
            "student_id" : self.student_id,
            "full_name" : self.full_name,
            "birth_year" : self.birth_year, 
            "class_name" : self.class_name,
        }
        
        
    def _add(self, conv: list):
        """Hàm này để tạo mẫu cuộc hội thoại khi truyền vào danh sách

        Args:
            conv (list): phần tử đầu là của user, phần tử hai là của assistant, và lặp lại tương tự
        >>> _add([
            "Xin chào bạn, tôi là sinh viên nè",
            "Chào bạn, tôi là chatbot"
        ])
        [{
            "role": "user", 
            "content": "Xin chào bạn, tôi là sinh viên nè"
        },
        {
            "role": "assistant", 
            "content": "Chào bạn, tôi là chatbot"
        }
        ]
        """
        temp = [] # Lưu cuộc hội thoại
        # Dùng vòng lặp để tạo mẫu
        for paragraph in range(0, len(conv), 2):
            user = {
                "role": "user", 
                "content": conv[paragraph]
            }
            assistant = {
                "role": "assistant", 
                "content": conv[paragraph+1]
            }
            temp.append(user)
            temp.append(assistant)
        return temp
    
    def __seeTerminal(self, name: str, value):
        # Quan sát chatbot chạy
        print(f"------------------{name}-----------------------------")
        print(value)
        print(f"------------------{name}-----------------------------\n")

    def _get_ques(self):
        if len(self.score) >= 9:
            return "Cảm ơn bạn đã trải qua 1 quá trình vui vẻ với tôi. Trước khi kết thúc cuộc hội thoại, bạn hãy điển thông tin và ấn xác nhận đi nào. Khi xác nhận xong hãy nhắn lại báo tôi nha. Cảm ơn bạn đã dành thời gian bên tôi."
        # Lưu vị trí cuối cùng khi lấy câu hỏi mới
        self.start = len(self.conv)
        # Lấy câu hỏi
        question = dass21[len(self.score)+1] + "\n\nBạn có thể chia sẻ cảm nhận của mình về câu hỏi này không?\n\nHoặc bạn có thể viết luôn con số thể hiện điểm cho câu hỏi trên: \n0. Hầu như không\n1. Một vài ngày\n2. Hơn một nửa số thời gian\n3. Gần như mỗi ngày"

        return question
        
    def _assess(self, conv: str, add = False):
        # Hàm đánh giá tính chất cuộc hội thoại
        question = dass21[len(self.score)]
        prompt = "\n".join(prompt_assess).format(question = question)
        ans = self.vistral.call(conv, prompt, specific = True, add = add)
        
        return ans
    
    def _next(self, conv, types):

        case = state[types]
        question = dass21[len(self.score)]
        if types==4:
            case = case.format(score = self._classify_level(sum(self.score)))
        prompt = "\n".join(prompt_next).format(question = question, case = case)

        ans = self.vistral.call(conv, prompt)
        if types!=4:
            self.score.append(int(types))
            
        return ans
    
    # def _continue(self, conv):

    #     question = dass21[len(self.score)]
    #     prompt = "\n".join(prompt_continue).format(question = question)
    #     add =  f"Đây là cuộc hội thoại mới sinh viên, câu trả lời của sinh viên chưa đủ để đánh giá, bạn hãy hỏi lại câu này {question}\n"
    #     ans = self.vistral.call(add + conv + "\nTư vấn viên: ", prompt)
    #     return ans
    
    def _continue(self, conv):

        ans = "Xin lỗi bạn, tôi chưa đủ khả để đánh giá điểm số của bạn, bạn có thể viết lại không. Hoặc chỉ cần viết 1 số thể hiện số điểm của bạn."
        question = dass21[len(self.score)+1]
        return ans + "\n" + question
    
    def _transform(self, all = False):
        # Biến đổi hội thoại để chuyền vào chatbot
        reconv = ""
        start = self.start if not all else 0
        for paragraph in self.conv[start:]: 
            reconv += paragraph["role"] + ": " + paragraph["content"] + "\n"
        return str(reconv)
    
    def _getNumber(self, sentence):
        # Tìm và lấy danh sách tất cả các con số trong văn bản
        numbers = re.findall(r'\d+', sentence)
        # Lấy con số cuối cùng trong danh sách
        last_number = int(numbers[-1])
        return last_number
    
    def _save(self):
        current_datetime = datetime.now()
        # Dữ liệu bạn muốn lưu
        state = self._classify_level(sum(self.score))
        data = [
            self.student_id,
            self.full_name,
            self.birth_year,
            self.class_name,
            self.score,
            state,
            self.conv,
            current_datetime.strftime('%Y-%m-%d_%H-%M-%S')
        ]

        # Đường dẫn tới file bạn muốn lưu
        file_path = Path("/workspace/vinhnq/nckh_2024_mentalhealth_chatbot/result/run/data.csv")

        # Kiểm tra xem file đã tồn tại chưa
        file_exists = file_path.exists()

        # Lưu dữ liệu vào file CSV
        with open(file_path, 'a', newline='') as file:
            writer = csv.writer(file)
            if not file_exists:  # Ghi header nếu file chưa tồn tại
                writer.writerow(['student_id', 'full_name', 'birth_year', 'class_name', 'score', 'state', 'conv', 'timestamp'])
            writer.writerow(data)

        print("File CSV đã được lưu thành công")

    def _classify_level(self, x):
        # Bảng đánh giá theo thang điểm

        if x <= 4: return "tốt"
        elif 5 <= x <= 9: return "nhẹ"
        elif 10 <= x <= 14: return "vừa phải"
        elif 15 <= x <= 19: return "nặng"
        else: return "nghiêm trọng"
            
    def _end(self):
        if self.state:
            if self.check_info:
                # Biến đổi sang dạng chuyền vào chatbot
                conversation = self._transform(all=True); self.__seeTerminal("conversation", conversation) 
                ans = self._next("---\n" + conversation + "\n---\nBạn phản hồi lại cho hội thoại trên đi.", 4) # Phản hồi đầu
                # print(ans)
                self.conv.append({"role": "Tư vấn viên", "content": ans}) # Thêm cuộc hội thoại
                self._save()
                self.conv = "End"
                self.state = False
                return ans
            else:
                return "Cảm ơn bạn đã trải qua 1 quá trình vui vẻ với tôi. Trước khi kết thúc cuộc hội thoại, bạn hãy điển thông tin và ấn xác nhận đi nào. Khi xác nhận xong hãy nhắn lại báo tôi nha. Cảm ơn bạn đã dành thời gian bên tôi."
        else:
            end1 = "Cuộc hội thoại đã kết thúc. Cảm ơn bạn đã kiên nhẫn cùng tôi đi đến câu hỏi cuối cùng. Đây là kết quả của bạn: \n"
            end2 = f"Điểm: {sum(self.score)}\nKết quả: {self._classify_level(sum(self.score))}"
            self.state = False

        return end1 + end2

    def execcute(self, conversation):

        cls = self._assess(conversation, self._add(conv_class)); self.__seeTerminal("classification", cls)
        
        if "w" in cls.lower(): # Nếu chưa đánh giá được
            return "w"

        else:
            types = self._getNumber(cls); self.__seeTerminal("Điểm", types) # Này là điểm
            
            return types