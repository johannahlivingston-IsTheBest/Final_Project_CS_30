import exam_class

class Player:
    def __init__(self):
        self.name = None
        self.level = 1
        self.stats = {"title":None, "partner": None, "exams_completed": 0, "deaths":0}
        self.gender = None
    def pick_gender(self):
        while True:
            user_gender = input("\nAre you a boy or a girl? ").lower()
            if user_gender == "boy":
                self.gender = "boy"
                self.name = "Felix"
                break
            elif user_gender == "girl":
                self.gender = "girl"
                self.name = "Amelia"
                break
            else:
                print("Invalid input. Please enter 'boy' or 'girl'.")
            self.stats["title"] = "Commoner"
        
    def display_info(self):
        self.pick_gender()
        print("Welcome EXTRA CREDIT — SURVIVE: Edition - You should have been worth more points!")
        print(f"\nLoading Player.... {self.name}")
        print(f"\nPlayer Info: \nName: {self.name} \nGender: {self.gender.title()} \nTitle: {self.stats['title']}")


    def player_exams(self):
        exam = exam_class.Exam(self)
        exam.start_exam_one()
        exam.check_exam_completion()


    def play(self):
        self.display_info()
        self.player_exams()
        print(f"\nExams Completed: {self.stats['exams_completed']}")
        print("\nThank you for playing EXTRA CREDIT — SURVIVE: Edition: You should have been worth more points!")

player = Player()

player.play()

