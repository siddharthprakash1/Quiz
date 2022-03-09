#question object has the attribute text,answer
class Question:
    def __init__(self,q_text,q_answer):
    # ur parameter inside init can be anything but for simplicity its same as the method
        self.text=q_text
        self.answer=q_answer
