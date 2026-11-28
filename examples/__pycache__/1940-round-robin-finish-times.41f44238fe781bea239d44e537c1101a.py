
# apl-source:1
# مثال 1940 — أزمنة انتهاء الدور الدائري
# apl-source:2
# Round robin scheduler finish times
# apl-source:3
# Demonstrates: جدولة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1940-round-robin-finish-times.apl
# apl-source:6

# apl-source:7
# نأخذ العملية الأولى من الطابور
# apl-source:8
# إن بقي لها عمل تعود للآخر
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
def دوري(ازمنة, حصة):
  # apl-source:19
  باقي = ازمنة + []
  # apl-source:20
  طابور = []
  # apl-source:21
  نهاية = []
  # apl-source:22
  for ك in range(len(ازمنة)):
    # apl-source:23
    طابور = طابور + [ك]
    # apl-source:24
    نهاية = نهاية + [0]
  # apl-source:25
  ساعة = 0
  # apl-source:26
  while len(طابور) > 0:
    # apl-source:27
    ك = طابور.pop(0)
    # apl-source:28
    خذ = min(حصة, باقي[ك])
    # apl-source:29
    ساعة = ساعة + خذ
    # apl-source:30
    باقي[ك] = باقي[ك] - خذ
    # apl-source:31
    if باقي[ك] > 0:
      # apl-source:32
      طابور = طابور + [ك]
    # apl-source:33
    else:
      # apl-source:34
      نهاية[ك] = ساعة
  # apl-source:35
  return نهاية
# apl-source:36

# apl-source:37
تأكد_يساوي(دوري([5, 3, 2], 2), [10, 9, 6], "ثلاث عمليات")
# apl-source:38
تأكد_يساوي(دوري([4], 3), [4], "عملية واحدة")
# apl-source:39
