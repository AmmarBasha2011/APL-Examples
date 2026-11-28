
# apl-source:1
# مثال 1654 — معاملات إقليدس الموسعة
# apl-source:2
# Extended Euclid coefficients
# apl-source:3
# Demonstrates: نظرية الأعداد
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1654-extended-euclid-coefficients.apl
# apl-source:6

# apl-source:7
# نكرر خطوات القسمة
# apl-source:8
# نحدث المعاملين مع كل خطوة
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
def إقليدس_موسع(أ, ب):
  # apl-source:19
  س0 = 1
  # apl-source:20
  س1 = 0
  # apl-source:21
  ص0 = 0
  # apl-source:22
  ص1 = 1
  # apl-source:23
  while ب != 0:
    # apl-source:24
    ق = أ // ب
    # apl-source:25
    ت = أ % ب
    # apl-source:26
    أ = ب
    # apl-source:27
    ب = ت
    # apl-source:28
    ت_س = س0 - ق * س1
    # apl-source:29
    س0 = س1
    # apl-source:30
    س1 = ت_س
    # apl-source:31
    ت_ص = ص0 - ق * ص1
    # apl-source:32
    ص0 = ص1
    # apl-source:33
    ص1 = ت_ص
  # apl-source:34
  return [أ, س0, ص0]
# apl-source:35

# apl-source:36
ن = إقليدس_موسع(30, 18)
# apl-source:37
تأكد_يساوي(ن[0], 6, "القاسم")
# apl-source:38
تأكد_يساوي(30 * ن[1] + 18 * ن[2], 6, "المتطابقة")
# apl-source:39
م = إقليدس_موسع(17, 5)
# apl-source:40
تأكد_يساوي(17 * م[1] + 5 * م[2], 1, "أوليان")
# apl-source:41
