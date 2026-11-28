
# apl-source:1
# مثال 1113 — مجموعة بحذف سريع
# apl-source:2
# Randomized set with swap delete
# apl-source:3
# Demonstrates: بدل بآخر عنصر
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1113-randomized-set.apl
# apl-source:6

# apl-source:7
# الحذف يبدل العنصر بآخر عنصر ثم يحذف الأخير
# apl-source:8
# فلا نحتاج إزاحة بقية العناصر
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
class مجموعة_سريعة:
    # apl-source:19
    def __init__(ذات):
        # apl-source:20
        ذات.عناصر = []
# apl-source:21

    # apl-source:22
    def ادرج(ذات, س):
        # apl-source:23
        if س in ذات.عناصر:
            # apl-source:24
            return False
        # apl-source:25
        ذات.عناصر = ذات.عناصر + [س]
        # apl-source:26
        return True
# apl-source:27

    # apl-source:28
    def ازل(ذات, س):
        # apl-source:29
        if س not in ذات.عناصر:
            # apl-source:30
            return False
        # apl-source:31
        ف = 0
        # apl-source:32
        while ذات.عناصر[ف] != س:
            # apl-source:33
            ف = ف + 1
        # apl-source:34
        ذات.عناصر[ف] = ذات.عناصر[-1]
        # apl-source:35
        ذات.عناصر.pop()
        # apl-source:36
        return True
# apl-source:37

    # apl-source:38
    def حجم_المجموعة(ذات):
        # apl-source:39
        return len(ذات.عناصر)
# apl-source:40

# apl-source:41
م = مجموعة_سريعة()
# apl-source:42
تأكد_يساوي(م.ادرج(1), True, "إدراج 1")
# apl-source:43
تأكد_يساوي(م.ازل(2), False, "حذف غائب")
# apl-source:44
تأكد_يساوي(م.ادرج(2), True, "إدراج 2")
# apl-source:45
تأكد_يساوي(م.حجم_المجموعة(), 2, "حجمان")
# apl-source:46
تأكد_يساوي(م.ازل(1), True, "حذف 1")
# apl-source:47
تأكد_يساوي(م.ادرج(2), False, "إدراج مكرر")
# apl-source:48
تأكد_يساوي(م.حجم_المجموعة(), 1, "حجم واحد")
# apl-source:49
