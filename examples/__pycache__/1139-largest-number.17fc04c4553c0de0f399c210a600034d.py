
# apl-source:1
# مثال 1139 — أكبر عدد
# apl-source:2
# Largest number from list
# apl-source:3
# Demonstrates: مقارنة مخصصة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1139-largest-number.apl
# apl-source:6

# apl-source:7
# نقارن رقمين بلصقهما بالترتيبين
# apl-source:8
# ونرتب بحيث يسبق الأكبر ناتجاً
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
def اكبر_عدد(أ):
  # apl-source:19
  ن = [str(س) for س in أ]
  # apl-source:20
  for ع in range(len(ن)):
    # apl-source:21
    for ك in range(len(ن) - ع - 1):
      # apl-source:22
      if (ن[ك] + ن[ك + 1]) < (ن[ك + 1] + ن[ك]):
        # apl-source:23
        ت = ن[ك]
        # apl-source:24
        ن[ك] = ن[ك + 1]
        # apl-source:25
        ن[ك + 1] = ت
  # apl-source:26
  ناتج = "".join(ن)
  # apl-source:27
  if ناتج[0] == "0":
    # apl-source:28
    return "0"
  # apl-source:29
  return ناتج
# apl-source:30

# apl-source:31
تأكد_يساوي(اكبر_عدد([10, 2]), "210", "مثال أول")
# apl-source:32
تأكد_يساوي(اكبر_عدد([3, 30, 34, 5, 9]), "9534330", "مثال ثان")
# apl-source:33
تأكد_يساوي(اكبر_عدد([0, 0]), "0", "أصفار")
# apl-source:34
تأكد_يساوي(اكبر_عدد([121, 12]), "12121", "بادئة مشتركة")
# apl-source:35
