
# apl-source:1
# مثال 876 — مفارقة الميلاد
# apl-source:2
# Birthday paradox
# apl-source:3
# Demonstrates: احتمال تفرد تراكمي
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/876-birthday-paradox.apl
# apl-source:6

# apl-source:7
# مفارقة الميلاد: 23 شخصاً تكفي لاحتمال 50% لميلاد مشترك
# apl-source:8
# الاحتمال التراكمي للتفرد يهبط بسرعة مفاجئة
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
def احتمال_تطابق(ن):
  # apl-source:19
  تفرد = 1.0
  # apl-source:20
  for ك in range(ن):
    # apl-source:21
    تفرد = تفرد * (365.0 - ك) / 365.0
  # apl-source:22
  return 1.0 - تفرد
# apl-source:23

# apl-source:24
print("P(10) =", احتمال_تطابق(10))
# apl-source:25
print("P(23) =", احتمال_تطابق(23))
# apl-source:26
print("P(50) =", احتمال_تطابق(50))
# apl-source:27

# apl-source:28
# أصغر ن يتجاوز 50%
# apl-source:29
ن = 1
# apl-source:30
while احتمال_تطابق(ن) <= 0.5:
  # apl-source:31
  ن = ن + 1
# apl-source:32
تأكد_يساوي(ن, 23, "23 هو الحد")
# apl-source:33

# apl-source:34
# عند 50 شخصاً يتجاوز 97%
# apl-source:35
تأكد_يساوي(احتمال_تطابق(50) > 0.97, 1 == 1, "P(50) > 97%")
# apl-source:36

# apl-source:37
# عند 366 يصبح يقيناً (مبدأ حمام الزاجل)
# apl-source:38
تأكد_يساوي(احتمال_تطابق(366), 1.0, "366 يقين")
# apl-source:39
