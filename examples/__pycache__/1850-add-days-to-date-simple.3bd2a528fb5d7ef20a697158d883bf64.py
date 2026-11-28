
# apl-source:1
# مثال 1850 — إضافة أيام إلى تاريخ
# apl-source:2
# Add days to a date
# apl-source:3
# Demonstrates: وقت
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1850-add-days-to-date-simple.apl
# apl-source:6

# apl-source:7
# نزيد اليوم وننتقل للشهر التالي عند تجاوز طوله
# apl-source:8
# نعالج نهاية السنة
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
def أضف_أياماً(س, ش, ي, ن):
  # apl-source:32
  for ك in range(ن):
    # apl-source:33
    ي = ي + 1
    # apl-source:34
    if ي > أيام_الشهر(س, ش):
      # apl-source:35
      ي = 1
      # apl-source:36
      ش = ش + 1
      # apl-source:37
      if ش > 12:
        # apl-source:38
        ش = 1
        # apl-source:39
        س = س + 1
  # apl-source:40
  return [س, ش, ي]
# apl-source:41

# apl-source:42
تأكد_يساوي(أضف_أياماً(2023, 12, 30, 5), [2024, 1, 4], "نهاية السنة")
# apl-source:43
تأكد_يساوي(أضف_أياماً(2024, 2, 28, 2), [2024, 3, 1], "كبيسة")
# apl-source:44
تأكد_يساوي(أضف_أياماً(2023, 1, 1, 0), [2023, 1, 1], "صفر")
# apl-source:45
