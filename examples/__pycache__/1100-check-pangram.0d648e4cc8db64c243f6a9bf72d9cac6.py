
# apl-source:1
# مثال 1100 — الجملة الشاملة
# apl-source:2
# Check if a sentence is a pangram
# apl-source:3
# Demonstrates: جرد الحروف
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1100-check-pangram.apl
# apl-source:6

# apl-source:7
# نمر على حروف الأبجدية اللاتينية
# apl-source:8
# ونتحقق أن كل حرف يظهر في الجملة
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
def شاملة(جملة):
  # apl-source:19
  for ح in "abcdefghijklmnopqrstuvwxyz":
    # apl-source:20
    if ح not in جملة:
      # apl-source:21
      return False
  # apl-source:22
  return True
# apl-source:23

# apl-source:24
تأكد_يساوي(شاملة("thequickbrownfoxjumpsoverthelazydog"), True, "الجملة الشهيرة")
# apl-source:25
تأكد_يساوي(شاملة("leetcode"), False, "ناقصة")
# apl-source:26
تأكد_يساوي(شاملة(""), False, "فارغة")
# apl-source:27
