
# apl-source:1
# مثال 1283 — عدد أطول المتتاليات
# apl-source:2
# Number of longest increasing subsequences
# apl-source:3
# Demonstrates: برمجة ديناميكية
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1283-lis-count.apl
# apl-source:6

# apl-source:7
# لكل موضع نخزن الطول وعدد الطرق
# apl-source:8
# وندمج الطرق عند تساوي الطول
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
def عدد_المتتاليات(أ):
  # apl-source:19
  ن = len(أ)
  # apl-source:20
  if ن == 0:
    # apl-source:21
    return 0
  # apl-source:22
  طول_ = [1] * ن
  # apl-source:23
  عدد_ = [1] * ن
  # apl-source:24
  for ع in range(ن):
    # apl-source:25
    for ج in range(ع):
      # apl-source:26
      if أ[ج] < أ[ع]:
        # apl-source:27
        if طول_[ج] + 1 > طول_[ع]:
          # apl-source:28
          طول_[ع] = طول_[ج] + 1
          # apl-source:29
          عدد_[ع] = عدد_[ج]
        # apl-source:30
        elif طول_[ج] + 1 == طول_[ع]:
          # apl-source:31
          عدد_[ع] = عدد_[ع] + عدد_[ج]
  # apl-source:32
  اقصى = 0
  # apl-source:33
  for ل in طول_:
    # apl-source:34
    if ل > اقصى:
      # apl-source:35
      اقصى = ل
  # apl-source:36
  مج = 0
  # apl-source:37
  for ع in range(ن):
    # apl-source:38
    if طول_[ع] == اقصى:
      # apl-source:39
      مج = مج + عدد_[ع]
  # apl-source:40
  return مج
# apl-source:41

# apl-source:42
تأكد_يساوي(عدد_المتتاليات([1,3,5,4,7]), 2, "مثال أول")
# apl-source:43
تأكد_يساوي(عدد_المتتاليات([2,2,2,2,2]), 5, "متساوية")
# apl-source:44
تأكد_يساوي(عدد_المتتاليات([1,2,4,3,5,4,7,2]), 3, "ثلاث")
# apl-source:45
