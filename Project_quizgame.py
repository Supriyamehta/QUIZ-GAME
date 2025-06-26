print("--------***********----------------***************  WELCOME TO QUIZ GAME OF CHALLENGES  *************-----------------------*******************-------------")
ans = input("DO YOU WANT TO START THE GAME (yes/no): ").upper()

if ans == "YES":
    print("SOME INFORMATION AND RULES ABOUT THE GAME ARE GIVEN BELOW ")
    print("1. ALL QUESTIONS CARRY THREE MARKS ")
    print("2. THERE IS -1 NEGATIVE MARKING IF YOU GIVE THE WRONG ANSWER ")
    print("3. QUESTIONS WILL BE AVAILABLE IN ALL TYPES: 1.TRUE & FALSE 2. MCQ QUESTIONS 3. ONE WORD ANSWER ")
    print("4. THERE ARE QUESTIONS FROM: 1.MATHS 2.SCIENCE 3.G.K 4.COMPUTER")
    print("5. ANSWERING ALL THE QUESTIONS IS MANDATORY ")
    print("6. SCORE DISPLAYED AT THE END OF THE GAME")

    print("\nLET'S START THE GAME:\n")
    SUBJECTS = input("WHICH SUBJECT DO YOU WANT TO ATTEMPT? (MATHS/COMPUTER/SCIENCE): ").strip().upper()
    score = 0

    if SUBJECTS == "MATHS":
        q1 = input("1. What is the value of 3 + 9? \n").lower()
        if q1 == "12" or q1 == "twelve":
            print("Correct")
            score += 3
        else:
            print("Incorrect")
            score -= 1

        q2 = input("2. What is the value of 4 * 9? \n").lower()
        if q2 == "36" or q2 == "thirtysix":
            print("Correct")
            score += 3
        else:
            print("Incorrect")
            score -= 1

        q3 = input("3. What is the square root of 144? \n").lower()
        if q3 == "12" or q3 == "twelve":
            print("Correct")
            score += 3
        else:
            print("Incorrect")
            score -= 1

        q4 = input("4. What is 15% of 200?\n ").lower()
        if q4 == "30" or q4 == "thirty":
            print("Correct")
            score += 3
        else:
            print("Incorrect")
            score -= 1

        q5 = input("5. Solve: (3 + 5) × 2 - 4 = \n").lower()
        if q5 == "12" or q5 == "twelve":
            print("Correct")
            score += 3
        else:
            print("Incorrect")
            score -= 1

        q6 = input("6. What is the next number in the series: 2, 4, 8, 16, ?\n ").lower()
        if q6 == "32" or q6 == "thirtytwo":
            print("Correct")
            score += 3
        else:
            print("Incorrect")
            score -= 1

        q7 = input("7. What is the perimeter of a square with side length 6 cm?\n ").lower()
        if q7 == "24" or q7 == "twentyfour":
            print("Correct")
            score += 3
        else:
            print("Incorrect")
            score -= 1

        q8 = input("8. What is the cube of 3? \n").lower()
        if q8 == "27" or q8 == "twentyseven":
            print("Correct")
            score += 3
        else:
            print("Incorrect")
            score -= 1

        q9 = input("9. A triangle has angles 60°, 60°, and __?\n ").lower()
        if q9 == "60" or q9 == "sixty":
            print("Correct")
            score += 3
        else:
            print("Incorrect")
            score -= 1

        q10 = input("10. What is the value of π (pi) up to 2 decimal places?\n ").lower()
        if q10 == "3.14":
            print("Correct")
            score += 3
        else:
            print("Incorrect")
            score -= 1

    elif SUBJECTS == "COMPUTER":
        print("ONLY ANSWER IN TRUE OR FALSE (T or F)")

        def check_tf(ans, correct):
            return ans in [correct, correct[0]]

        q1 = input("1. RAM is a permanent memory. \n").strip().lower()
        if check_tf(q1, "false"):
            print("Correct")
            score += 3
        else:
            print("Incorrect")
            score -= 1

        q2 = input("2. HTML is a programming language.\n ").strip().lower()
        if check_tf(q2, "false"):
            print("Correct")
            score += 3
        else:
            print("Incorrect")
            score -= 1

        q3 = input("3. RAM stands for Random Access Memory. \n").strip().lower()
        if check_tf(q3, "true"):
            print("Correct")
            score += 3
        else:
            print("Incorrect")
            score -= 1

        q4 = input("4. A byte is made up of 16 bits.\n ").strip().lower()
        if check_tf(q4, "false"):
            print("Correct")
            score += 3
        else:
            print("Incorrect")
            score -= 1

        q5 = input("5. Google Chrome is a web browser. \n").strip().lower()
        if check_tf(q5, "true"):
            print("Correct")
            score += 3
        else:
            print("Incorrect")
            score -= 1

        q6 = input("6. The Internet and the World Wide Web are the same thing.\n ").strip().lower()
        if check_tf(q6, "false"):
            print("Correct")
            score += 3
        else:
            print("Incorrect")
            score -= 1

        q7 = input("7. Linux is an open-source operating system.\n ").strip().lower()
        if check_tf(q7, "true"):
            print("Correct")
            score += 3
        else:
            print("Incorrect")
            score -= 1

        q8 = input("8. A computer virus is a type of hardware. \n").strip().lower()
        if check_tf(q8, "false"):
            print("Correct")
            score += 3
        else:
            print("Incorrect")
            score -= 1

        q9 = input("9. HTML is used to design web pages.\n ").strip().lower()
        if check_tf(q9, "true"):
            print("Correct")
            score += 3
        else:
            print("Incorrect")
            score -= 1

        q10 = input("10. An IP address uniquely identifies a computer on a network.\n ").strip().lower()
        if check_tf(q10, "true"):
            print("Correct")
            score += 3
        else:
            print("Incorrect")
            score -= 1

    elif SUBJECTS == "SCIENCE":
        print("ONLY ANSWER IN TRUE OR FALSE (T or F)")

        def check_tf(ans, correct):
            return ans in [correct, correct[0]]

        q1 = input("1. The Earth is the center of the solar system.\n ").strip().lower()
        if check_tf(q1, "false"):
            print("Correct")
            score += 3
        else:
            print("Incorrect")
            score -= 1

        q2 = input("2. The Sun is a planet.\n ").strip().lower()
        if check_tf(q2, "false"):
            print("Correct")
            score += 3
        else:
            print("Incorrect")
            score -= 1

        q3 = input("3. Water boils at 100°C at sea level.\n ").strip().lower()
        if check_tf(q3, "true"):
            print("Correct")
            score += 3
        else:
            print("Incorrect")
            score -= 1

        q4 = input("4. Sound can travel through a vacuum. \n").strip().lower()
        if check_tf(q4, "false"):
            print("Correct")
            score += 3
        else:
            print("Incorrect")
            score -= 1

        q5 = input("5. Plants produce oxygen during photosynthesis.\n ").strip().lower()
        if check_tf(q5, "true"):
            print("Correct")
            score += 3
        else:
            print("Incorrect")
            score -= 1

        q6 = input("6. Electrons have a positive charge. \n").strip().lower()
        if check_tf(q6, "false"):
            print("Correct")
            score += 3
        else:
            print("Incorrect")
            score -= 1

        q7 = input("7. The human heart has four chambers. ").strip().lower()
        if check_tf(q7, "true"):
            print("Correct")
            score += 3
        else:
            print("Incorrect")
            score -= 1

        q8 = input("8. Atoms are the smallest units of matter.\n ").strip().lower()
        if check_tf(q8, "true"):
            print("Correct")
            score += 3
        else:
            print("Incorrect")
            score -= 1

        q9 = input("9. Carbon dioxide is essential for photosynthesis.\n ").strip().lower()
        if check_tf(q9, "true"):
            print("Correct")
            score += 3
        else:
            print("Incorrect")
            score -= 1

        q10 = input("10. DNA carries genetic information.\n ").strip().lower()
        if check_tf(q10, "true"):
            print("Correct")
            score += 3
        else:
            print("Incorrect")
            score -= 1
    else:
        print("Invalid subject. Exiting the game.")
        exit()

    print("\nYour final score is:", score)

else:
    print("OK BYE!")
