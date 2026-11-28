
# apl-source:1
# مثال 899 — تتابعات جزئية مميزة
# apl-source:2
# Distinct subsequences
# apl-source:3
# Demonstrates: خصم آخر ظهور سابق
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/899-distinct-subsequences.apl
# apl-source:6

# apl-source:7
# عدد التتابعات الجزئية المميزة لسلسلة (برمجة ديناميكية)
# apl-source:8
# ع[i] = 2*ع[i-1] - ع[آخر ظهور سابق للحرف]
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
def عدد_مميزة(سلسلة):
  # apl-source:19
  ن = len(سلسلة)
  # apl-source:20
  ع = [1]
  # apl-source:21
  آخر = []
  # apl-source:22
  for i in range(ن):
    # apl-source:23
    حرف = سلسلة[i]
    # apl-source:24
    جديد = 2 * ع[i]
    # apl-source:25
    # آخر ظهور سابق للحرف
    # apl-source:26
    سابق = -1
    # apl-source:27
    for ج in range(len(آخر)):
      # apl-source:28
      if آخر[ج][0] == حرف:
        # apl-source:29
        سابق = آخر[ج][1]
    # apl-source:30
    if سابق >= 0:
      # apl-source:31
      جديد = جديد - ع[سابق]
    # apl-source:32
    ع = ع + [جديد]
    # apl-source:33
    # حدّث آخر ظهور
    # apl-source:34
    وجد = 0
    # apl-source:35
    for ج in range(len(آخر)):
      # apl-source:36
      if آخر[ج][0] == حرف:
        # apl-source:37
        آخر[ج][1] = i
        # apl-source:38
        وجد = 1
    # apl-source:39
    if وجد == 0:
      # apl-source:40
      آخر = آخر + [[حرف, i]]
  # apl-source:41
  return ع[ن] - 1
# apl-source:42

# apl-source:43
print("gfg:", عدد_مميزة("gfg"))
# apl-source:44
print("aba:", عدد_مميزة("aba"))
# apl-source:45

# apl-source:46
# التتابعات غير الفارغة المميزة لـ gfg: g, f, gf, gg, fg, gfg
# apl-source:47
تأكد_يساوي(عدد_مميزة("gfg"), 6, "gfg = 6")
# apl-source:48
# aba: a, b, ab, aa, ba, aba
# apl-source:49
تأكد_يساوي(عدد_مميزة("aba"), 6, "aba = 6")
# apl-source:50
# حرف واحد
# apl-source:51
تأكد_يساوي(عدد_مميزة("z"), 1, "حرف واحد")
# apl-source:52
# كلها متماثلة: aaa لها a, aa, aaa
# apl-source:53
تأكد_يساوي(عدد_مميزة("aaa"), 3, "aaa = 3")
# apl-source:54
