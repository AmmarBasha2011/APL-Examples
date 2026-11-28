
# apl-source:1
# مثال 964 — خلط فيشر-يتس
# apl-source:2
# Fisher-Yates shuffle
# apl-source:3
# Demonstrates: تبديل من الذيل للرأس
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/964-fisher-yates.apl
# apl-source:6

# apl-source:7
# خلط فيشر-يتس: تبديل من الذيل نحو الرأس بمؤشر عشوائي
# apl-source:8
# مولد حتمي يجعل الناتج قابلاً للتحقق
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
بذرة = [42]
# apl-source:19
def عشوائي(حد):
  # apl-source:20
  بذرة[0] = (بذرة[0] * 1103515245 + 12345) % 2147483648
  # apl-source:21
  return بذرة[0] % حد
# apl-source:22

# apl-source:23
def اخلط(عناصر):
  # apl-source:24
  for i in range(len(عناصر) - 1, 0, -1):
    # apl-source:25
    ج = عشوائي(i + 1)
    # apl-source:26
    مؤقت = عناصر[i]
    # apl-source:27
    عناصر[i] = عناصر[ج]
    # apl-source:28
    عناصر[ج] = مؤقت
  # apl-source:29
  return عناصر
# apl-source:30

# apl-source:31
نتيجة = اخلط([1, 2, 3, 4, 5, 6, 7, 8])
# apl-source:32
تأكد_يساوي(نتيجة[0], 3, "العنصر الأول")
# apl-source:33
تأكد_يساوي(نتيجة[1], 5, "العنصر الثاني")
# apl-source:34
تأكد_يساوي(نتيجة[2], 7, "العنصر الثالث")
# apl-source:35
تأكد_يساوي(نتيجة[3], 8, "العنصر الرابع")
# apl-source:36
تأكد_يساوي(نتيجة[4], 2, "العنصر الخامس")
# apl-source:37
تأكد_يساوي(نتيجة[5], 6, "العنصر السادس")
# apl-source:38
تأكد_يساوي(نتيجة[6], 1, "العنصر السابع")
# apl-source:39
تأكد_يساوي(نتيجة[7], 4, "العنصر الثامن")
# apl-source:40
