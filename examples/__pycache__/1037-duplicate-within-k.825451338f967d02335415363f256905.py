
# apl-source:1
# مثال 1037 — تكرار قريب
# apl-source:2
# Contains nearby duplicate
# apl-source:3
# Demonstrates: آخر فهرس
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1037-duplicate-within-k.apl
# apl-source:6

# apl-source:7
# نحفظ آخر فهرس رأيناه لكل قيمة
# apl-source:8
# لو كانت المسافة للظهور السابق لا تتجاوز ك فالتكرار قريب
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
def تكرار_قريب(ق, ك):
  # apl-source:19
  قيم = []
  # apl-source:20
  فهارس = []
  # apl-source:21
  for ع in range(len(ق)):
    # apl-source:22
    if ق[ع] in قيم:
      # apl-source:23
      ف = 0
      # apl-source:24
      while قيم[ف] != ق[ع]:
        # apl-source:25
        ف = ف + 1
      # apl-source:26
      if (ع - فهارس[ف]) <= ك:
        # apl-source:27
        return True
      # apl-source:28
      فهارس[ف] = ع
    # apl-source:29
    else:
      # apl-source:30
      قيم = قيم + [ق[ع]]
      # apl-source:31
      فهارس = فهارس + [ع]
  # apl-source:32
  return False
# apl-source:33

# apl-source:34
تأكد_يساوي(تكرار_قريب([1, 2, 3, 1], 3), True, "مسافة ثلاثة")
# apl-source:35
تأكد_يساوي(تكرار_قريب([1, 0, 1, 1], 1), True, "متجاوران")
# apl-source:36
تأكد_يساوي(تكرار_قريب([1, 2, 3, 1, 2, 3], 2), False, "بعيدة")
# apl-source:37
