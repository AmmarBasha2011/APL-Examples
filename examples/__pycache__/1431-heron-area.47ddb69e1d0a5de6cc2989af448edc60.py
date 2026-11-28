
# apl-source:1
# مثال 1431 — مساحة هيرون
# apl-source:2
# Triangle area by Heron formula
# apl-source:3
# Demonstrates: هندسة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1431-heron-area.apl
# apl-source:6

# apl-source:7
# نحسب نصف المحيط
# apl-source:8
# المساحة جذر حاصل ضرب نصف المحيط في فروقه
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
def مساحة_هيرون(أ, ب, ج):
  # apl-source:19
  ن = (أ + ب + ج) / 2
  # apl-source:20
  return (ن * (ن - أ) * (ن - ب) * (ن - ج)) ** 0.5
# apl-source:21

# apl-source:22
تأكد_يساوي(مساحة_هيرون(3, 4, 5), 6.0, "قائم")
# apl-source:23
تأكد_يساوي(مساحة_هيرون(5, 5, 6), 12.0, "متساوي الساقين")
# apl-source:24
تأكد_يساوي(مساحة_هيرون(13, 14, 15), 84.0, "ثلاثة عشر")
# apl-source:25
