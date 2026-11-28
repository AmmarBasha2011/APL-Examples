
# apl-source:1
# مثال 2157 — صنف قائمة مهام
# apl-source:2
# Todo list class
# apl-source:3
# Demonstrates: أصناف
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2157-todo-list-class-complete-and-remaining.apl
# apl-source:6

# apl-source:7
# # كل مهمة لها حالة
# apl-source:8
# # المتبقي هو غير المنجز
# apl-source:9

# apl-source:10
def تأكد_يساوي(فعلي, متوقع, اسم):
  # apl-source:11
  if فعلي != متوقع:
    # apl-source:12
    print("فشل:", اسم)
    # apl-source:13
    print("  متوقع:", متوقع)
    # apl-source:14
    print("  فعلي:", فعلي)
    # apl-source:15
    قياسي_نظام_اخرج(1)
  # apl-source:16
  print("ناجح:", اسم)
# apl-source:17

# apl-source:18
class مهام:
    # apl-source:19
    def __init__(ذات):
        # apl-source:20
        ذات.قائمة = []
# apl-source:21

    # apl-source:22
    def اضف(ذات, عنوان):
        # apl-source:23
        ذات.قائمة = ذات.قائمة + [[عنوان, False]]
# apl-source:24

    # apl-source:25
    def انجز(ذات, عنوان):
        # apl-source:26
        for م in ذات.قائمة:
            # apl-source:27
            if م[0] == عنوان:
                # apl-source:28
                م[1] = True
                # apl-source:29
                return True
        # apl-source:30
        return False
# apl-source:31

    # apl-source:32
    def متبقي(ذات):
        # apl-source:33
        عدد = 0
        # apl-source:34
        for م in ذات.قائمة:
            # apl-source:35
            if م[1] == False:
                # apl-source:36
                عدد = عدد + 1
        # apl-source:37
        return عدد
# apl-source:38

# apl-source:39
ت = مهام()
# apl-source:40
ت.اضف("a")
# apl-source:41
ت.اضف("b")
# apl-source:42
ت.اضف("c")
# apl-source:43
تأكد_يساوي(ت.متبقي(), 3, "ثلاث")
# apl-source:44
تأكد_يساوي(ت.انجز("b"), True, "إنجاز")
# apl-source:45
تأكد_يساوي(ت.انجز("z"), False, "غير موجودة")
# apl-source:46
تأكد_يساوي(ت.متبقي(), 2, "اثنتان")
# apl-source:47
