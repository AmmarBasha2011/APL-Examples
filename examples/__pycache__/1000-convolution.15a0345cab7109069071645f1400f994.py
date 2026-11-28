
# apl-source:1
# مثال 1000 — الالتفاف
# apl-source:2
# Convolution
# apl-source:3
# Demonstrates: انزلاق نواة على إشارة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1000-convolution.apl
# apl-source:6

# apl-source:7
# الالتفاف: تراكب إشارة مع نواة لإنتاج تأثير أو ترشيح
# apl-source:8
# كل عينة ناتجة مجموع حاصل ضرب الانزلاقات المتقاطعة
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
def التفاف(إشارة, نواة):
  # apl-source:19
  ن = (len(إشارة) + len(نواة)) - 1
  # apl-source:20
  ناتج = []
  # apl-source:21
  for _ in range(ن):
    # apl-source:22
    ناتج = ناتج + [0]
  # apl-source:23
  for i in range(len(إشارة)):
    # apl-source:24
    for j in range(len(نواة)):
      # apl-source:25
      ناتج[i + j] = ناتج[i + j] + (إشارة[i] * نواة[j])
  # apl-source:26
  return ناتج
# apl-source:27

# apl-source:28
ناتج = التفاف([1, 2, 3], [0, 1, 0.5])
# apl-source:29
تأكد_يساوي(len(ناتج), 5, "الطول المجمع")
# apl-source:30
تأكد_يساوي(round(ناتج[0], 4), 0, "العينة الأولى")
# apl-source:31
تأكد_يساوي(round(ناتج[1], 4), 1, "العينة الثانية")
# apl-source:32
تأكد_يساوي(round(ناتج[2], 4), 2.5, "العينة الثالثة")
# apl-source:33
تأكد_يساوي(round(ناتج[3], 4), 4, "العينة الرابعة")
# apl-source:34
تأكد_يساوي(round(ناتج[4], 4), 1.5, "العينة الأخيرة")
# apl-source:35
