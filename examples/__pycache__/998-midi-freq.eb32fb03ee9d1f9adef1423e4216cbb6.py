
# apl-source:1
# مثال 998 — ترددات نوتات MIDI
# apl-source:2
# MIDI note frequency
# apl-source:3
# Demonstrates: سلم معتدل بأس ثنائي
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/998-midi-freq.apl
# apl-source:6

# apl-source:7
# نوتات MIDI إلى ترددات: السلم المعتدل باثنتي عشرة درجة نصفية
# apl-source:8
# كل نوتة تبعد عن لا المرجعية بأس ثنائي
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
def تردد(نوتة):
  # apl-source:19
  return 440 * (2 ** ((نوتة - 69) / 12))
# apl-source:20

# apl-source:21
تأكد_يساوي(round(تردد(69), 2), 440, "لا المرجعية")
# apl-source:22
تأكد_يساوي(round(تردد(60), 2), 261.63, "دو الوسطى")
# apl-source:23
تأكد_يساوي(round(تردد(81), 2), 880, "لا الأوكتاف الأعلى")
# apl-source:24
تأكد_يساوي(round(تردد(57), 2), 220, "لا الأوكتاف الأدنى")
# apl-source:25
