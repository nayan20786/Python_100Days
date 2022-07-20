class QuizBrain:
    def __init__(self, q_list):
        self.qno = 0
        self.q_list = q_list

    def QuestionTime(self):
        is_correct = 0

        for a in self.q_list:
            answer = input(f"Q{self.qno}.{a.text}")
            self.qno = self.qno + 1
            if answer == a.answer:
                is_correct += 1
                print("Correct:😁Less go dababy")
            else:
                print("Incorrect")
            print(f"The Correct Answer is :: {a.answer}")

        return is_correct
