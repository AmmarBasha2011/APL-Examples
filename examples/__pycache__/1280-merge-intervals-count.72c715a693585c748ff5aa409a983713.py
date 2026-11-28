
# apl-source:1
# مثال 1280 — عدد المجالات بعد الدمج
# apl-source:2
# Merged intervals count
# apl-source:3
# Demonstrates: ترتيب
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1280-merge-intervals-count.apl
# apl-source:6

# apl-source:7
# نرتب بالبداية
# apl-source:8
# وندمج كل مجال يبدأ قبل نهاية السابق
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
def ادمج_مجالات(م):
  # apl-source:19
  if len(م) == 0:
    # apl-source:20
    return []
  # apl-source:21
  ق = sorted(م)
  # apl-source:22
  ناتج = [ق[0]]
  # apl-source:23
  for ع in range(1, len(ق)):
    # apl-source:24
    اخر = ناتج[-1]
    # apl-source:25
    if ق[ع][0] <= اخر[1]:
      # apl-source:26
      if ق[ع][1] > اخر[1]:
        # apl-source:27
        اخر[1] = ق[ع][1]
    # apl-source:28
    else:
      # apl-source:29
      ناتج = ناتج + [ق[ع]]
  # apl-source:30
  return ناتج
# apl-source:31

# apl-source:32
تأكد_يساوي(ادمج_مجالات([[1,3],[2,6],[8,10],[15,18]]), [[1,6],[8,10],[15,18]], "مثال أول")
# apl-source:33
تأكد_يساوي(ادمج_مجالات([[1,4],[4,5]]), [[1,5]], "متلاصقة")
# apl-source:34
تأكد_يساوي(len(ادمج_مجالات([[1,10],[2,3],[4,5]])), 1, "مجال يحوي الباقي")
# apl-source:35
تأكد_يساوي(ادمج_مجالات([]), [], "فارغة")
# apl-source:36
