
# apl-source:1
# مثال 905 — معامل كيندال تاو
# apl-source:2
# Kendall tau
# apl-source:3
# Demonstrates: أزواج متفقة ومخالفة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/905-kendall-tau.apl
# apl-source:6

# apl-source:7
# معامل كيندال تاو: ارتباط ترتيبي بين قائمتين
# apl-source:8
# تاو = (متفقة - مخالفة) / (ن(ن-1)/2)
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
def كيندال(أ, ب):
  # apl-source:19
  ن = len(أ)
  # apl-source:20
  متفقة = 0
  # apl-source:21
  مخالفة = 0
  # apl-source:22
  for i in range(ن):
    # apl-source:23
    for ج in range(i + 1, ن):
      # apl-source:24
      فرق_أ = أ[i] - أ[ج]
      # apl-source:25
      فرق_ب = ب[i] - ب[ج]
      # apl-source:26
      if فرق_أ * فرق_ب > 0:
        # apl-source:27
        متفقة = متفقة + 1
      # apl-source:28
      elif فرق_أ * فرق_ب < 0:
        # apl-source:29
        مخالفة = مخالفة + 1
  # apl-source:30
  return (متفقة - مخالفة) / (ن * (ن - 1) // 2)
# apl-source:31

# apl-source:32
ت1 = كيندال([1, 2, 3, 4], [1, 3, 2, 4])
# apl-source:33
print("تاو =", ت1)
# apl-source:34

# apl-source:35
تأكد_يساوي(round(ت1, 4), 0.6667, "زوج مخالف واحد من 6")
# apl-source:36

# apl-source:37
# تطابق تام
# apl-source:38
تأكد_يساوي(كيندال([1, 2, 3], [1, 2, 3]), 1, "تطابق تام = 1")
# apl-source:39

# apl-source:40
# انعكاس تام
# apl-source:41
تأكد_يساوي(كيندال([1, 2, 3], [3, 2, 1]), -1, "انعكاس تام = -1")
# apl-source:42
