
# apl-source:1
# مثال 917 — ضرب السلاسل المصفوفية
# apl-source:2
# Matrix chain multiplication
# apl-source:3
# Demonstrates: تقويس ببرمجة ديناميكية
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/917-matrix-chain.apl
# apl-source:6

# apl-source:7
# ضرب السلاسل المصفوفية: أفضل ترتيب أقواس يقلل العمليات
# apl-source:8
# برمجة ديناميكية: م[i][j] أقل كلفة لضرب i..j
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
def أقل_كلفة(أبعاد):
  # apl-source:19
  ن = len(أبعاد) - 1
  # apl-source:20
  م = []
  # apl-source:21
  for _ in range(ن + 1):
    # apl-source:22
    صف = []
    # apl-source:23
    for __ in range(ن + 1):
      # apl-source:24
      صف = صف + [0]
    # apl-source:25
    م = م + [صف]
  # apl-source:26
  for طول_سلسلة in range(2, ن + 1):
    # apl-source:27
    for i in range(1, ن - طول_سلسلة + 2):
      # apl-source:28
      ج = i + طول_سلسلة - 1
      # apl-source:29
      م[i][ج] = 1000000000000
      # apl-source:30
      for k in range(i, ج):
        # apl-source:31
        كلفة = م[i][k] + م[k + 1][ج] + أبعاد[i - 1] * أبعاد[k] * أبعاد[ج]
        # apl-source:32
        if كلفة < م[i][ج]:
          # apl-source:33
          م[i][ج] = كلفة
  # apl-source:34
  return م[1][ن]
# apl-source:35

# apl-source:36
# أبعاد: 40x20, 20x30, 30x10, 10x30
# apl-source:37
ك = أقل_كلفة([40, 20, 30, 10, 30])
# apl-source:38
print("أقل كلفة:", ك)
# apl-source:39

# apl-source:40
تأكد_يساوي(ك, 26000, "المثال القياسي")
# apl-source:41
تأكد_يساوي(أقل_كلفة([10, 20, 30]), 6000, "مصفوفتان فقط")
# apl-source:42
تأكد_يساوي(أقل_كلفة([5, 10]), 0, "مصفوفة واحدة: لا ضرب")
# apl-source:43
# مثال يفيد فيه التقويس: (A(10x100) B(100x5)) C(5x50): 5000+2500=7500 مقابل 50000+25000
# apl-source:44
تأكد_يساوي(أقل_كلفة([10, 100, 5, 50]), 7500, "ترتيب الأقواس يهم")
# apl-source:45
