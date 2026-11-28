
# apl-source:1
# مثال 1034 — مصفوفة جبل
# apl-source:2
# Valid mountain array
# apl-source:3
# Demonstrates: صعود ثم هبوط
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1034-valid-mountain.apl
# apl-source:6

# apl-source:7
# الجبل يصعد بدقة إلى قمة ثم يهبط بدقة
# apl-source:8
# والقمة ليست في الطرفين
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
  ع = 0
  # apl-source:21
  while ((ع + 1) < ن) and (ق[ع] < ق[ع + 1]):
    # apl-source:22
    ع = ع + 1
  # apl-source:23
  if (ع == 0) or (ع == (ن - 1)):
    # apl-source:24
    return False
  # apl-source:25
  while ((ع + 1) < ن) and (ق[ع] > ق[ع + 1]):
    # apl-source:26
    ع = ع + 1
  # apl-source:27
  return ع == (ن - 1)
# apl-source:28

# apl-source:29
تأكد_يساوي(جبل([0, 3, 2, 1]), True, "جبل")
# apl-source:30
تأكد_يساوي(جبل([2, 1]), False, "قصيرة")
# apl-source:31
تأكد_يساوي(جبل([3, 5, 5]), False, "هضبة")
# apl-source:32
تأكد_يساوي(جبل([0, 2, 3, 3, 5, 2, 1, 0]), False, "قمتان")
# apl-source:33
