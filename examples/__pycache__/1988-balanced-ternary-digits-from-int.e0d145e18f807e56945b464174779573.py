
# apl-source:1
# مثال 1988 — التمثيل الثلاثي المتوازن
# apl-source:2
# Balanced ternary
# apl-source:3
# Demonstrates: أنظمة العد
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1988-balanced-ternary-digits-from-int.apl
# apl-source:6

# apl-source:7
# # إذا كان الباقي 2 نكتب T ونزيد 1 قبل القسمة
# apl-source:8
# # ونعالج الأعداد السالبة بنفس الطريقة
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
def ثلاثي(ن):
  # apl-source:19
  if ن == 0:
    # apl-source:20
    return "0"
  # apl-source:21
  خرج = ""
  # apl-source:22
  while ن != 0:
    # apl-source:23
    ر = ن % 3
    # apl-source:24
    if ر == 0:
      # apl-source:25
      خرج = "0" + خرج
      # apl-source:26
      ن = ن // 3
    # apl-source:27
    elif ر == 1:
      # apl-source:28
      خرج = "1" + خرج
      # apl-source:29
      ن = (ن - 1) // 3
    # apl-source:30
    else:
      # apl-source:31
      خرج = "T" + خرج
      # apl-source:32
      ن = (ن + 1) // 3
  # apl-source:33
  return خرج
# apl-source:34

# apl-source:35
تأكد_يساوي(ثلاثي(0), "0", "صفر")
# apl-source:36
تأكد_يساوي(ثلاثي(5), "1TT", "٥")
# apl-source:37
تأكد_يساوي(ثلاثي(8), "10T", "٨")
# apl-source:38
تأكد_يساوي(ثلاثي(13), "111", "١٣")
# apl-source:39
تأكد_يساوي(ثلاثي(-1), "T", "سالب")
# apl-source:40
