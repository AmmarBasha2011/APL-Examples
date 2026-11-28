
# apl-source:1
# مثال 2023 — الكسر المستمر لعدد نسبي
# apl-source:2
# Continued fraction of rational
# apl-source:3
# Demonstrates: رياضيات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2023-continued-fraction-of-rational-number.apl
# apl-source:6

# apl-source:7
# # كل خطوة نسجل الخارج
# apl-source:8
# # ثم نقلب الكسر
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
def مستمر(ب, م):
  # apl-source:19
  خرج = []
  # apl-source:20
  while م != 0:
    # apl-source:21
    خرج = خرج + [ب // م]
    # apl-source:22
    ت = م
    # apl-source:23
    م = ب % م
    # apl-source:24
    ب = ت
  # apl-source:25
  return خرج
# apl-source:26

# apl-source:27
تأكد_يساوي(مستمر(415, 93), [4, 2, 6, 7], "٤١٥ على ٩٣")
# apl-source:28
تأكد_يساوي(مستمر(3, 7), [0, 2, 3], "٣ على ٧")
# apl-source:29
تأكد_يساوي(مستمر(5, 1), [5], "صحيح")
# apl-source:30
