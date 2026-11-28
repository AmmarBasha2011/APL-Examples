
# apl-source:1
# مثال 2009 — التحقق من مصفوفة جبلية
# apl-source:2
# Valid mountain array
# apl-source:3
# Demonstrates: قوائم
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2009-valid-mountain-array-check.apl
# apl-source:6

# apl-source:7
# # نصعد ما أمكن ثم ننزل ما أمكن
# apl-source:8
# # يجب أن نصل للنهاية وأن تكون القمة داخلية
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
def جبل(ق):
  # apl-source:19
  ن = len(ق)
  # apl-source:20
  if ن < 3:
    # apl-source:21
    return False
  # apl-source:22
  ك = 0
  # apl-source:23
  while ك + 1 < ن and ق[ك] < ق[ك + 1]:
    # apl-source:24
    ك = ك + 1
  # apl-source:25
  if ك == 0 or ك == ن - 1:
    # apl-source:26
    return False
  # apl-source:27
  while ك + 1 < ن and ق[ك] > ق[ك + 1]:
    # apl-source:28
    ك = ك + 1
  # apl-source:29
  return ك == ن - 1
# apl-source:30

# apl-source:31
تأكد_يساوي(جبل([0, 3, 2, 1]), True, "جبل")
# apl-source:32
تأكد_يساوي(جبل([3, 5, 5]), False, "قمة مسطحة")
# apl-source:33
تأكد_يساوي(جبل([2, 1]), False, "قصير")
# apl-source:34
تأكد_يساوي(جبل([0, 2, 3, 4, 5, 2, 1, 0]), True, "طويل")
# apl-source:35
