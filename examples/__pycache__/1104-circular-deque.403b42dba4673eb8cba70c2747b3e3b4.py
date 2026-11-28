
# apl-source:1
# مثال 1104 — طابور مزدوج دائري
# apl-source:2
# Circular double-ended queue
# apl-source:3
# Demonstrates: فهرس بالباقي
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1104-circular-deque.apl
# apl-source:6

# apl-source:7
# مؤشر رأس وحجم على مصفوفة بسعة ثابتة
# apl-source:8
# الإدخال من الأمام يرجع الرأس خطوة بالباقي
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
class مزدوج_دائري:
    # apl-source:19
    def __init__(ذات, سعة):
        # apl-source:20
        ذات.بيانات = [0] * سعة
        # apl-source:21
        ذات.سعة = سعة
        # apl-source:22
        ذات.رأس = 0
        # apl-source:23
        ذات.حجم = 0
# apl-source:24

    # apl-source:25
    def ادخل_امام(ذات, س):
        # apl-source:26
        if ذات.حجم == ذات.سعة:
            # apl-source:27
            return False
        # apl-source:28
        ذات.رأس = (ذات.رأس - 1) % ذات.سعة
        # apl-source:29
        ذات.بيانات[ذات.رأس] = س
        # apl-source:30
        ذات.حجم = ذات.حجم + 1
        # apl-source:31
        return True
# apl-source:32

    # apl-source:33
    def ادخل_خلف(ذات, س):
        # apl-source:34
        if ذات.حجم == ذات.سعة:
            # apl-source:35
            return False
        # apl-source:36
        ذات.بيانات[(ذات.رأس + ذات.حجم) % ذات.سعة] = س
        # apl-source:37
        ذات.حجم = ذات.حجم + 1
        # apl-source:38
        return True
# apl-source:39

    # apl-source:40
    def احذف_خلف(ذات):
        # apl-source:41
        if ذات.حجم == 0:
            # apl-source:42
            return False
        # apl-source:43
        ذات.حجم = ذات.حجم - 1
        # apl-source:44
        return True
# apl-source:45

    # apl-source:46
    def امام(ذات):
        # apl-source:47
        return ذات.بيانات[ذات.رأس]
# apl-source:48

    # apl-source:49
    def خلف(ذات):
        # apl-source:50
        return ذات.بيانات[(ذات.رأس + ذات.حجم - 1) % ذات.سعة]
# apl-source:51

# apl-source:52
د = مزدوج_دائري(3)
# apl-source:53
تأكد_يساوي(د.ادخل_خلف(1), True, "إدخال خلفي أول")
# apl-source:54
تأكد_يساوي(د.ادخل_خلف(2), True, "إدخال خلفي ثان")
# apl-source:55
تأكد_يساوي(د.ادخل_امام(3), True, "إدخال أمامي")
# apl-source:56
تأكد_يساوي(د.ادخل_امام(4), False, "ممتلئ")
# apl-source:57
تأكد_يساوي(د.خلف(), 2, "الخلف")
# apl-source:58
تأكد_يساوي(د.احذف_خلف(), True, "حذف الخلف")
# apl-source:59
تأكد_يساوي(د.ادخل_امام(4), True, "بعد الحذف")
# apl-source:60
تأكد_يساوي(د.امام(), 4, "الأمام")
# apl-source:61
تأكد_يساوي(د.خلف(), 1, "الخلف الجديد")
# apl-source:62
