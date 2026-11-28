
# apl-source:1
# مثال 1912 — مسألة يوسف بمحاكاة الطابور
# apl-source:2
# Josephus problem queue simulation
# apl-source:3
# Demonstrates: محاكاة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1912-josephus-queue-simulation.apl
# apl-source:6

# apl-source:7
# نمشي في الدائرة ونعد
# apl-source:8
# نحذف من وصل عده إلى ك
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
def يوسف(ن, ك):
  # apl-source:19
  ق = []
  # apl-source:20
  for ي in range(1, ن + 1):
    # apl-source:21
    ق = ق + [ي]
  # apl-source:22
  ف = 0
  # apl-source:23
  while len(ق) > 1:
    # apl-source:24
    ف = (ف + ك - 1) % len(ق)
    # apl-source:25
    ق.pop(ف)
  # apl-source:26
  return ق[0]
# apl-source:27

# apl-source:28
تأكد_يساوي(يوسف(7, 3), 4, "٧ و٣")
# apl-source:29
تأكد_يساوي(يوسف(5, 2), 3, "٥ و٢")
# apl-source:30
تأكد_يساوي(يوسف(1, 5), 1, "واحد")
# apl-source:31
