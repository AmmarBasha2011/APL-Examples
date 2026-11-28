
# apl-source:1
# مثال 2130 — أعداد أولام
# apl-source:2
# Ulam numbers
# apl-source:3
# Demonstrates: متتاليات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2130-ulam-numbers-first-terms.apl
# apl-source:6

# apl-source:7
# # نعد التمثيلات لكل مرشح
# apl-source:8
# # نقبل المرشح إذا كان العدد واحدا
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
def اولام(ن):
  # apl-source:19
  ق = [1, 2]
  # apl-source:20
  م = 2
  # apl-source:21
  while len(ق) < ن:
    # apl-source:22
    م = م + 1
    # apl-source:23
    عدد = 0
    # apl-source:24
    for ا in range(len(ق)):
      # apl-source:25
      for ب in range(ا + 1, len(ق)):
        # apl-source:26
        if ق[ا] + ق[ب] == م:
          # apl-source:27
          عدد = عدد + 1
    # apl-source:28
    if عدد == 1:
      # apl-source:29
      ق = ق + [م]
  # apl-source:30
  return ق[:ن]
# apl-source:31

# apl-source:32
تأكد_يساوي(اولام(10), [1, 2, 3, 4, 6, 8, 11, 13, 16, 18], "عشرة")
# apl-source:33
تأكد_يساوي(اولام(2), [1, 2], "اثنان")
# apl-source:34
