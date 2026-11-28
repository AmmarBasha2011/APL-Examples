
# apl-source:1
# مثال 655 — خط بريسنهام
# apl-source:2
# Bresenham line
# apl-source:3
# Demonstrates: تنقيط، خطأ متراكم، شبكة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/655-bresenham-line.apl
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
# خط بريسنهام: تنقيط مستقيم على شبكة
# apl-source:25
# Demonstrates: خطأ متراكم, جميع الأرباع, بلا فاصلة عائمة
# apl-source:26
# رسم الخطوط كما تفعل الشاشات والطابعات القديمة
# apl-source:27

# apl-source:28
def abs(س):
  # apl-source:29
  if س < 0:
    # apl-source:30
    return 0 - س
  # apl-source:31
  return س
# apl-source:32

# apl-source:33
def خط(س1, ص1, س2, ص2):
  # apl-source:34
  نقاط = []
  # apl-source:35
  فرق_س = abs(س2 - س1)
  # apl-source:36
  فرق_ص = abs(ص2 - ص1)
  # apl-source:37
  خطوة_س = 1
  # apl-source:38
  if س1 > س2:
    # apl-source:39
    خطوة_س = -1
  # apl-source:40
  خطوة_ص = 1
  # apl-source:41
  if ص1 > ص2:
    # apl-source:42
    خطوة_ص = -1
  # apl-source:43
  خطأ_تراكمي = فرق_س - فرق_ص
  # apl-source:44
  while True:
    # apl-source:45
    نقاط.append([س1, ص1])
    # apl-source:46
    if س1 == س2 and ص1 == ص2:
      # apl-source:47
      return نقاط
    # apl-source:48
    مضاعف = 2 * خطأ_تراكمي
    # apl-source:49
    if مضاعف > 0 - فرق_ص:
      # apl-source:50
      خطأ_تراكمي = خطأ_تراكمي - فرق_ص
      # apl-source:51
      س1 = س1 + خطوة_س
    # apl-source:52
    if مضاعف < فرق_س:
      # apl-source:53
      خطأ_تراكمي = خطأ_تراكمي + فرق_س
      # apl-source:54
      ص1 = ص1 + خطوة_ص
# apl-source:55

# apl-source:56
ق = خط(0, 0, 5, 3)
# apl-source:57
تأكد_يساوي(len(ق), 6, "عدد النقاط")
# apl-source:58
تأكد_يساوي(ق[0], [0, 0], "البداية")
# apl-source:59
تأكد_يساوي(ق[5], [5, 3], "النهاية")
# apl-source:60
تأكد_يساوي(ق, [[0, 0], [1, 1], [2, 1], [3, 2], [4, 2], [5, 3]], "مسار دقيق")
# apl-source:61
عمودي = خط(2, 2, 2, 7)
# apl-source:62
تأكد_يساوي(len(عمودي), 6, "عمودي بطول 6")
# apl-source:63
تأكد_يساوي(عمودي[0], [2, 2], "بداية العمودي")
# apl-source:64
تأكد_يساوي(عمودي[5], [2, 7], "نهاية العمودي")
# apl-source:65
عكسي = خط(5, 3, 0, 0)
# apl-source:66
تأكد_يساوي(عكسي[0], [5, 3], "بداية المعكوس")
# apl-source:67
تأكد_يساوي(عكسي[5], [0, 0], "نهاية المعكوس")
# apl-source:68
print("نقاط:", ق)
# apl-source:69
