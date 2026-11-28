
# apl-source:1
# مثال 1093 — لغة الماعز
# apl-source:2
# Goat Latin
# apl-source:3
# Demonstrates: قواعد تحويل الكلمات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1093-goat-latin.apl
# apl-source:6

# apl-source:7
# الكلمة التي تبدأ بحرف علة تأخذ ma في آخرها
# apl-source:8
# وغيرها ينقل حرفها الأول للنهاية قبل ma، ثم يضاف a بعدد ترتيب الكلمة
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
def علة_أول(ح):
  # apl-source:19
  return ح in "aeiouAEIOU"
# apl-source:20

# apl-source:21
def ماعز(جملة):
  # apl-source:22
  كلمات = جملة.split(" ")
  # apl-source:23
  ناتج = []
  # apl-source:24
  for ع in range(len(كلمات)):
    # apl-source:25
    ك = كلمات[ع]
    # apl-source:26
    if علة_أول(ك[0]):
      # apl-source:27
      ب = ك + "ma"
    # apl-source:28
    else:
      # apl-source:29
      ب = ك[1:] + ك[0] + "ma"
    # apl-source:30
    ناتج = ناتج + [ب + ("a" * (ع + 1))]
  # apl-source:31
  return " ".join(ناتج)
# apl-source:32

# apl-source:33
تأكد_يساوي(ماعز("I speak Goat Latin"), "Imaa peaksmaaa oatGmaaaa atinLmaaaaa", "مثال")
# apl-source:34
تأكد_يساوي(ماعز("The quick brown fox"), "heTmaa uickqmaaa rownbmaaaa oxfmaaaaa", "ثاني")
# apl-source:35
تأكد_يساوي(ماعز("a"), "amaa", "كلمة واحدة")
# apl-source:36
