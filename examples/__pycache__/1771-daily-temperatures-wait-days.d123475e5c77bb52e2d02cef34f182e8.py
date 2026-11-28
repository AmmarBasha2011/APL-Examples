
# apl-source:1
# مثال 1771 — أيام الانتظار لدرجة أدفأ
# apl-source:2
# Days until a warmer temperature
# apl-source:3
# Demonstrates: مكدسات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1771-daily-temperatures-wait-days.apl
# apl-source:6

# apl-source:7
# مكدس من المواضع
# apl-source:8
# عند ارتفاع نحسب الفرق
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
def انتظار(د):
  # apl-source:19
  ناتج = []
  # apl-source:20
  for ع in د:
    # apl-source:21
    ناتج.append(0)
  # apl-source:22
  مكدس = []
  # apl-source:23
  for ك in range(len(د)):
    # apl-source:24
    while len(مكدس) > 0 and د[مكدس[len(مكدس) - 1]] < د[ك]:
      # apl-source:25
      ي = مكدس.pop()
      # apl-source:26
      ناتج[ي] = ك - ي
    # apl-source:27
    مكدس.append(ك)
  # apl-source:28
  return ناتج
# apl-source:29

# apl-source:30
تأكد_يساوي(انتظار([73, 74, 75, 71, 69, 72, 76, 73]), [1, 1, 4, 2, 1, 1, 0, 0], "كلاسيكي")
# apl-source:31
تأكد_يساوي(انتظار([30, 20, 10]), [0, 0, 0], "هابطة")
# apl-source:32
