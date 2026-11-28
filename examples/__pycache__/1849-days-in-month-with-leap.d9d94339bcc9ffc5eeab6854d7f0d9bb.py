
# apl-source:1
# مثال 1849 — أيام الشهر مع السنة الكبيسة
# apl-source:2
# Days in month considering leap year
# apl-source:3
# Demonstrates: وقت
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1849-days-in-month-with-leap.apl
# apl-source:6

# apl-source:7
# نعرف السنة الكبيسة أولاً
# apl-source:8
# نختار طول الشهر من جدول
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
def كبيسة(س):
  # apl-source:19
  if س % 400 == 0:
    # apl-source:20
    return True
  # apl-source:21
  if س % 100 == 0:
    # apl-source:22
    return False
  # apl-source:23
  return س % 4 == 0
# apl-source:24

# apl-source:25
def أيام_الشهر(س, ش):
  # apl-source:26
  أطوال = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  # apl-source:27
  if ش == 2 and كبيسة(س):
    # apl-source:28
    return 29
  # apl-source:29
  return أطوال[ش - 1]
# apl-source:30

# apl-source:31
تأكد_يساوي(أيام_الشهر(2024, 2), 29, "كبيسة")
# apl-source:32
تأكد_يساوي(أيام_الشهر(2023, 2), 28, "عادية")
# apl-source:33
تأكد_يساوي(أيام_الشهر(1900, 2), 28, "قرن")
# apl-source:34
تأكد_يساوي(أيام_الشهر(2000, 2), 29, "ألفية")
# apl-source:35
تأكد_يساوي(أيام_الشهر(2023, 4), 30, "أبريل")
# apl-source:36
