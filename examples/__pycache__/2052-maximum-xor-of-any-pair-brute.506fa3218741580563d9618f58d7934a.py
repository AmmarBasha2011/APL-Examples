
# apl-source:1
# مثال 2052 — أكبر XOR بين أي زوجين
# apl-source:2
# Maximum pair XOR brute force
# apl-source:3
# Demonstrates: بتات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2052-maximum-xor-of-any-pair-brute.apl
# apl-source:6

# apl-source:7
# # حل مباشر مناسب للقوائم الصغيرة
# apl-source:8
# # يصلح أساسا للمقارنة مع حل المصفوفة الثنائية
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
def اكبر_xor(ق):
  # apl-source:19
  افضل = 0
  # apl-source:20
  for ا in range(len(ق)):
    # apl-source:21
    for ب in range(ا + 1, len(ق)):
      # apl-source:22
      افضل = max(افضل, ق[ا] ^ ق[ب])
  # apl-source:23
  return افضل
# apl-source:24

# apl-source:25
تأكد_يساوي(اكبر_xor([3, 10, 5, 25, 2, 8]), 28, "كلاسيكي")
# apl-source:26
تأكد_يساوي(اكبر_xor([0]), 0, "واحد")
# apl-source:27
تأكد_يساوي(اكبر_xor([14, 70, 53, 83, 49, 91, 36, 80, 92, 51, 66, 70]), 127, "اثنا عشر")
# apl-source:28
