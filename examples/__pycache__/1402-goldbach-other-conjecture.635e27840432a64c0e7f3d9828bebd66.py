
# apl-source:1
# مثال 1402 — تخمين غولدباخ الآخر
# apl-source:2
# Goldbach's other conjecture
# apl-source:3
# Demonstrates: رياضيات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1402-goldbach-other-conjecture.apl
# apl-source:6

# apl-source:7
# نجرب كل مربع ممكن لكل عدد فردي مركب
# apl-source:8
# ونبحث عن أول عدد يفشل
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
def اولي(ن):
  # apl-source:19
  if ن < 2:
    # apl-source:20
    return False
  # apl-source:21
  ع = 2
  # apl-source:22
  while ع * ع <= ن:
    # apl-source:23
    if ن % ع == 0:
      # apl-source:24
      return False
    # apl-source:25
    ع = ع + 1
  # apl-source:26
  return True
# apl-source:27

# apl-source:28
def يمكن_كتابته(ن):
  # apl-source:29
  ك = 1
  # apl-source:30
  while 2 * ك * ك < ن:
    # apl-source:31
    if اولي(ن - 2 * ك * ك):
      # apl-source:32
      return True
    # apl-source:33
    ك = ك + 1
  # apl-source:34
  return False
# apl-source:35

# apl-source:36
def اول_مخالف():
  # apl-source:37
  ن = 9
  # apl-source:38
  while True:
    # apl-source:39
    if (not اولي(ن)) and (not يمكن_كتابته(ن)):
      # apl-source:40
      return ن
    # apl-source:41
    ن = ن + 2
# apl-source:42

# apl-source:43
تأكد_يساوي(يمكن_كتابته(9), True, "تسعة")
# apl-source:44
تأكد_يساوي(يمكن_كتابته(15), True, "خمسة عشر")
# apl-source:45
تأكد_يساوي(اول_مخالف(), 5777, "المخالف الأول")
# apl-source:46
