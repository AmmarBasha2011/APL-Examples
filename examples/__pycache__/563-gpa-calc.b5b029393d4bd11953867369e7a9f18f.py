
# apl-source:1
# مثال 563 — المعدل التراكمي
# apl-source:2
# GPA calculator
# apl-source:3
# Demonstrates: GPA، ساعات معتمدة، متوسط موزون
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/563-gpa-calc.apl
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
# المعدل التراكمي بالساعات المعتمدة
# apl-source:15
مواد = [["برمجة", 3, 4.0], ["رياضيات", 3, 3.7], ["فيزياء", 2, 3.0], ["تخرج", 4, 3.3]]
# apl-source:16
نقاط = 0
# apl-source:17
ساعات_كلية = 0
# apl-source:18
for مادة in مواد:
    # apl-source:19
    نقاط = نقاط + مادة[1] * مادة[2]
    # apl-source:20
    ساعات_كلية = ساعات_كلية + مادة[1]
    # apl-source:21
    print(مادة[0], ":", مادة[1], "ساعات ×", مادة[2])
# apl-source:22
معدل = نقاط / ساعات_كلية
# apl-source:23
print("الساعات:", ساعات_كلية, "| النقاط:", round(نقاط, 2))
# apl-source:24
print("المعدل:", round(معدل, 2))
# apl-source:25
تأكد_يساوي(ساعات_كلية, 12, "إجمالي الساعات")
# apl-source:26
تأكد_يساوي(round(معدل, 2), 3.52, "المعدل التراكمي")
# apl-source:27
