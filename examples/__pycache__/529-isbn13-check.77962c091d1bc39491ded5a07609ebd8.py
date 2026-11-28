
# apl-source:1
# مثال 529 — تحقق ردمك ISBN-13
# apl-source:2
# ISBN-13 validation
# apl-source:3
# Demonstrates: ردمك ISBN-13، رقم تحقق
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/529-isbn13-check.apl
# apl-source:6

# apl-source:7
def تأكد_يساوي(فعلي, متوقع, اسم):
    # apl-source:8
    if فعلي != متوقع:
        # apl-source:9
        print("فشل:", اسم, "| متوقع:", متوقع, "| فعلي:", فعلي)
        # apl-source:10
        قياسي_نظام_اخرج(1)
    # apl-source:11
    print("ناجح:", اسم)
# apl-source:12

# apl-source:13

# apl-source:14
# تحقق من ردمك ISBN-13
# apl-source:15
def ردمك_صالح(رقم):
    # apl-source:16
    if len(رقم) != 13:
        # apl-source:17
        return False
    # apl-source:18
    م = 0
    # apl-source:19
    for i in range(12):
        # apl-source:20
        ر = int(رقم[i])
        # apl-source:21
        if i % 2 == 0:
            # apl-source:22
            م = م + ر
        # apl-source:23
        else:
            # apl-source:24
            م = م + 3 * ر
    # apl-source:25
    تحقق = (10 - م % 10) % 10
    # apl-source:26
    return تحقق == int(رقم[12])
# apl-source:27

# apl-source:28
تأكد_يساوي(ردمك_صالح("9780306406157"), True, "ردمك صالح")
# apl-source:29
تأكد_يساوي(ردمك_صالح("9780306406158"), False, "ردمك خاطئ")
# apl-source:30
تأكد_يساوي(ردمك_صالح("123"), False, "طول خاطئ")
# apl-source:31
