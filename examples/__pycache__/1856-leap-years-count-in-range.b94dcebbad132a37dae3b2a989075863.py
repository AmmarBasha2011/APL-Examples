
# apl-source:1
# مثال 1856 — عدد السنوات الكبيسة في مدى
# apl-source:2
# Count leap years in range
# apl-source:3
# Demonstrates: وقت
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1856-leap-years-count-in-range.apl
# apl-source:6

# apl-source:7
# القاعدة الغريغورية
# apl-source:8
# نعد داخل المدى المغلق
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
def عد_الكبيسة(أ, ب):
  # apl-source:26
  عد = 0
  # apl-source:27
  for س in range(أ, ب + 1):
    # apl-source:28
    if كبيسة(س):
      # apl-source:29
      عد = عد + 1
  # apl-source:30
  return عد
# apl-source:31

# apl-source:32
تأكد_يساوي(عد_الكبيسة(2000, 2004), 2, "2000 و2004")
# apl-source:33
تأكد_يساوي(عد_الكبيسة(1900, 1900), 0, "1900")
# apl-source:34
تأكد_يساوي(عد_الكبيسة(1996, 2024), 8, "ثمان وعشرون سنة")
# apl-source:35
