import sys

if len(sys.argv) > 1:
    filename = sys.argv[1]
    with open(filename, 'r') as f:
        qna = f.read()
        qna = qna.split("\n")
        mid = int(len(qna)/2)
        questions = qna[:mid]
        answers= qna[mid:]

    
    failed = []
    for i in range(len(questions)):
        print(questions[i])
        my_ans = input("> ").strip()
        if my_ans == answers[i]:
            print("success")
        else:
            fail_msg = (f"fail: {my_ans} -> {answers[i]}")
            print(fail_msg)
            failed.append(fail_msg)

    if failed:
        print(*failed, sep="\n")

        
else:
    print("No file provided.")
