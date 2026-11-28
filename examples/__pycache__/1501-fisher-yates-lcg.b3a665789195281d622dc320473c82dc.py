
# apl-source:1
# مثال 1501 — خلط فيشر ييتس بمولد ثابت
# apl-source:2
# Fisher Yates shuffle with LCG
# apl-source:3
# Demonstrates: ألعاب
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1501-fisher-yates-lcg.apl
# apl-source:6

# apl-source:7
# نختار موقعاً عشوائياً من المتبقي
# apl-source:8
# نبدل ونكمل نزولاً
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
def خلط(أ, بذرة):
  # apl-source:19
  ح = بذرة
  # apl-source:20
  ع = len(أ) - 1
  # apl-source:21
  while ع > 0:
    # apl-source:22
    ح = (ح * 1103515245 + 12345) % 2147483648
    # apl-source:23
    ي = ح % (ع + 1)
    # apl-source:24
    ت = أ[ع]
    # apl-source:25
    أ[ع] = أ[ي]
    # apl-source:26
    أ[ي] = ت
    # apl-source:27
    ع = ع - 1
  # apl-source:28
  return أ
# apl-source:29

# apl-source:30
أ1 = خلط([1, 2, 3, 4, 5, 6], 42)
# apl-source:31
أ2 = خلط([1, 2, 3, 4, 5, 6], 42)
# apl-source:32
تأكد_يساوي(أ1, أ2, "نفس البذرة نفس الخلط")
# apl-source:33
مجموع = 0
# apl-source:34
for ع in أ1:
  # apl-source:35
  مجموع = مجموع + ع
# apl-source:36
تأكد_يساوي(مجموع, 21, "لم يضِع عنصر")
# apl-source:37
تأكد_يساوي(len(خلط([9], 1)), 1, "عنصر واحد")
# apl-source:38
