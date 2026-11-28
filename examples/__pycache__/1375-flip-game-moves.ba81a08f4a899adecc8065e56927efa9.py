
# apl-source:1
# مثال 1375 — حركات لعبة القلب
# apl-source:2
# Flip game next states
# apl-source:3
# Demonstrates: نصوص
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1375-flip-game-moves.apl
# apl-source:6

# apl-source:7
# القلب يحول ++ إلى --
# apl-source:8
# نمر على النص ونبني حالة جديدة لكل موضع
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
def حالات_تالية(حالة):
  # apl-source:19
  ناتج = []
  # apl-source:20
  for ع in range(len(حالة) - 1):
    # apl-source:21
    if (حالة[ع] == "+") and (حالة[ع + 1] == "+"):
      # apl-source:22
      ناتج = ناتج + [حالة[:ع] + "--" + حالة[ع + 2:]]
  # apl-source:23
  return ناتج
# apl-source:24

# apl-source:25
تأكد_يساوي(حالات_تالية("++++"), ["--++","+--+","++--"], "ثلاث حالات")
# apl-source:26
تأكد_يساوي(حالات_تالية("+"), [], "علامة")
# apl-source:27
تأكد_يساوي(حالات_تالية("+-++"), ["+---"], "حالة واحدة")
# apl-source:28
