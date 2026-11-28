
# apl-source:1
# مثال 996 — ضرب الأعداد الضخمة
# apl-source:2
# Big integer multiplication
# apl-source:3
# Demonstrates: أرقام بمصفوفة وحمل
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/996-bigint-multiply.apl
# apl-source:6

# apl-source:7
# ضرب الأعداد الضخمة: أرقام بأطوال تتجاوز نطاق الصحيح المدمج
# apl-source:8
# خوارزمية المدرسة على مصفوفتي أرقام مع الحمل
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
def أرقام(سلسلة):
  # apl-source:19
  ناتج = []
  # apl-source:20
  for i in range(len(سلسلة) - 1, -1, -1):
    # apl-source:21
    ناتج = ناتج + [int(سلسلة[i])]
  # apl-source:22
  return ناتج
# apl-source:23

# apl-source:24
def اضرب(سلسلة1, سلسلة2):
  # apl-source:25
  أ = أرقام(سلسلة1)
  # apl-source:26
  ب = أرقام(سلسلة2)
  # apl-source:27
  ناتج = []
  # apl-source:28
  for _ in range(len(أ) + len(ب)):
    # apl-source:29
    ناتج = ناتج + [0]
  # apl-source:30
  for i in range(len(أ)):
    # apl-source:31
    حمل = 0
    # apl-source:32
    for j in range(len(ب)):
      # apl-source:33
      مجموع = (ناتج[i + j] + (أ[i] * ب[j])) + حمل
      # apl-source:34
      ناتج[i + j] = مجموع % 10
      # apl-source:35
      حمل = مجموع // 10
    # apl-source:36
    ناتج[i + len(ب)] = ناتج[i + len(ب)] + حمل
  # apl-source:37
  أعلى = len(ناتج) - 1
  # apl-source:38
  while (أعلى > 0) and (ناتج[أعلى] == 0):
    # apl-source:39
    أعلى = أعلى - 1
  # apl-source:40
  سلسلة = ""
  # apl-source:41
  for i in range(أعلى, -1, -1):
    # apl-source:42
    سلسلة = سلسلة + str(ناتج[i])
  # apl-source:43
  return سلسلة
# apl-source:44

# apl-source:45
تأكد_يساوي(اضرب("123456789", "987654321"), "121932631112635269", "ضرب كبير")
# apl-source:46
تأكد_يساوي(اضرب("999", "999"), "998001", "مربع كبير")
# apl-source:47
تأكد_يساوي(اضرب("12", "3"), "36", "حالة صغيرة")
# apl-source:48
