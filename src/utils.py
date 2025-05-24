import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, AutoConfig
import os

from huggingface_hub import login
login(token = "") # Đăng nhập vào Hugging Face Hub

system_prompt = "Bạn là một trợ lí Tiếng Việt nhiệt tình và trung thực. Hãy luôn trả lời một cách hữu ích nhất có thể, đồng thời giữ an toàn.\n"
system_prompt += "Câu trả lời của bạn không nên chứa bất kỳ nội dung gây hại, phân biệt chủng tộc, phân biệt giới tính, độc hại, nguy hiểm hoặc bất hợp pháp nào. Hãy đảm bảo rằng các câu trả lời của bạn không có thiên kiến xã hội và mang tính tích cực."
system_prompt += "Nếu một câu hỏi không có ý nghĩa hoặc không hợp lý về mặt thông tin, hãy giải thích tại sao thay vì trả lời một điều gì đó không chính xác. Nếu bạn không biết câu trả lời cho một câu hỏi, hãy trẳ lời là bạn không biết và vui lòng không chia sẻ thông tin sai lệch."


class VistralChatbot:
    def __init__(self, prompt=system_prompt):
        """Hàm gọi chatbot của Việt Nam.
        Call: có lưu lịch sự cuộc hội thoại, truyền nhiều lần. Làm mới bằng cách để param reset=True

        Args:
            prompt (str): Chỉnh phong cách chatbot
        >>> VistralChatbot("Bạn là một trợ lí Tiếng Việt nhiệt tình và trung thực.")
        """
        
        # Gọi tokenizer và model
        self.tokenizer = AutoTokenizer.from_pretrained('Viet-Mistral/Vistral-7B-Chat')
        self.model = AutoModelForCausalLM.from_pretrained(
            'Viet-Mistral/Vistral-7B-Chat',
            torch_dtype=torch.bfloat16, # change to torch.float16 if you're using V100
            device_map="auto",
            use_cache=True,
            cache_dir="/workspace/vinhnq/saved_models",
            
        )
        
        self.prompt = prompt # Chuyền cách prompt ban đầu để chỉnh phong các chatbot
        
        # Chỉnh cuộc hội thoại ban đầu
        self.conversation = [{"role": "system", "content": self.prompt }]
        
    def call(self, human, prompt, reset=True, specific = False, add = False):
        """Tương tác với chatbot

        Args:
            human (string): Câu hội thoại.
            reset (bool, optional): Làm mới cuộc hội thoại. Defaults to False.
            prompt (string): Chỉnh phong cách chatbot.
        >>> Call("Xin chào, bạn là ai?")
        Tôi là Nhị đẹp trai, tốt bụng, luôn quan tâm và giúp đỡ người khác.
        """
        
        # Làm mới cuộc hội thoại
        if reset:
            self.prompt = prompt
            self.conversation = [{"role": "system", "content": self.prompt }]
            print("The chat history has been cleared!")
        
        if add:
            self.conversation.extend(add)
        
        # Truyền cuộc hội thoại của người vào
        self.conversation.append({"role": "user", "content": human })
        
        # Chỉnh thông số
        
        if specific:
            input_ids = self.tokenizer.apply_chat_template(self.conversation, return_tensors="pt").to(self.model.device)
            out_ids = self.model.generate(
                input_ids=input_ids,
                max_new_tokens=768,
                do_sample=True,
                top_p=0.1,
                top_k=2,
                temperature=0.1
            )
        else:
            input_ids = self.tokenizer.apply_chat_template(self.conversation, return_tensors="pt").to(self.model.device)
            
            out_ids = self.model.generate(
                input_ids=input_ids,
                max_new_tokens=768,
                do_sample=True,
                top_p=0.6,
                top_k=30,
                temperature=0.2,
                repetition_penalty=1.05,
            )
        assistant = self.tokenizer.batch_decode(out_ids[:, input_ids.size(1): ], skip_special_tokens=True)[0].strip()
        # Truyền cuộc hội thoại của chatbot vào
        self.conversation.append({"role": "assistant", "content": assistant })
        return assistant
    

class PhoGPTChatbot:
    def __init__(self):
        """Hàm gọi chatbot của Việt Nam.
        Call: có lưu lịch sự cuộc hội thoại, truyền nhiều lần. Làm mới bằng cách để param reset=True

        >>> PhoGPTChatbot("Bạn là một trợ lí Tiếng Việt nhiệt tình và trung thực.")
        """
        
        model_path = "vinai/PhoGPT-4B-Chat"  

        config = AutoConfig.from_pretrained(model_path, trust_remote_code=True)  
        config.init_device = "cuda"
        # config.attn_config['attn_impl'] = 'flash' # If installed: this will use either Flash Attention V1 or V2 depending on what is installed

        self.model = AutoModelForCausalLM.from_pretrained(
            model_path, 
            config=config, 
            torch_dtype=torch.bfloat16, 
            trust_remote_code=True,
            cache_dir ="/workspace/ai_intern/Shine/pretrained_weights"
            )
        # If your GPU does not support bfloat16:
        # model = AutoModelForCausalLM.from_pretrained(model_path, config=config, torch_dtype=torch.float16, trust_remote_code=True)
        self.model.eval()  

        self.tokenizer = AutoTokenizer.from_pretrained(model_path, trust_remote_code=True)  

        PROMPT_TEMPLATE = "### Câu hỏi: {instruction}\n### Trả lời:"  
        
    def call(self, human, prompt, reset=True, specific = False, add = False):
        """Tương tác với chatbot

        Args:
            human (string): Câu hội thoại.
            reset (bool, optional): Làm mới cuộc hội thoại. Defaults to False.
            prompt (string): Chỉnh phong cách chatbot.
        >>> Call("Xin chào, bạn là ai?")
        Tôi là Nhị đẹp trai, tốt bụng, luôn quan tâm và giúp đỡ người khác.
        """
        
        # Làm mới cuộc hội thoại
        if reset:
            self.prompt = prompt
            self.conversation = [{"role": "system", "content": self.prompt }]
            print("The chat history has been cleared!")
        
        # Truyền cuộc hội thoại của người vào
        self.conversation.append({"role": "user", "content": human })
        
        # Chỉnh thông số
        
        if specific:
            if add:
                self.conversation.extend(add)
            input_prompt = self.tokenizer.apply_chat_template(self.conversation, return_tensors="pt", tokenize=False, add_generation_prompt=True)
            input_ids = self.tokenizer(input_prompt, return_tensors="pt")  
            out_ids = self.model.generate(
                inputs=input_ids["input_ids"].to("cuda"),  
                attention_mask=input_ids["attention_mask"].to("cuda"),  
                max_new_tokens=768,
                do_sample=True,
                top_p=0.1,
                top_k=2,
                temperature=0.1,
                eos_token_id=self.tokenizer.eos_token_id,  
                pad_token_id=self.tokenizer.pad_token_id  
            )
        else:
            input_prompt = self.tokenizer.apply_chat_template(self.conversation, return_tensors="pt", tokenize=False, add_generation_prompt=True)
            input_ids = self.tokenizer(input_prompt, return_tensors="pt")  
            out_ids = self.model.generate(
                inputs=input_ids["input_ids"].to("cuda"),  
                attention_mask=input_ids["attention_mask"].to("cuda"),  
                max_new_tokens=768,
                do_sample=True,
                top_p=0.9,
                top_k=30,
                temperature=1,
                repetition_penalty=1.05,
                eos_token_id=self.tokenizer.eos_token_id,  
                pad_token_id=self.tokenizer.pad_token_id  
            )
        response = self.tokenizer.batch_decode(out_ids, skip_special_tokens=True)[0]  
        response = response.split("### Trả lời:")[1]

        return response
