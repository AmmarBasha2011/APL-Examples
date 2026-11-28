
# apl-source:1
# مثال 1908 — تحويل الأرقام الرومانية لعدد
# apl-source:2
# Parse Roman numeral to integer
# apl-source:3
# Demonstrates: تحويل
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1908-roman-numeral-to-integer-parse.apl
# apl-source:6

# apl-source:7
# نقرأ الرموز من اليسار
# apl-source:8
# نطرح الرمز إن جاء بعده أكبر
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
def قيمة(ح):
  # apl-source:19
  if ح == "I":
    # apl-source:20
    return 1
  # apl-source:21
  if ح == "V":
    # apl-source:22
    return 5
  # apl-source:23
  if ح == "X":
    # apl-source:24
    return 10
  # apl-source:25
  if ح == "L":
    # apl-source:26
    return 50
  # apl-source:27
  if ح == "C":
    # apl-source:28
    return 100
  # apl-source:29
  if ح == "D":
    # apl-source:30
    return 500
  # apl-source:31
  return 1000
# apl-source:32

# apl-source:33
def روماني(س):
  # apl-source:34
  كلي = 0
  # apl-source:35
  for ك in range(len(س)):
    # apl-source:36
    ق = قيمة(س[ك])
    # apl-source:37
    if ك + 1 < len(س) and قيمة(س[ك + 1]) > ق:
      # apl-source:38
      كلي = كلي - ق
    # apl-source:39
    else:
      # apl-source:40
      كلي = كلي + ق
  # apl-source:41
  return كلي
# apl-source:42

# apl-source:43
تأكد_يساوي(روماني("III"), 3, "ثلاثة")
# apl-source:44
تأكد_يساوي(روماني("IX"), 9, "تسعة")
# apl-source:45
تأكد_يساوي(روماني("MCMXCIV"), 1994, "١٩٩٤")
# apl-source:46
