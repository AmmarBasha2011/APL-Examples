
# apl-source:1
# مثال 1516 — صرف الفئات من الصراف
# apl-source:2
# ATM notes dispense
# apl-source:3
# Demonstrates: مالية
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1516-atm-notes-dispense.apl
# apl-source:6

# apl-source:7
# نبدأ بأكبر فئة
# apl-source:8
# المبلغ الذي لا يقبل القسمة على أصغر فئة مرفوض
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
def اصرف(مبلغ):
  # apl-source:19
  فئات = [200, 100, 50, 20, 10]
  # apl-source:20
  نتيجة = {}
  # apl-source:21
  for ف in فئات:
    # apl-source:22
    if مبلغ >= ف:
      # apl-source:23
      نتيجة[ف] = مبلغ // ف
      # apl-source:24
      مبلغ = مبلغ % ف
  # apl-source:25
  if مبلغ != 0:
    # apl-source:26
    return {}
  # apl-source:27
  return نتيجة
# apl-source:28

# apl-source:29
تأكد_يساوي(اصرف(380), {200: 1, 100: 1, 50: 1, 20: 1, 10: 1}, "كل الفئات")
# apl-source:30
تأكد_يساوي(اصرف(500), {200: 2, 100: 1}, "فئتان")
# apl-source:31
تأكد_يساوي(اصرف(35), {}, "مرفوض")
# apl-source:32
