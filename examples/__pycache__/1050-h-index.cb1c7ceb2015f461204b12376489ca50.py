
# apl-source:1
# مثال 1050 — مؤشر هـ
# apl-source:2
# H-index
# apl-source:3
# Demonstrates: ترتيب تنازلي
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1050-h-index.apl
# apl-source:6

# apl-source:7
# نرتب الاستشهادات تنازلياً
# apl-source:8
# ه هو أكبر ترتيب عدد الاستشهاد عنده لا يقل عن ترتيبه
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
def مؤشر_ه(استشهادات):
  # apl-source:19
  ق = list(استشهادات)
  # apl-source:20
  ق.sort()
  # apl-source:21
  ق.reverse()
  # apl-source:22
  ه = 0
  # apl-source:23
  for ع in range(len(ق)):
    # apl-source:24
    if ق[ع] >= (ع + 1):
      # apl-source:25
      ه = ع + 1
  # apl-source:26
  return ه
# apl-source:27

# apl-source:28
تأكد_يساوي(مؤشر_ه([3, 0, 6, 1, 5]), 3, "ثلاثة")
# apl-source:29
تأكد_يساوي(مؤشر_ه([1, 3, 1]), 1, "واحد")
# apl-source:30
تأكد_يساوي(مؤشر_ه([0, 0]), 0, "صفر")
# apl-source:31
تأكد_يساوي(مؤشر_ه([10, 10, 10, 10]), 4, "أربعة")
# apl-source:32
