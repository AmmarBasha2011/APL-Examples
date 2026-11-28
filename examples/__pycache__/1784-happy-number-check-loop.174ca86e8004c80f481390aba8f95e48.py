
# apl-source:1
# مثال 1784 — العدد السعيد
# apl-source:2
# Happy number check
# apl-source:3
# Demonstrates: نظرية الأعداد
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1784-happy-number-check-loop.apl
# apl-source:6

# apl-source:7
# نكرر حتى نصل واحداً أو ندور
# apl-source:8
# نخزن ما رأيناه
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
def مربعات(ن):
  # apl-source:19
  مجموع = 0
  # apl-source:20
  while ن > 0:
    # apl-source:21
    ر = ن % 10
    # apl-source:22
    مجموع = مجموع + ر * ر
    # apl-source:23
    ن = ن // 10
  # apl-source:24
  return مجموع
# apl-source:25

# apl-source:26
def سعيد(ن):
  # apl-source:27
  رأينا = {}
  # apl-source:28
  while ن != 1 and (str(ن) in رأينا) == False:
    # apl-source:29
    رأينا[str(ن)] = 1
    # apl-source:30
    ن = مربعات(ن)
  # apl-source:31
  return ن == 1
# apl-source:32

# apl-source:33
تأكد_يساوي(سعيد(19), True, "تسعة عشر")
# apl-source:34
تأكد_يساوي(سعيد(2), False, "اثنان")
# apl-source:35
تأكد_يساوي(سعيد(7), True, "سبعة")
# apl-source:36
تأكد_يساوي(سعيد(1), True, "واحد")
# apl-source:37
