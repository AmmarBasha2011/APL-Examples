
# apl-source:1
# مثال 2099 — عدد تجزئات العدد الصحيح
# apl-source:2
# Integer partition count
# apl-source:3
# Demonstrates: برمجة ديناميكية
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2099-integer-partition-count-dp.apl
# apl-source:6

# apl-source:7
# # نضيف الأجزاء من 1 إلى ن تباعا
# apl-source:8
# # كل جزء يمكن تكراره
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
def تجزئات(ن):
  # apl-source:19
  ق = [1] + [0] * ن
  # apl-source:20
  for جزء in range(1, ن + 1):
    # apl-source:21
    for س in range(جزء, ن + 1):
      # apl-source:22
      ق[س] = ق[س] + ق[س - جزء]
  # apl-source:23
  return ق[ن]
# apl-source:24

# apl-source:25
تأكد_يساوي(تجزئات(0), 1, "٠")
# apl-source:26
تأكد_يساوي(تجزئات(5), 7, "٥")
# apl-source:27
تأكد_يساوي(تجزئات(10), 42, "١٠")
# apl-source:28
تأكد_يساوي(تجزئات(20), 627, "٢٠")
# apl-source:29
