
# apl-source:1
# مثال 1823 — جمع كسرين بأبسط صورة
# apl-source:2
# Add two fractions in lowest terms
# apl-source:3
# Demonstrates: حساب
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1823-fraction-add-lowest-terms.apl
# apl-source:6

# apl-source:7
# القاسم المشترك يختصر الناتج
# apl-source:8
# نعيد البسط والمقام
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
def قاسم(أ, ب):
  # apl-source:19
  while ب != 0:
    # apl-source:20
    ت = ب
    # apl-source:21
    ب = أ % ب
    # apl-source:22
    أ = ت
  # apl-source:23
  return أ
# apl-source:24

# apl-source:25
def اجمع_كسرين(أ, ب):
  # apl-source:26
  بسط = أ[0] * ب[1] + ب[0] * أ[1]
  # apl-source:27
  مقام = أ[1] * ب[1]
  # apl-source:28
  ق = قاسم(بسط, مقام)
  # apl-source:29
  return [بسط // ق, مقام // ق]
# apl-source:30

# apl-source:31
تأكد_يساوي(اجمع_كسرين([1, 2], [1, 3]), [5, 6], "نصف وثلث")
# apl-source:32
تأكد_يساوي(اجمع_كسرين([1, 4], [1, 4]), [1, 2], "ربعان")
# apl-source:33
تأكد_يساوي(اجمع_كسرين([2, 3], [1, 3]), [1, 1], "واحد")
# apl-source:34
