import re

text = "Score: 1. Bạn cảm thấy bản thân khó mà nghỉ ngơi một cách thoải mái đúng không?\n\nNhận xét: Sinh viên đã trả lời câu hỏi bằng cách nói rằng họ cảm thấy bình thường, điều này ngụ ý rằng họ không gặp khó khăn gì trong việc nghỉ ngơi một cách thoải mái. Tuy nhiên, câu trả lời của họ không trực tiếp giải quyết câu hỏi, vì nó chỉ đơn giản là cung cấp thông tin về trạng thái hiện tại của họ chứ không phải khả năng nghỉ ngơi thoải mái của họ.\n\nĐiểm đánh giá: 1 (Áp dụng cho sinh viên ở mức độ nào đó, hoặc trong một số trường hợp)"

# Tìm và lấy danh sách tất cả các con số trong văn bản
numbers = re.findall(r'\d+', text)

# Lấy con số cuối cùng trong danh sách
last_number = int(numbers[-1])

print("Con số cuối cùng trong văn bản là:", last_number)
 
from transformers import AutoModelForCausalLM, AutoTokenizer
print(help(AutoModelForCausalLM.from_pretrained))

