
# apl-source:1
# مثال 2355 — عدد الأعداد المتناظرة
# apl-source:2
# Count palindromic numbers
# apl-source:3
# Demonstrates: قوائم
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2355-list-count-palindromic-numbers.apl
# apl-source:6

# apl-source:7
# # نمرر القائمة
# apl-source:8
# # ونتحقق من الناتج
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
def ف(ق):
  # apl-source:19
  ع = 0
  # apl-source:20
  for ن in ق:
    # apl-source:21
    if str(ن) == str(ن)[::-1]:
      # apl-source:22
      ع = ع + 1
  # apl-source:23
  return ع
# apl-source:24

# apl-source:25
تأكد_يساوي(ف([121, 123, 5]), 2, "حالة 1")
# apl-source:26
تأكد_يساوي(ف([10, 20]), 0, "حالة 2")
# apl-source:27
تأكد_يساوي(ف([11, 22, 33]), 3, "حالة 3")
# apl-source:28
تأكد_يساوي(ف([1221, 1231]), 1, "حالة 4")
# apl-source:29
