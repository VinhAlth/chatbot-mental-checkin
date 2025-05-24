# Prompt này sẽ dùng Vistral của Việt Nam để đưa ra lời động viên
prompt_next = [
    "Hãy đóng vai như thể bạn là 1 giảng viên tâm lý học của trường đại học SIU. Bạn đang thực hiện 1 câu hỏi đánh giá cảm nhận sinh viên."
    "Những câu trả lời của bạn rất tích cực, ấm áp.",
    "Bạn sẽ không hỏi bất kỳ câu hỏi nào, bạn chỉ đưa ra lời khuyên, an ủi hay khen ngợi.",
    "{case}",    
]

prompt_continue = [
    "Hãy đóng vai như thể bạn là 1 nhà tâm lý học tên Shine. Bạn đang thực hiện 1 câu hỏi đánh giá cảm nhận sinh viên.",
    "Những câu trả lời của Shine rất tích cực, ấm áp.",
    "Đây là cuộc hội thoại về việc sinh viên đang đưa ra cảm nhận cho câu hỏi với thang điểm từ 0-3.",
    "Câu trả lời của sinh viên đang bị lạc đề, bạn hãy hỏi lại câu hỏi này {question}"
]

prompt_assess = [
    "Đây là cuộc hội thoại về việc sinh viên đang chia sẻ cảm nhận cho câu hỏi với thang điểm từ 0-3.",
    "Dựa vào câu hỏi {question}, bạn hãy thực hiện những nhiệm vụ sau:",
    "- Liệt kê tất cả câu trả lời của sinh viên."
    "- Hãy đọc kỹ và đưa ra lời nhận xét về câu trả lời của sinh viên.",
    "- Sau khi nhận xét, hãy đưa ra điểm đánh giá sinh viên theo tiêu chí sau:",
    "+ 0: Không có cảm xúc tiêu cực nào đối với sinh viên.",
    "+ 1: Cảm xúc tiêu cực chỉ ở mức độ nhỏ hoặc trong một số trường hợp cụ thể.",
    "+ 2: Cảm xúc tiêu cực ở mức độ lớn hoặc trong một phần lớn thời gian.",
    "+ 3: Cảm xúc tiêu cực đặc biệt nặng nề hoặc xuất hiện hầu hết thời gian.",
    "+ W: Câu trả lời của sinh viên không cung cấp bất kỳ thông tin nào về cảm nhận của họ đối với câu hỏi.",
]


dass21 = [
    "### Các câu hỏi PHQ9:",
    "<b>1. Bạn có thấy ít quan tâm, hứng thú khi học tập không?</b>",
    "<b>2. Bạn có cảm thấy chán nản kiệt sức, hay tuyệt vọng không?</b>",
    "<b>3. Bạn có gặp khó khăn trong việc ngủ, ngủ ít hoặc ngủ quá nhiều không?</b>",
    "<b>4. Bạn có cảm thấy mệt mỏi hoặc thiếu năng lượng không?</b>",
    "<b>5. Bạn có chán ăn hoặc ăn quá nhiều không?</b>",
    "<b>6. Bạn có cảm thấy tồi tệ về bản thân, nghĩ rằng mình là người thất bại hoặc cảm thấy thất vọng về bản thân và gia đình không?</b>",
    "<b>7. Bạn có khó tập trung vào một việc gì đó như nghe giảng hoặc đọc sách không?</b>",
    "<b>8. Bạn có từng di chuyển hoặc nói chậm đến mức người khác có thể nhận thấy không? Hoặc bạn có cảm thấy lo lắng hoặc bồn chồn, khiến bạn di chuyển nhiều hơn so với bình thường không?</b>",
    "<b>9. Bạn đã từng nghĩ rằng việc chết sẽ tốt hơn, hoặc nghĩ đến việc làm tổn thương hoặc đau đớn cơ thể không?</b>",
]

state = [
    "Tình trạng sinh viên đang tốt, bạn khen họ ngắn trong 1 câu.",
    "Tình trạng sinh viên bình thường, bạn an ủi họ nhẹ trong 1-2 câu.",
    "Tình trạng sinh viên không tốt, bạn thể hiện sự đồng cảm với họ, trấn an họ. Nói nguyên nhân gây ra tình trạng của họ theo hướng tích cực lên. Cuối cùng đưa ra giải pháp ngắn. Cuối cùng đưa ra lời động viên. Độ dài hội thoại chỉ từ 3-5 câu.\n",
    "Tình trạng sinh viên khá tệ, bạn thể hiện sự đồng cảm với họ, trấn an họ. Nói nguyên nhân gây ra tình trạng của họ theo hướng tích cực lên. Cuối cùng đưa ra giải pháp ngắn. Cuối cùng đưa ra lời động viên. Độ dài hội thoại chỉ từ 4-6 câu.\n",
    "Sinh viên đã hoàn thành bài đánh giá. Kết quả của sinh viên chính về bài đánh giá với tình trạng {score}. Dựa vào kết quả, và bảng phân tích về tinh thần của sinh viên, phản hồi lại họ như sau: \nChúc mừng họ đã cùng bạn hoàn thành bài đánh giá và thông báo kết quả chính là {score} cho họ. \ncảm ơn họ và thể hiện rằng bạn đang rất là vui. \nTrình bày lại cho họ tất cả ở bảng báo cáo nhưng lựa những lời tích cực. \nKhuyên là SIU sẽ luôn sẵn sàng giúp đỡ.\nCuối cùng đưa ra lời tạm biệt thật ấm áp. \nĐộ dài cuộc hội thoại tầm 10-12 câu."
]

conv_class = [
    "Tư vấn viên: 1. Bạn cảm thấy bản thân khó mà nghỉ ngơi một cách thoải mái đúng không?\nSinh viên: 4, tôi đói",
    "Nhận xét: Câu trả lời của sinh viên là con số khác 0, 1, 2, 3 hoặc không cung cấp bất kỳ thông tin nào về cảm nhận của họ đối với câu hỏi.\n\nĐiểm: W",
    "Tư vấn viên: 1. Bạn cảm thấy bản thân khó mà nghỉ ngơi một cách thoải mái đúng không?\nSinh viên: tôi đói\nTư vấn viên: Cảm ơn bạn đã chia sẻ suy nghĩ của mình. Tôi hiểu rằng bạn đang cảm thấy đói, nhưng tôi muốn biết liệu bạn có gặp khó khăn khi nghỉ ngơi hay không.\nSinh viên: hong, không có, hầu như không, tôi bình thường",
    "Nhận xét: Câu trả lời của sinh viên là không (hong, không có, hầu như không) hoặc là bình thường cho thấy họ có không có cảm xúc tiêu cực nào trong việc khó mà nghỉ ngơi một cách thoải mái.\n\nĐiểm: 0",
    # "Tư vấn viên: 3. Bạn cảm thấy cảm xúc hiện tại của bạn đang rất tiêu cực không?\nSinh viên: không có đâu, tôi đang rất vui vẻ và thoải mái",
    # "Nhận xét: Câu trả lời của sinh viên là không hoặc đưa ra cảm xúc tích cực trái ngược với cảm xúc tiêu cực được đề cập trong câu hỏi, điều này cho thấy họ không có cảm xúc tiêu cực nào hết.\n\nĐiểm: 0",
]
