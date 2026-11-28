
# apl-source:1
# مثال 1918 — لعبة الحجارة بالطرح
# apl-source:2
# Subtract stones game DP
# apl-source:3
# Demonstrates: ألعاب
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1918-stone-game-subtract-dp.apl
# apl-source:6

# apl-source:7
# نأخذ ١ أو ٢ أو ٣ حجارة
# apl-source:8
# نبني الحالات من الصغير للكبير
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
def يربح(ن):
  # apl-source:19
  ر = [False]
  # apl-source:20
  for ك in range(1, ن + 1):
    # apl-source:21
    ربح = False
    # apl-source:22
    for خ in [1, 2, 3]:
      # apl-source:23
      if ك - خ >= 0 and ر[ك - خ] == False:
        # apl-source:24
        ربح = True
    # apl-source:25
    ر = ر + [ربح]
  # apl-source:26
  return ر[ن]
# apl-source:27

# apl-source:28
تأكد_يساوي(يربح(4), False, "٤ خسارة")
# apl-source:29
تأكد_يساوي(يربح(5), True, "٥ ربح")
# apl-source:30
تأكد_يساوي(يربح(8), False, "٨ خسارة")
# apl-source:31
تأكد_يساوي(يربح(7), True, "٧ ربح")
# apl-source:32
