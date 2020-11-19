"""
Stepik backend for COP3530 at the University of Florida
Written by Ori Leibovici and Hamish Pierpont
"""


def generate():
    
    def create_feedback(input):
        if "\n" in input:
            feedback = "Incorrect answer: input was:\n------------\n{}\n------------".format(input)
        else:
            feedback = "Incorrect answer: input was {}".format(input)
        return feedback
    
    def append_newline(input):
        return input + '\n'
        
    def zip_into_list(list_1, list_2):
        return list(zip(list_1, list_2))
    
    tests = [] #Put tests in here as strings without newlines at end - feedback will look mangled otherwise
    correct_answers = [] #Put correct answers in here as strings
    
    list_of_feedback  = map(create_feedback, tests) #Generate list of feedback for tests
    tests_with_newlines = map(append_newline, tests) #Add newlines to tests
    
    right_answers_with_feedback = zip_into_list(correct_answers, list_of_feedback)
    tests_with_answers_and_feedback = zip_into_list(tests_with_newlines, right_answers_with_feedback) #Create list of [tests, [clues, feedback]]
    
    return tests_with_answers_and_feedback


def check(reply, clue):

    compliments = ["Good work!",
                   "Brilliant!",
                   "Alan Turing would be proud.",
                   "You are a genius!",
                   "Wowza!"
                ]
                
    if isinstance(clue, str):
        if reply.strip() == clue.strip():
            return True, compliments[len(reply) % 5]
        else:
            return False, "Try again..."
    else:
        if reply.strip() == clue[0]:
            return True, compliments[len(reply) % 5]
        else:
            return False, clue[0]


