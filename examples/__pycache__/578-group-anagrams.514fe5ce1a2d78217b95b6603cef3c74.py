
# apl-source:1
# مثال 578 — تجميع المتناقضات
# apl-source:2
# Group anagrams
# apl-source:3
# Demonstrates: أناجرام، تجميع، مفاتيح مرتبة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/578-group-anagrams.apl
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
# تجميع المتشابهات الأبجدية بمفتاح الفرز
# apl-source:15
def جمّع(كلمات):
    # apl-source:16
    مجموعات = dict()
    # apl-source:17
    for كلمة in كلمات:
        # apl-source:18
        مفتاح = "".join(sorted(list(كلمة)))
        # apl-source:19
        if مفتاح in مجموعات:
            # apl-source:20
            مجموعات[مفتاح].append(كلمة)
        # apl-source:21
        else:
            # apl-source:22
            مجموعات[مفتاح] = [كلمة]
    # apl-source:23
    نتيجة = list()
    # apl-source:24
    for مفتاح in مجموعات:
        # apl-source:25
        نتيجة.append(sorted(مجموعات[مفتاح]))
    # apl-source:26
    return sorted(نتيجة)
# apl-source:27

# apl-source:28
تأكد_يساوي(جمّع(["eat", "tea", "tan", "ate", "nat", "bat"]), [["ate", "eat", "tea"], ["bat"], ["nat", "tan"]], "ثلاث مجموعات")
# apl-source:29
تأكد_يساوي(جمّع(["a"]), [["a"]], "كلمة واحدة")
# apl-source:30
