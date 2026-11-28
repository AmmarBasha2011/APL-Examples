
# apl-source:1
# مثال 1091 — التحويل للأحرف الصغيرة
# apl-source:2
# To lower case without built-ins
# apl-source:3
# Demonstrates: جدول الحروف
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1091-to-lower-manual.apl
# apl-source:6

# apl-source:7
# نبحث عن كل حرف في جدول الأحرف الكبيرة
# apl-source:8
# ونستبدله بنظيره من جدول الصغيرة
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
def صغير(نص_):
  # apl-source:19
  كبيرة_ = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  # apl-source:20
  صغيرة = "abcdefghijklmnopqrstuvwxyz"
  # apl-source:21
  ناتج = ""
  # apl-source:22
  for ح in نص_:
    # apl-source:23
    بدل = ح
    # apl-source:24
    for ع in range(26):
      # apl-source:25
      if كبيرة_[ع] == ح:
        # apl-source:26
        بدل = صغيرة[ع]
    # apl-source:27
    ناتج = ناتج + بدل
  # apl-source:28
  return ناتج
# apl-source:29

# apl-source:30
تأكد_يساوي(صغير("Hello"), "hello", "Hello")
# apl-source:31
تأكد_يساوي(صغير("LOVELY"), "lovely", "كلها كبيرة")
# apl-source:32
تأكد_يساوي(صغير("al&phaBET"), "al&phabet", "رموز")
# apl-source:33
تأكد_يساوي(صغير("مرحبا ABC"), "مرحبا abc", "عربي ولاتيني")
# apl-source:34
