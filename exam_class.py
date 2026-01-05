import puzzles

class Exam:
    def __init__(self, player):
        self.player = player
        self.exam_completed = 0
        self.puzzles = puzzles.Puzzles() 

    def start_exam_one(self):
        print("\nYou are about to take Exam One!")
        ready = input("\nAre you ready to begin the exam? (yes/no) ").lower()

        print("\nStarting the exam...")
        self.puzzles.riddle()

    def check_exam_completion(self):
        if self.puzzles.rid_complete:
            self.exam_completed += 1
            self.player.stats["exams_completed"] = self.exam_completed
            print("\nCongratulations! You have passed Exam One.")
        else:
            print("\nYou failed Exam One.")
