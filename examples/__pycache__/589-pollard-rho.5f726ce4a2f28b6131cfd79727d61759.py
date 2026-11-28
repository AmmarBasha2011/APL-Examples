
# apl-source:1
# مثال 589 — تحليل بولارد-رو
# apl-source:2
# Pollard rho factorization
# apl-source:3
# Demonstrates: عوامل أولية، بولارد-رو، دورات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/589-pollard-rho.apl
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
# تحليل بولارد-رو إلى عوامل أولية
# apl-source:25
# Demonstrates: خوارزمية احتمالية ببذرة ثابتة, قاسم_مشترك, كشف دورات
# apl-source:26
# مثال كلاسيكي: تحليل 8051 = 83 × 97
# apl-source:27

# apl-source:28
def قاسم_مشترك(أ, ب):
  # apl-source:29
  while ب != 0:
    # apl-source:30
    مؤقت = ب
    # apl-source:31
    ب = أ % ب
    # apl-source:32
    أ = مؤقت
  # apl-source:33
  return أ
# apl-source:34

# apl-source:35
def بولارد(ن):
  # apl-source:36
  if ن % 2 == 0:
    # apl-source:37
    return 2
  # apl-source:38
  س = 2
  # apl-source:39
  ص = 2
  # apl-source:40
  ق = 1
  # apl-source:41
  while ق == 1:
    # apl-source:42
    س = (س * س + 1) % ن
    # apl-source:43
    ص = (ص * ص + 1) % ن
    # apl-source:44
    ص = (ص * ص + 1) % ن
    # apl-source:45
    ق = قاسم_مشترك(max(س - ص, ص - س), ن)
  # apl-source:46
  return ق
# apl-source:47

# apl-source:48
ع = بولارد(8051)
# apl-source:49
مكمل = 8051 // ع
# apl-source:50
print("عامل:", ع, " والمكمل:", مكمل)
# apl-source:51
تأكد_يساوي(min(ع, مكمل), 83, "العامل الأصغر")
# apl-source:52
تأكد_يساوي(max(ع, مكمل), 97, "العامل الأكبر")
# apl-source:53
تأكد_يساوي(ع * مكمل, 8051, "التحقق من الناتج")
# apl-source:54
