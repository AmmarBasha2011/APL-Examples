
# apl-source:1
# مثال 1165 — متتاليات مميزة
# apl-source:2
# Distinct subsequences count
# apl-source:3
# Demonstrates: برمجة ديناميكية
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1165-distinct-subsequences.apl
# apl-source:6

# apl-source:7
# د[ج] عدد طرق تكوين أول ج حروف من الهدف
# apl-source:8
# نمر على حروف المصدر ونحدث الجدول عكسياً
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
def عدد_طرق(س, ه):
  # apl-source:19
  د = [0] * (len(ه) + 1)
  # apl-source:20
  د[0] = 1
  # apl-source:21
  for ح in س:
    # apl-source:22
    for ج in range(len(ه), 0, -1):
      # apl-source:23
      if ه[ج - 1] == ح:
        # apl-source:24
        د[ج] = د[ج] + د[ج - 1]
  # apl-source:25
  return د[len(ه)]
# apl-source:26

# apl-source:27
تأكد_يساوي(عدد_طرق("rabbbit", "rabbit"), 3, "مثال أول")
# apl-source:28
تأكد_يساوي(عدد_طرق("babgbag", "bag"), 5, "مثال ثان")
# apl-source:29
تأكد_يساوي(عدد_طرق("abc", "d"), 0, "لا طريقة")
# apl-source:30
تأكد_يساوي(عدد_طرق("aaa", "a"), 3, "ثلاث")
# apl-source:31
