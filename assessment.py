class Assessment:
    def __init__(self, title, max_score):
        self.title = title
        self.max_score = max_score

    def calculate_percentage(self, score):
        return (score / self.max_score) * 100

    def grade_message(self, score):
        percentage = self.calculate_percentage(score)

        if percentage <= 60:
            return "Need improvement"
        elif percentage <= 85:
            return "Good"
        else:
            return "Great job"

    def display_info(self):
        print("Title:", self.title)
        print("Max Score:", self.max_score)
