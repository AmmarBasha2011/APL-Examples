
# apl-source:1
# مثال 1225 — أكبر xor
# apl-source:2
# Maximum XOR of two numbers
# apl-source:3
# Demonstrates: عمليات بتات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1225-max-xor-pair.apl
# apl-source:6

# apl-source:7
# نبني الجواب بتاً بتاً من الأعلى
# apl-source:8
# ونتحقق بوجود زوج بنفس البادئات
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
def اكبر_xor(أ):
  # apl-source:19
  ناتج = 0
  # apl-source:20
  قناع = 0
  # apl-source:21
  for ب in range(31, -1, -1):
    # apl-source:22
    قناع = قناع | (1 << ب)
    # apl-source:23
    بوادئ = []
    # apl-source:24
    for س in أ:
      # apl-source:25
      بوادئ = بوادئ + [س & قناع]
    # apl-source:26
    تجربة = ناتج | (1 << ب)
    # apl-source:27
    وجد = False
    # apl-source:28
    for ز in بوادئ:
      # apl-source:29
      if (تجربة ^ ز) in بوادئ:
        # apl-source:30
        وجد = True
    # apl-source:31
    if وجد:
      # apl-source:32
      ناتج = تجربة
  # apl-source:33
  return ناتج
# apl-source:34

# apl-source:35
تأكد_يساوي(اكبر_xor([3,10,5,25,2,8]), 28, "مثال أول")
# apl-source:36
تأكد_يساوي(اكبر_xor([14,70,53,83,49,91,36,80,92,51,66,70]), 127, "مثال ثان")
# apl-source:37
تأكد_يساوي(اكبر_xor([0]), 0, "عنصر")
# apl-source:38
