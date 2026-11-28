
# apl-source:1
# مثال 1387 — مضروبات الأرقام
# apl-source:2
# Digit factorial numbers
# apl-source:3
# Demonstrates: رياضيات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1387-digit-factorials.apl
# apl-source:6

# apl-source:7
# 145 يساوي 1 زائد 24 زائد 120
# apl-source:8
# نحسب المضروبات مرة واحدة لكل رقم
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
def مضروبات_الأرقام():
  # apl-source:19
  م = [1]
  # apl-source:20
  for ع in range(1, 10):
    # apl-source:21
    م = م + [م[ع - 1] * ع]
  # apl-source:22
  return م
# apl-source:23

# apl-source:24
def مميز(ن):
  # apl-source:25
  م = مضروبات_الأرقام()
  # apl-source:26
  مجموع = 0
  # apl-source:27
  for ح in str(ن):
    # apl-source:28
    مجموع = مجموع + م[int(ح)]
  # apl-source:29
  return مجموع == ن
# apl-source:30

# apl-source:31
def ابحث(حد):
  # apl-source:32
  ناتج = []
  # apl-source:33
  for ن in range(10, حد):
    # apl-source:34
    if مميز(ن):
      # apl-source:35
      ناتج = ناتج + [ن]
  # apl-source:36
  return ناتج
# apl-source:37

# apl-source:38
تأكد_يساوي(مميز(145), True, "مئة وخمسة وأربعون")
# apl-source:39
تأكد_يساوي(مميز(40585), True, "أربعون ألفاً")
# apl-source:40
تأكد_يساوي(مميز(144), False, "ليس مميزاً")
# apl-source:41
تأكد_يساوي(ابحث(2000), [145], "أقل من ألفين")
# apl-source:42
