
# apl-source:1
# مثال 1882 — أقرب جد مشترك
# apl-source:2
# Lowest common ancestor by parents
# apl-source:3
# Demonstrates: أشجار
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1882-lowest-common-ancestor-parents.apl
# apl-source:6

# apl-source:7
# نجمع أجداد الأولى
# apl-source:8
# أول جد للثانية موجود فيهم
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
def أقرب_جد(آباء, أ, ب):
  # apl-source:19
  أجداد = {}
  # apl-source:20
  ع = أ
  # apl-source:21
  while ع != -1:
    # apl-source:22
    أجداد[str(ع)] = 1
    # apl-source:23
    ع = آباء[ع]
  # apl-source:24
  ع = ب
  # apl-source:25
  while ع != -1:
    # apl-source:26
    if str(ع) in أجداد:
      # apl-source:27
      return ع
    # apl-source:28
    ع = آباء[ع]
  # apl-source:29
  return -1
# apl-source:30

# apl-source:31
آ = [-1, 0, 0, 1, 1, 2]
# apl-source:32
تأكد_يساوي(أقرب_جد(آ, 3, 4), 1, "أخوان")
# apl-source:33
تأكد_يساوي(أقرب_جد(آ, 3, 5), 0, "من فرعين")
# apl-source:34
تأكد_يساوي(أقرب_جد(آ, 3, 1), 1, "جد مباشر")
# apl-source:35
