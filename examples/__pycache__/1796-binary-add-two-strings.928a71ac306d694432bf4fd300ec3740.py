
# apl-source:1
# مثال 1796 — جمع عددين ثنائيين نصاً
# apl-source:2
# Add two binary strings
# apl-source:3
# Demonstrates: ترميز
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1796-binary-add-two-strings.apl
# apl-source:6

# apl-source:7
# نمر من آخر الرقم
# apl-source:8
# نحمل الواحد للتالي
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
  ي = len(أ) - 1
  # apl-source:20
  ك = len(ب) - 1
  # apl-source:21
  حمل = 0
  # apl-source:22
  ناتج = ""
  # apl-source:23
  while ي >= 0 or ك >= 0 or حمل > 0:
    # apl-source:24
    مجموع = حمل
    # apl-source:25
    if ي >= 0:
      # apl-source:26
      مجموع = مجموع + int(أ[ي])
      # apl-source:27
      ي = ي - 1
    # apl-source:28
    if ك >= 0:
      # apl-source:29
      مجموع = مجموع + int(ب[ك])
      # apl-source:30
      ك = ك - 1
    # apl-source:31
    ناتج = str(مجموع % 2) + ناتج
    # apl-source:32
    حمل = مجموع // 2
  # apl-source:33
  return ناتج
# apl-source:34

# apl-source:35
تأكد_يساوي(اجمع_ثنائي("11", "1"), "100", "حمل")
# apl-source:36
تأكد_يساوي(اجمع_ثنائي("1010", "1011"), "10101", "أربعة")
# apl-source:37
تأكد_يساوي(اجمع_ثنائي("0", "0"), "0", "صفر")
# apl-source:38
