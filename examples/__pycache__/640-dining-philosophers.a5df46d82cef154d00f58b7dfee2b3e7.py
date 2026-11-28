
# apl-source:1
# مثال 640 — الفلاسفة المتعشون
# apl-source:2
# Dining philosophers
# apl-source:3
# Demonstrates: جمود، ترتيب موارد، تجويع
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/640-dining-philosophers.apl
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
# الفلاسفة المتعشون: تجنب الجمود بترتيب الموارد
# apl-source:25
# Demonstrates: قفل بترتيب رقمي, كسر الانتظار الدائري, محاكاة وجبات
# apl-source:26
# كل فيلسوف يلتقط الشوكة الأقل رقما أولا
# apl-source:27

# apl-source:28
def حاكي(عدد, وجبات):
  # apl-source:29
  شوك = [True] * عدد
  # apl-source:30
  أكل = [0] * عدد
  # apl-source:31
  for جولة in range(وجبات * 3):
    # apl-source:32
    for ف in range(عدد):
      # apl-source:33
      يسار = ف
      # apl-source:34
      يمين = (ف + 1) % عدد
      # apl-source:35
      أول = min(يسار, يمين)
      # apl-source:36
      ثان = max(يسار, يمين)
      # apl-source:37
      if شوك[أول] and شوك[ثان]:
        # apl-source:38
        شوك[أول] = False
        # apl-source:39
        شوك[ثان] = False
        # apl-source:40
        أكل[ف] = أكل[ف] + 1
        # apl-source:41
        شوك[أول] = True
        # apl-source:42
        شوك[ثان] = True
  # apl-source:43
  return أكل
# apl-source:44

# apl-source:45
أكل = حاكي(5, 3)
# apl-source:46
print("وجبات كل فيلسوف:", أكل)
# apl-source:47
مجموع = 0
# apl-source:48
for وجبة in أكل:
  # apl-source:49
  مجموع = مجموع + وجبة
# apl-source:50
تأكد_يساوي(مجموع, 45, "خمسة فلاسفة × 3 جولات × 3 فرص")
# apl-source:51
تأكد_يساوي(min(أكل) > 0, True, "لا جمود ولا تجويع بترتيب الموارد")
# apl-source:52
