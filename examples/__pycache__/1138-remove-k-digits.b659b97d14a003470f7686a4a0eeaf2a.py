
# apl-source:1
# مثال 1138 — حذف أرقام
# apl-source:2
# Remove k digits for smallest number
# apl-source:3
# Demonstrates: مكدس رتيب
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1138-remove-k-digits.apl
# apl-source:6

# apl-source:7
# نحذف الرقم السابق كلما كان أكبر من الحالي
# apl-source:8
# ثم نقص ما تبقى من النهاية
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
def اصغر_بعد_حذف(ع, ك):
  # apl-source:19
  مكدس = []
  # apl-source:20
  for ح in ع:
    # apl-source:21
    while (ك > 0) and (len(مكدس) > 0) and (مكدس[-1] > ح):
      # apl-source:22
      مكدس.pop()
      # apl-source:23
      ك = ك - 1
    # apl-source:24
    مكدس = مكدس + [ح]
  # apl-source:25
  if ك > 0:
    # apl-source:26
    مكدس = مكدس[:len(مكدس) - ك]
  # apl-source:27
  نتيجة = "".join(مكدس)
  # apl-source:28
  نتيجة = نتيجة.lstrip("0")
  # apl-source:29
  if نتيجة == "":
    # apl-source:30
    return "0"
  # apl-source:31
  return نتيجة
# apl-source:32

# apl-source:33
تأكد_يساوي(اصغر_بعد_حذف("1432219", 3), "1219", "مثال أول")
# apl-source:34
تأكد_يساوي(اصغر_بعد_حذف("10200", 1), "200", "أصفار بادئة")
# apl-source:35
تأكد_يساوي(اصغر_بعد_حذف("10", 2), "0", "حذف الكل")
# apl-source:36
تأكد_يساوي(اصغر_بعد_حذف("12345", 2), "123", "تصاعدي")
# apl-source:37
