
# apl-source:1
# مثال 1876 — مدى القائمة
# apl-source:2
# Range of a list
# apl-source:3
# Demonstrates: إحصاء
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1876-range-and-spread-of-list.apl
# apl-source:6

# apl-source:7
# نمر مرة واحدة
# apl-source:8
# نحتفظ بالحدين
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
def مدى(ق):
  # apl-source:19
  صغير = ق[0]
  # apl-source:20
  كبير = ق[0]
  # apl-source:21
  for ع in ق:
    # apl-source:22
    صغير = min(صغير, ع)
    # apl-source:23
    كبير = max(كبير, ع)
  # apl-source:24
  return كبير - صغير
# apl-source:25

# apl-source:26
تأكد_يساوي(مدى([3, 9, 1, 7]), 8, "مختلط")
# apl-source:27
تأكد_يساوي(مدى([5]), 0, "واحد")
# apl-source:28
تأكد_يساوي(مدى([-2, 2]), 4, "سالب")
# apl-source:29
