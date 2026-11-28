
# apl-source:1
# مثال 938 — الفرز البايتونيكي
# apl-source:2
# Bitonic sort
# apl-source:3
# Demonstrates: شبكة مقارنات ثابتة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/938-bitonic-sort.apl
# apl-source:6

# apl-source:7
# فرز البايتونيك: شبكة مقارنات ثابتة صالحة للتوازي
# apl-source:8
# عدد المقارنات لا يعتمد على البيانات
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
def فرز_بايتونيك(قيم):
  # apl-source:19
  م = []
  # apl-source:20
  for x in قيم:
    # apl-source:21
    م = م + [x]
  # apl-source:22
  ن = len(م)
  # apl-source:23
  ك = 2
  # apl-source:24
  while ك <= ن:
    # apl-source:25
    ج = ك // 2
    # apl-source:26
    while ج > 0:
      # apl-source:27
      for i in range(ن):
        # apl-source:28
        شريك = i ^ ج
        # apl-source:29
        if شريك > i:
          # apl-source:30
          if (i & ك) == 0 and م[i] > م[شريك]:
            # apl-source:31
            مؤقت = م[i]
            # apl-source:32
            م[i] = م[شريك]
            # apl-source:33
            م[شريك] = مؤقت
          # apl-source:34
          if (i & ك) != 0 and م[i] < م[شريك]:
            # apl-source:35
            مؤقت = م[i]
            # apl-source:36
            م[i] = م[شريك]
            # apl-source:37
            م[شريك] = مؤقت
      # apl-source:38
      ج = ج // 2
    # apl-source:39
    ك = ك * 2
  # apl-source:40
  return م
# apl-source:41

# apl-source:42
نتيجة = فرز_بايتونيك([3, 7, 4, 8, 6, 2, 1, 5])
# apl-source:43
print("المرتبة:", نتيجة)
# apl-source:44

# apl-source:45
تأكد_يساوي(len(نتيجة), 8, "الطول")
# apl-source:46
تأكد_يساوي(نتيجة[0], 1, "الأصغر")
# apl-source:47
تأكد_يساوي(نتيجة[7], 8, "الأكبر")
# apl-source:48
for i in range(8):
  # apl-source:49
  تأكد_يساوي(نتيجة[i], i + 1, "عنصر " + str(i))
# apl-source:50

# apl-source:51
# حالات حدية بطول قوة اثنين
# apl-source:52
تأكد_يساوي(فرز_بايتونيك([2, 1])[0], 1, "عنصران")
# apl-source:53
مفرد = فرز_بايتونيك([42])
# apl-source:54
تأكد_يساوي(مفرد[0], 42, "مفرد")
# apl-source:55

# apl-source:56
# مرتبة عكسياً
# apl-source:57
معكوسة = فرز_بايتونيك([4, 3, 2, 1])
# apl-source:58
تأكد_يساوي(معكوسة[0], 1, "عكس أول")
# apl-source:59
تأكد_يساوي(معكوسة[3], 4, "عكس أخير")
# apl-source:60
