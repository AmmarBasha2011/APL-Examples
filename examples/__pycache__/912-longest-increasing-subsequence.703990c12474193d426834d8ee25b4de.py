
# apl-source:1
# مثال 912 — أطول تتابع متزايد
# apl-source:2
# Longest increasing subsequence
# apl-source:3
# Demonstrates: صبر مع بحث ثنائي
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/912-longest-increasing-subsequence.apl
# apl-source:6

# apl-source:7
# أطول تتابع جزئي متزايد: صبر/بحث ثنائي O(n log n)
# apl-source:8
# ت[i] أصغر نهاية ممكنة لتتابع متزايد بطول i+1
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
def أطول_متزايد(مصفوفة):
  # apl-source:19
  ت = []
  # apl-source:20
  for x in مصفوفة:
    # apl-source:21
    # أول موضع في ت لا يصغر عن x (بحث ثنائي)
    # apl-source:22
    أدنى = 0
    # apl-source:23
    أعلى = len(ت)
    # apl-source:24
    while أدنى < أعلى:
      # apl-source:25
      وسط = (أدنى + أعلى) // 2
      # apl-source:26
      if ت[وسط] < x:
        # apl-source:27
        أدنى = وسط + 1
      # apl-source:28
      else:
        # apl-source:29
        أعلى = وسط
    # apl-source:30
    if أدنى == len(ت):
      # apl-source:31
      ت = ت + [x]
    # apl-source:32
    else:
      # apl-source:33
      ت[أدنى] = x
  # apl-source:34
  return len(ت)
# apl-source:35

# apl-source:36
print("LIS:", أطول_متزايد([10, 9, 2, 5, 3, 7, 101, 18]))
# apl-source:37

# apl-source:38
تأكد_يساوي(أطول_متزايد([10, 9, 2, 5, 3, 7, 101, 18]), 4, "المثال القياسي")
# apl-source:39
تأكد_يساوي(أطول_متزايد([0, 1, 0, 3, 2, 3]), 4, "مع تكرار")
# apl-source:40
تأكد_يساوي(أطول_متزايد([7, 7, 7, 7]), 1, "كلها متساوية")
# apl-source:41
تأكد_يساوي(أطول_متزايد([1, 2, 3, 4, 5]), 5, "مرتبة تصاعدياً")
# apl-source:42
تأكد_يساوي(أطول_متزايد([5, 4, 3, 2, 1]), 1, "مرتبة تنازلياً")
# apl-source:43
تأكد_يساوي(أطول_متزايد([]), 0, "فارغة")
# apl-source:44
