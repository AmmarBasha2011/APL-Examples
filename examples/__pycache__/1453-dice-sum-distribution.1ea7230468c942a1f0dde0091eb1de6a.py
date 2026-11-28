
# apl-source:1
# مثال 1453 — توزيع مجموع النردين
# apl-source:2
# Distribution of two dice sums
# apl-source:3
# Demonstrates: محاكاة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1453-dice-sum-distribution.apl
# apl-source:6

# apl-source:7
# نعد كل الأزواج الممكنة
# apl-source:8
# نخزن العدد لكل مجموع
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
def توزيع_النردين():
  # apl-source:19
  عد = {}
  # apl-source:20
  for أ in range(1, 7):
    # apl-source:21
    for ب in range(1, 7):
      # apl-source:22
      م = أ + ب
      # apl-source:23
      عد[م] = عد.get(م, 0) + 1
  # apl-source:24
  return عد
# apl-source:25

# apl-source:26
نتيجة = توزيع_النردين()
# apl-source:27
تأكد_يساوي(نتيجة[7], 6, "سبعة")
# apl-source:28
تأكد_يساوي(نتيجة[2], 1, "اثنان")
# apl-source:29
تأكد_يساوي(نتيجة[12], 1, "اثنا عشر")
# apl-source:30
تأكد_يساوي(len(نتيجة), 11, "أحد عشر مجموعاً")
# apl-source:31
