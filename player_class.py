import exam_class, act_one

class Player:
    def __init__(self):
        self.name = act_one.tutorial.name
        self.level = 1
        self.stats = {"title":None, "partner": None, "exams_completed": 0, "lives":1}
       
    def pick_gender(self):
        while True:
            user_gender = input("\nDo you want to take on the new name of Felix or Amelia? ").lower()
            if user_gender == "felix":
                self.gender = "boy"
                self.name = "Felix"
                self.stats["title"] = "Commoner"
                break
            elif user_gender == "amelia":
                self.gender = "girl"
                self.name = "Amelia"
                self.stats["title"] = "Commoner"
                break
            else:
                print("Invalid input. Please enter 'boy' or 'girl'.")
        
    def display_info(self):
        self.pick_gender()
        print("Welcome EXTRA CREDIT — SURVIVE: Edition - You should have been worth more points!")
        print(f"\nLoading Player.... {self.name}")
        print(f"\nPlayer Info: \nName: {self.name} \nTitle: {self.stats['title']} \nLives: {self.stats['lives']}")


    def player_exams(self):
        exam = exam_class.Exam(self)
        exam.start_exam_one()
        exam.check_exam_completion()


    def play(self):
        act_one.starting_text()
        act_one.tutorial()
        self.player_exams()
        print(f"\nExams Completed: {self.stats['exams_completed']}")
        print("\nThank you for playing EXTRA CREDIT — SURVIVE: Edition: You should have been worth more points!")

player = Player()
player.play()
print(f"{player.name}")

