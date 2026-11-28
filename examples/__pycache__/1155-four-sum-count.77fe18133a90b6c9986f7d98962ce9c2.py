
# apl-source:1
# مثال 1155 — عد رباعيات
# apl-source:2
# Four sum count from four lists
# apl-source:3
# Demonstrates: جدول تجزئة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1155-four-sum-count.apl
# apl-source:6

# apl-source:7
# نخزن مجاميع أول قائمتين وعدد تكرارها
# apl-source:8
# ثم نبحث عن المكمل في مجاميع الأخريين
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
def عد_رباعيات(أ, ب, ج, د):
  # apl-source:19
  مجاميع = {}
  # apl-source:20
  for س in أ:
    # apl-source:21
    for ص in ب:
      # apl-source:22
      مجاميع[س + ص] = مجاميع.get(س + ص, 0) + 1
  # apl-source:23
  ناتج = 0
  # apl-source:24
  for س in ج:
    # apl-source:25
    for ص in د:
      # apl-source:26
      ناتج = ناتج + مجاميع.get(-(س + ص), 0)
  # apl-source:27
  return ناتج
# apl-source:28

# apl-source:29
تأكد_يساوي(عد_رباعيات([1,2], [-2,-1], [-1,2], [0,2]), 2, "مثال أول")
# apl-source:30
تأكد_يساوي(عد_رباعيات([0], [0], [0], [0]), 1, "أصفار")
# apl-source:31
تأكد_يساوي(عد_رباعيات([1], [1], [1], [1]), 0, "لا حل")
# apl-source:32
