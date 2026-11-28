
# apl-source:1
# مثال 610 — خطوة الثعبان
# apl-source:2
# Snake game step
# apl-source:3
# Demonstrates: ثعبان، نمو، اصطدام
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/610-snake-step.apl
# apl-source:6

# apl-source:7
# Assertion style:
# apl-source:8
#   دالة تأكد_يساوي(فعلي, متوقع, اسم):
# apl-source:9
#     لو فعلي != متوقع:
# apl-source:10
#       اطبع "فشل:", اسم
# apl-source:11
#       اطبع "  متوقع:", متوقع
# apl-source:12
#       اطبع "  فعلي:", فعلي
# apl-source:13
#       قياسي_نظام_اخرج(1)
# apl-source:14
#     اطبع "ناجح:", اسم
# apl-source:15

# apl-source:16
def تأكد_يساوي(فعلي, متوقع, اسم):
  # apl-source:17
  if فعلي != متوقع:
    # apl-source:18
    print("فشل:", اسم)
    # apl-source:19
    print("  متوقع:", متوقع)
    # apl-source:20
    print("  فعلي:", فعلي)
    # apl-source:21
    قياسي_نظام_اخرج(1)
  # apl-source:22
  print("ناجح:", اسم)
# apl-source:23

# apl-source:24
# لعبة الثعبان: خطوة حركة ونمو واصطدام
# apl-source:25
# Demonstrates: جسم كقائمة مواضع, طعام ونمو, كشف الاصطدام بالجدران والذات
# apl-source:26
# منطق لعبة كامل دون رسوميات
# apl-source:27

# apl-source:28
عرض = 6
# apl-source:29
ارتفاع_الشبكة = 6
# apl-source:30
جسم = [[2, 2], [2, 1], [2, 0]]
# apl-source:31
اتجاه = [0, 1]
# apl-source:32
طعام = [2, 4]
# apl-source:33

# apl-source:34
def خطوة(جسم, اتجاه, طعام):
  # apl-source:35
  رأس = جسم[0]
  # apl-source:36
  جديد = [رأس[0] + اتجاه[0], رأس[1] + اتجاه[1]]
  # apl-source:37
  if جديد[0] < 0 or جديد[0] >= ارتفاع_الشبكة or جديد[1] < 0 or جديد[1] >= عرض:
    # apl-source:38
    return "جدار"
  # apl-source:39
  if جديد in جسم and جديد != طعام:
    # apl-source:40
    return "ذات"
  # apl-source:41
  جسم.insert(0, جديد)
  # apl-source:42
  if جديد == طعام:
    # apl-source:43
    return "أكل"
  # apl-source:44
  جسم.pop()
  # apl-source:45
  return "تحرك"
# apl-source:46

# apl-source:47
تأكد_يساوي(خطوة(جسم, اتجاه, طعام), "تحرك", "خطوة عادية")
# apl-source:48
تأكد_يساوي(len(جسم), 3, "الطول ثابت دون أكل")
# apl-source:49
تأكد_يساوي(خطوة(جسم, اتجاه, طعام), "أكل", "أكل الطعام")
# apl-source:50
تأكد_يساوي(len(جسم), 4, "نمو بعد الأكل")
# apl-source:51
جسم2 = [[0, 0]]
# apl-source:52
تأكد_يساوي(خطوة(جسم2, [-1, 0], [5, 5]), "جدار", "اصطدام بالجدار")
# apl-source:53
print("طول الثعبان الآن:", len(جسم))
# apl-source:54
