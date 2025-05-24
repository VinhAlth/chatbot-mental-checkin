class Bye:
    def __init__(self, li: list):
        self.li = li
        
        self.score = sum(li)
        
        if self.score <= 4: self.name_score =  "tinh thần khỏe mạnh"
        elif 5 <= self.score <= 9: self.name_score =  "tinh thần tốt"
        elif 10 <= self.score <= 14: self.name_score =  "tinh thần ổn định"
        elif 15 <= self.score <= 19: self.name_score =  "tinh thần mỏng manh"
        else: self.name_score =  "tinh thần yếu đuối"
        
    def _coreSymptoms(self):
        return +(self.li[0]!=0) +(self.li[1]!=0)
    
    def _otherSymptoms(self):
        return +(self.li[5]!=0) +(self.li[6]!=0) +(self.li[8]!=0)
    
    def _somaticSymptoms(self):
        return +(self.li[2]!=0) +(self.li[3]!=0) +(self.li[4]!=0) +(self.li[7]!=0)
    
    def dontknow(self):
        if self._coreSymptoms():
            s1 = ("sinh viên có dấu hiệu chính của tinh thần yếu đuối. ", 1)
        else:
            s1 = ("sinh viên không có dấu hiệu chính của tinh thần yếu đuối. ", 0)
            
        if self._otherSymptoms() + self._coreSymptoms() >= 3:
            s2 = ("sinh viên có vài dấu hiệu liên quan. ", 2)
        elif self._otherSymptoms()==0:
            s2 = ("sinh viên không có dấu hiệu liên quan. ",0)
        else:
            s2 = ("sinh viên chỉ có vài dấu hiệu liên quan. ",1)
            
            
        if self._somaticSymptoms()>2:
            s3 = ("sinh viên có 1 số dấu hiệu về cơ thể. ", 2)
        elif self._somaticSymptoms()==0:
            s3 = ("sinh viên không có dấu hiệu về cơ thể. ", 0)
        else:
            s3 = ("sinh viên chỉ có vài dấu hiệu về cơ thể. ", 1)
            
        if s1[1]:
            if s2[1]==2:
                s = s1[0] + s2[0] + "Cho thấy sinh viên có khả năng có tinh thần không khỏe mạnh. Và "
                if s3[1]==2:
                    s+= s3[0] + "cho thấy sinh viên có 1 tinh thần yếu đuối."
                else:
                    s+= s3[0] + "cho thấy sinh viên có 1 tinh thần ổn định."
            else:
                s = "Mặc dù " + s1[0] + "Nhưng " + s2[0] + "Cho thấy sinh viên có khả năng có tinh thần tốt. "
                if s3[1]==2:
                    s+= "Nhưng " + s3[0] + "cho thấy sinh viên có 1 cơ thể không khỏe mạnh."
                else:
                    s+= "Và " + s3[0] + "cho thấy sinh viên có 1 tinh thần tốt."
        else:
            if s2[1]==2:
                if s3[1]==2:
                    s = "Mặc dù " + s2[0] +  "Và " + s3[0] + "Nhưng " + s1[0] + "Cho thấy sinh viên có khả năng có tinh thần tốt."
                else:
                    s = "Mặc dù " + s2[0] +  "Nhưng " + s1[0] +  "Và " + s3[0] + "Cho thấy sinh viên có khả năng có tinh thần tốt."
            else:
                if s3[1]==2:
                    s = "Mặc dù " + s3[0] +  "Nhưng " + s1[0] +  "Và " + s2[0] + "Cho thấy sinh viên có khả năng có tinh thần tốt."
                else:
                    s = s1[0] + s2[0] + "Và " + s3[0] + "cho thấy sinh viên có 1 tinh thần khỏe mạnh."                
        return  self._level() + s
        
    def _level(self):
        num_symptoms = self._otherSymptoms() + self._coreSymptoms() + self._somaticSymptoms()
        if num_symptoms < 5:
            return "Sinh viên có trên 4 dấu hiệu tích cực nên sinh viên có tinh thần khỏe mạnh. "
        elif num_symptoms < 8 and self._count(1) and ( (self._count(2)+self._count(3))/self._count(1) <= 0.6 ):
            return "Sinh viên có 1 số dấu hiệu không tốt nhưng chỉ ở mức nhẹ nên sinh viên có tinh thần tốt. "
        elif self.name_score == "tinh thần yếu đuối":
            return "Sinh viên có hầu hết các dấu hiệu và các dấu hiệu có ảnh hưởng rõ rệt đến cuộc sống. "
        else:
            return "Sinh viên có hầu hết các dấu hiệu hoặc có 1 số dấu hiệu ở mức hơi cao. "
            
    def _count(self, num):
        out = self.li.count(num)
        if num == 0:
            out = 9 - self.li.count(num)
        return out

    
    
        
