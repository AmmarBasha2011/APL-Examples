
# apl-source:1
# مثال 1044 — جمع ثنائي
# apl-source:2
# Add binary strings
# apl-source:3
# Demonstrates: حمل من اليمين
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1044-add-binary.apl
# apl-source:6

# apl-source:7
# نجمع الخانات من اليمين مع الحمل
# apl-source:8
# المجموع 0 أو 1 يبقى والحمل يمضي للخانة التالية
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
def اجمع_ثنائي(أ, ب):
  # apl-source:19
  ناتج = ""
  # apl-source:20
  ي = len(أ) - 1
  # apl-source:21
  ك = len(ب) - 1
  # apl-source:22
  حمل = 0
  # apl-source:23
  while (ي >= 0) or (ك >= 0) or (حمل > 0):
    # apl-source:24
    مج = حمل
    # apl-source:25
    if ي >= 0:
      # apl-source:26
      مج = مج + int(أ[ي])
      # apl-source:27
      ي = ي - 1
    # apl-source:28
    if ك >= 0:
      # apl-source:29
      مج = مج + int(ب[ك])
      # apl-source:30
      ك = ك - 1
    # apl-source:31
    ناتج = str(مج % 2) + ناتج
    # apl-source:32
    حمل = مج // 2
  # apl-source:33
  return ناتج
# apl-source:34

# apl-source:35
تأكد_يساوي(اجمع_ثنائي("11", "1"), "100", "حمل متسلسل")
# apl-source:36
تأكد_يساوي(اجمع_ثنائي("1010", "1011"), "10101", "أربع خانات")
# apl-source:37
تأكد_يساوي(اجمع_ثنائي("0", "0"), "0", "صفران")
# apl-source:38
