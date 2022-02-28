from base64 import encode


for day in range(1,51):
    report_file = open("{}주차.txt".format(day), "w", encoding="utf8")
    print("-{} 주차 주간보고 -".format(day), file=report_file)
    print("부서 : ", file=report_file)
    print("이름 : ", file=report_file)
    print("업무 요약 : ", file=report_file)
    report_file.close()