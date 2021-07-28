from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import*
from random import shuffle, randint


class Question():
    def __init__(self, question, right_ans, wrong_ans1, wrong_ans2, wrong_ans3):
        self.question = question
        self.right_ans = right_ans
        self.wrong_ans1 = wrong_ans1
        self.wrong_ans2 = wrong_ans2
        self.wrong_ans3 = wrong_ans3
        

app = QApplication([])
window = QWidget()
window.right_responses = 0
window.questions_asked = 0
window.questions_correct = 0
window.setWindowTitle('Test')
window.resize(800,600)



#______________________________________________________________________________________________

proceed_btn = QPushButton('Confirm')
question = QLabel('If you have 1 banana and 5 apples, what are the chances of unraveling a button?')

button_box = QGroupBox('Possible Answers:')
ans1 = QRadioButton('50%')
ans2 = QRadioButton('78%')
ans3 = QRadioButton('?????')
ans4 = QRadioButton('stainless steel')

button_ans_box = QGroupBox('Question Results:')
question_results = QLabel('Correct! :)')
try:
    question_ans = QLabel(f'Statistics:<br>-Questions asked: {window.questions_asked}<br>-Questions answered correctly: {window.questions_correct}<br>-Correctness percentage: {(window.questions_correct) / (window.questions_asked) * 100}')
except:
    question_ans = QLabel(f'Statistics:<br>-Questions asked: {window.questions_asked}<br>-Questions answered correctly: {window.questions_correct}<br>-Correctness percentage: 0.0')
questions_correct_ans = QLabel('')
layout_ans = QVBoxLayout()
layout_ans.addWidget(question_results, alignment = (Qt.AlignLeft | Qt.AlignTop))
layout_ans.addWidget(question_ans, alignment = Qt.AlignHCenter, stretch = 2)
layout_ans.addWidget(questions_correct_ans, alignment = Qt.AlignCenter)
questions_correct_ans.hide()

button_ans_box.setLayout(layout_ans)

radiogroup = QButtonGroup()
radiogroup.addButton(ans1)
radiogroup.addButton(ans2)
radiogroup.addButton(ans3)
radiogroup.addButton(ans4)

layout1 = QHBoxLayout()
layout2 = QVBoxLayout()
layout3 = QVBoxLayout()

layout2.addWidget(ans1)
layout2.addWidget(ans2)
layout3.addWidget(ans3)
layout3.addWidget(ans4)

layout1.addLayout(layout2)
layout1.addLayout(layout3)

button_box.setLayout(layout1)


line1 = QHBoxLayout()
line2 = QHBoxLayout()
line3 = QHBoxLayout()

line1.addWidget(question, alignment = Qt.AlignCenter)
line2.addWidget(button_box)
line2.addWidget(button_ans_box)
button_ans_box.hide()
line3.addStretch(1)
line3.addWidget(proceed_btn, stretch = 1.5)
line3.addStretch(1)

whole_layout11 = QVBoxLayout()
whole_layout11.addLayout(line1, stretch = 2)
whole_layout11.addLayout(line2, stretch = 8)
whole_layout11.addStretch(1)
whole_layout11.addLayout(line3, stretch = 1)
whole_layout11.addStretch(1)
whole_layout11.setSpacing(5)

window.setLayout(whole_layout11)


#______________________________________________________________________________________________

#_______________________________________________________________________________

def showres():
    button_box.hide()
    button_ans_box.show()
    proceed_btn.setText("Proceed")
def showques():
    button_ans_box.hide()
    button_box.show()
    radiogroup.setExclusive(False)
    ans1.setChecked(False)
    ans2.setChecked(False)
    ans3.setChecked(False)
    ans4.setChecked(False)
    radiogroup.setExclusive(True)
    proceed_btn.setText("Confirm")
def test():
    if proceed_btn.text() == "Confirm":
        showres()
    else:
        showques()

answers = [ans1, ans2, ans3, ans4]

def ask(q):
    window.questions_asked += 1
    answers[0].setText(q.right_ans)
    answers[1].setText(q.wrong_ans1)
    answers[2].setText(q.wrong_ans2)
    answers[3].setText(q.wrong_ans3)
    question.setText(q.question)
    # try:
    #     question_ans.setText(f'Statistics:<br>-Questions asked: {window.questions_asked}<br>-Questions answered correctly: {window.questions_correct}<br>-Correctness percentage: {(window.questions_correct) / (window.questions_asked) * 100}')
    # except:
    #     question_ans.setText(f'Statistics:<br>-Questions asked: {window.questions_asked}<br>-Questions answered correctly: {window.questions_correct}<br>-Correctness percentage: 0.0')
    showques()

def showcorrect(yesorno):
    question_results.setText(yesorno)
    showres()

def checkans():
    if answers[0].isChecked():
        showcorrect("Correct! :)")
        questions.remove(window.questiontoask)
        if questions == []:
            showcorrect('Final score:')
            question.setText('End of test.')
            question_ans.setText(f'Statistics:<br>-Number of questions: 10<br>-Questions answered correctly: {window.questions_correct}<br>-Questions asked: {window.questions_asked}<br>-Correctness percentage: {(window.questions_correct) / (window.questions_asked) * 100}')
        window.questions_correct += 1
    elif answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
        showcorrect("Incorrect... :(")
    print('_________________________________________')
    print('Statistics:')
    print('-Questions asked:', str(window.questions_asked))
    print('-Questions answered correctly:', str(window.questions_correct))
    print('-Percentage correct:', str(window.questions_correct / window.questions_asked * 100))

def nextques():
    window.questiontoask = questions[randint(0, len(questions) - 1)]
    ask(window.questiontoask)

def check_what_todo():
    if proceed_btn.text() == 'Confirm':
        questions_correct_ans.hide()
        checkans()
        try:
            question_ans.setText(f'Statistics:<br>-Questions asked: {window.questions_asked}<br>-Questions answered correctly: {window.questions_correct}<br>-Correctness percentage: {round((window.questions_correct) / (window.questions_asked) * 100, 1)}')
        except:
            question_ans.setText(f'Statistics:<br>-Questions asked: {window.questions_asked}<br>-Questions answered correctly: {window.questions_correct}<br>-Correctness percentage: 0.0')
    elif proceed_btn.text() == 'Proceed':
        questions_correct_ans.setText(str(window.right_responses))
        questions_correct_ans.show()
        nextques()
        try:
            question_ans.setText(f'Statistics:<br>-Questions answered correctly: {window.questions_correct}<br>-Questions asked: {window.questions_asked}<br>-Correctness percentage: {(window.questions_correct) / (window.questions_asked) * 100}')
        except:
            question_ans.setText(f'Statistics:<br>-Questions answered correctly: {window.questions_correct}<br>-Questions asked: {window.questions_asked}<br>-Correctness percentage: 0.0')
    else:
        nextques()

question1 = Question("How much money is a camel worth?", '50,000', '10,000', '5,000', '100,000')
question2 = Question("How many bananas does it take to explode?", '10,000', '100,000', '50,000', '5,000')
question3 = Question("How much money would it take to buy the whole world?", '200 trillion', '100 trillion', '750 trillion', '1 quadrillion')
question4 = Question("How many iguanas are there in the world?", "250,000", '100,000', '50,000', '500,000')
question5 = Question("What person is NOT carved into Mount Rushmore?", "John F. Kennedy", 'George Washington', 'Thomas Jefferson', 'Theodore Roosevelt')
question6 = Question('How many carrots do you have to eat to turn orange?', '300', '200', '100', '50')
question7 = Question('Which social media app users manipulated the stock market together?', 'Reddit', 'Instagram', 'Facebook', 'Twitter')
question8 = Question('Which country has no capital?', 'Nauru', 'France', 'Bhutan', 'Armenia')
question9 = Question('Who was the first Canadian in space?', 'Marc Ganeau', 'Neil Armstrong', 'Billy Bob Joe', 'Gordon Ramsay')
question10 = Question('Who voiced the rabbit in Zootopia?', 'Ginnifer Goodwin', 'Terry Stronk', 'Samantha Smith', 'Chonky Bonk')
questions = [question1, question2, question3, question4, question5, question6, question7, question8, question9, question10]
shuffle(questions)


proceed_btn.clicked.connect(check_what_todo)
nextques()
window.show()

app.exec_()


#YAAAAAAAAAAAAAAAAAAAY I FINALLY FINISHED
