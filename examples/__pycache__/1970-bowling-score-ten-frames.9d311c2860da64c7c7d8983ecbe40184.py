
# apl-source:1
# مثال 1970 — حساب نقاط البولينج
# apl-source:2
# Bowling score
# apl-source:3
# Demonstrates: ألعاب
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1970-bowling-score-ten-frames.apl
# apl-source:6

# apl-source:7
# # نمشي على الرميات إطارا بإطار
# apl-source:8
# # القاضية تأخذ رميتين بعدها والاحتياطية رمية واحدة
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
def نقاط(رميات):
  # apl-source:19
  مج = 0
  # apl-source:20
  م = 0
  # apl-source:21
  for إطار in range(10):
    # apl-source:22
    if رميات[م] == 10:
      # apl-source:23
      مج = مج + 10 + رميات[م + 1] + رميات[م + 2]
      # apl-source:24
      م = م + 1
    # apl-source:25
    else:
      # apl-source:26
      if رميات[م] + رميات[م + 1] == 10:
        # apl-source:27
        مج = مج + 10 + رميات[م + 2]
      # apl-source:28
      else:
        # apl-source:29
        مج = مج + رميات[م] + رميات[م + 1]
      # apl-source:30
      م = م + 2
  # apl-source:31
  return مج
# apl-source:32

# apl-source:33
تأكد_يساوي(نقاط([10] * 12), 300, "مثالية")
# apl-source:34
تأكد_يساوي(نقاط([9, 0] * 10), 90, "تسعات")
# apl-source:35
تأكد_يساوي(نقاط([5] * 21), 150, "احتياطيات")
# apl-source:36
تأكد_يساوي(نقاط([0] * 20), 0, "أصفار")
# apl-source:37
