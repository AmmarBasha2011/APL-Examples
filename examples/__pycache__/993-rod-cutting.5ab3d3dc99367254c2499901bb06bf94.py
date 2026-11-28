
# apl-source:1
# مثال 993 — قطع القضيب
# apl-source:2
# Rod cutting
# apl-source:3
# Demonstrates: ديناميكية تصاعدية
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/993-rod-cutting.apl
# apl-source:6

# apl-source:7
# قطع القضيب: أقصى ثمن بتقطيع قضيب بطول ن لأجزاء بأسعار معطاة
# apl-source:8
# برمجة ديناميكية تصاعدية على كل طول أصغر
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
أسعار = [1, 5, 8, 9, 10, 17, 17, 20]
# apl-source:19

# apl-source:20
def أقصى_ثمن(ن):
  # apl-source:21
  جدول = [0]
  # apl-source:22
  for i in range(1, ن + 1):
    # apl-source:23
    أفضل = 0
    # apl-source:24
    for j in range(1, i + 1):
      # apl-source:25
      مرشح = جدول[i - j] + أسعار[j - 1]
      # apl-source:26
      if مرشح > أفضل:
        # apl-source:27
        أفضل = مرشح
    # apl-source:28
    جدول = جدول + [أفضل]
  # apl-source:29
  return جدول[ن]
# apl-source:30

# apl-source:31
تأكد_يساوي(أقصى_ثمن(4), 10, "طول أربعة")
# apl-source:32
تأكد_يساوي(أقصى_ثمن(8), 22, "طول ثمانية")
# apl-source:33
تأكد_يساوي(أقصى_ثمن(1), 1, "طول واحد")
# apl-source:34
