
# apl-source:1
# مثال 625 — ضرب كاراتسوبا
# apl-source:2
# Karatsuba multiplication
# apl-source:3
# Demonstrates: كاراتسوبا، فرق تسد، أعداد كبيرة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/625-karatsuba.apl
# apl-source:6

# apl-source:7
# Assertion style:
# apl-source:8
#   دالة تأكد_يساوي(فعلي, متوقع, اسم):
# apl-source:9
#     لو فعلي != متوقع:
# apl-source:10
#       اطبع "فشل:", اسم
# apl-source:11
#       اطبع "  متوقع:", متوقع
# apl-source:12
#       اطبع "  فعلي:", فعلي
# apl-source:13
#       قياسي_نظام_اخرج(1)
# apl-source:14
#     اطبع "ناجح:", اسم
# apl-source:15

# apl-source:16
def تأكد_يساوي(فعلي, متوقع, اسم):
  # apl-source:17
  if فعلي != متوقع:
    # apl-source:18
    print("فشل:", اسم)
    # apl-source:19
    print("  متوقع:", متوقع)
    # apl-source:20
    print("  فعلي:", فعلي)
    # apl-source:21
    قياسي_نظام_اخرج(1)
  # apl-source:22
  print("ناجح:", اسم)
# apl-source:23

# apl-source:24
# ضرب كاراتسوبا: ضرب الأعداد الكبيرة بتقسيم أسرع
# apl-source:25
# Demonstrates: فرق تسد, ثلاثة ضروب بدل أربعة, تقسيم عشري
# apl-source:26
# الضرب المدرسي O(n²) وهذه O(n^1.585)
# apl-source:27

# apl-source:28
def كاراتسوبا(س, ص):
  # apl-source:29
  if س < 10 or ص < 10:
    # apl-source:30
    return س * ص
  # apl-source:31
  ن = max(len(str(س)), len(str(ص)))
  # apl-source:32
  نصف = ن // 2
  # apl-source:33
  قوة = 10 ** نصف
  # apl-source:34
  أعلى1 = س // قوة
  # apl-source:35
  أدنى1 = س % قوة
  # apl-source:36
  أعلى2 = ص // قوة
  # apl-source:37
  أدنى2 = ص % قوة
  # apl-source:38
  ز0 = كاراتسوبا(أدنى1, أدنى2)
  # apl-source:39
  ز2 = كاراتسوبا(أعلى1, أعلى2)
  # apl-source:40
  ز1 = كاراتسوبا(أدنى1 + أعلى1, أدنى2 + أعلى2) - ز0 - ز2
  # apl-source:41
  return ز2 * (10 ** (2 * نصف)) + ز1 * قوة + ز0
# apl-source:42

# apl-source:43
تأكد_يساوي(كاراتسوبا(1234, 5678), 7006652, "ضرب رباعي")
# apl-source:44
تأكد_يساوي(كاراتسوبا(123456789, 987654321), 121932631112635269, "ضرب تساعي")
# apl-source:45
تأكد_يساوي(كاراتسوبا(7, 8), 56, "حالة أساس")
# apl-source:46
print("1234 × 5678 =", كاراتسوبا(1234, 5678))
# apl-source:47
