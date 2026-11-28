
# apl-source:1
# مثال 651 — حيل البتات
# apl-source:2
# Bit tricks
# apl-source:3
# Demonstrates: بتات، إزاحات، XOR
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/651-bit-tricks.apl
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
# حيل البتات الشائعة
# apl-source:25
# Demonstrates: س & -س, س & (س-1), إزاحات, مقايضة XOR
# apl-source:26
# عمليات البتات أسرع من القسمة والباقي
# apl-source:27

# apl-source:28
def عد_البتات(س):
  # apl-source:29
  عدد = 0
  # apl-source:30
  while س > 0:
    # apl-source:31
    عدد = عدد + س % 2
    # apl-source:32
    س = س // 2
  # apl-source:33
  return عدد
# apl-source:34

# apl-source:35
def أدنى_بت(س):
  # apl-source:36
  return س & (0 - س)
# apl-source:37

# apl-source:38
def قوة_اثنين(س):
  # apl-source:39
  return س > 0 and (س & (س - 1)) == 0
# apl-source:40

# apl-source:41
تأكد_يساوي(عد_البتات(182), 5, "عد البتات المضيئة")
# apl-source:42
تأكد_يساوي(أدنى_بت(40), 8, "أدنى بت مضيء")
# apl-source:43
تأكد_يساوي(قوة_اثنين(16), True, "16 قوة اثنين")
# apl-source:44
تأكد_يساوي(قوة_اثنين(18), False, "18 ليست قوة اثنين")
# apl-source:45
تأكد_يساوي(40 & 39, 32, "إطفاء أدنى بت")
# apl-source:46
تأكد_يساوي(1 << 10, 1024, "إزاحة يسار")
# apl-source:47
تأكد_يساوي(1024 >> 3, 128, "إزاحة يمين")
# apl-source:48
س = 7
# apl-source:49
ص = 9
# apl-source:50
س = س ^ ص
# apl-source:51
ص = س ^ ص
# apl-source:52
س = س ^ ص
# apl-source:53
تأكد_يساوي([س, ص], [9, 7], "مقايضة بلا متغير ثالث")
# apl-source:54
print("انتهت الحيل")
# apl-source:55
