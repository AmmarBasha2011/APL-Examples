
# apl-source:1
# مثال 1617 — دمج عدة قوائم مرتبة
# apl-source:2
# Merge k sorted lists
# apl-source:3
# Demonstrates: قوائم
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1617-merge-k-sorted-lists.apl
# apl-source:6

# apl-source:7
# ندمج قائمتين في كل مرة
# apl-source:8
# نكرر حتى تبقى قائمة واحدة
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
def ادمج_اثنتين(أ, ب):
  # apl-source:19
  ي = 0
  # apl-source:20
  ج = 0
  # apl-source:21
  ناتج = []
  # apl-source:22
  while ي < len(أ) and ج < len(ب):
    # apl-source:23
    if أ[ي] <= ب[ج]:
      # apl-source:24
      ناتج.append(أ[ي])
      # apl-source:25
      ي = ي + 1
    # apl-source:26
    else:
      # apl-source:27
      ناتج.append(ب[ج])
      # apl-source:28
      ج = ج + 1
  # apl-source:29
  for ع in range(ي, len(أ)):
    # apl-source:30
    ناتج.append(أ[ع])
  # apl-source:31
  for ع in range(ج, len(ب)):
    # apl-source:32
    ناتج.append(ب[ع])
  # apl-source:33
  return ناتج
# apl-source:34

# apl-source:35
def ادمج_الكل(قوائم):
  # apl-source:36
  ناتج = []
  # apl-source:37
  for ق in قوائم:
    # apl-source:38
    ناتج = ادمج_اثنتين(ناتج, ق)
  # apl-source:39
  return ناتج
# apl-source:40

# apl-source:41
تأكد_يساوي(ادمج_الكل([[1, 4, 5], [1, 3, 4], [2, 6]]), [1, 1, 2, 3, 4, 4, 5, 6], "ثلاث قوائم")
# apl-source:42
تأكد_يساوي(ادمج_الكل([]), [], "بلا قوائم")
# apl-source:43
تأكد_يساوي(ادمج_الكل([[], [1]]), [1], "قائمة فارغة")
# apl-source:44
