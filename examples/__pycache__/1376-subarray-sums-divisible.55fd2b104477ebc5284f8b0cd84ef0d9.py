
# apl-source:1
# مثال 1376 — مجاميع قابلة للقسمة
# apl-source:2
# Subarray sums divisible by K
# apl-source:3
# Demonstrates: مجاميع تراكمية
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1376-subarray-sums-divisible.apl
# apl-source:6

# apl-source:7
# مجموعان تراكميان بنفس الباقي يعنيان مصفوفة مقبولة
# apl-source:8
# نعد تكرار كل باقي
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
def عد_قابلة(أرقام, ك):
  # apl-source:19
  عدّ = {}
  # apl-source:20
  عدّ[0] = 1
  # apl-source:21
  مجموع = 0
  # apl-source:22
  نتيجة = 0
  # apl-source:23
  for ر in أرقام:
    # apl-source:24
    مجموع = مجموع + ر
    # apl-source:25
    باقي = ((مجموع % ك) + ك) % ك
    # apl-source:26
    سابق = عدّ.get(باقي, 0)
    # apl-source:27
    نتيجة = نتيجة + سابق
    # apl-source:28
    عدّ[باقي] = سابق + 1
  # apl-source:29
  return نتيجة
# apl-source:30

# apl-source:31
تأكد_يساوي(عد_قابلة([4,5,0,-2,-3,1], 5), 7, "سبعة")
# apl-source:32
تأكد_يساوي(عد_قابلة([5], 9), 0, "لا شيء")
# apl-source:33
تأكد_يساوي(عد_قابلة([0,0], 3), 3, "أصفار")
# apl-source:34
