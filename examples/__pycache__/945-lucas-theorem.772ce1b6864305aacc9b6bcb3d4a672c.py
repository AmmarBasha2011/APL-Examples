
# apl-source:1
# مثال 945 — مبرهنة لوكاس
# apl-source:2
# Lucas theorem
# apl-source:3
# Demonstrates: توافيق على أرقام p-ية
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/945-lucas-theorem.apl
# apl-source:6

# apl-source:7
# مبرهنة لوكاس: التوافيق الكبيرة مودولو عدد أولي
# apl-source:8
# C(n,k) mod p = حاصل ضرب C(ni,ki) mod p على أرقام p-ية
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
def توافيق_صغيرة(ن, ك):
  # apl-source:19
  if ك > ن:
    # apl-source:20
    return 0
  # apl-source:21
  ناتج = 1
  # apl-source:22
  for i in range(ك):
    # apl-source:23
    ناتج = ناتج * (ن - i) // (i + 1)
  # apl-source:24
  return ناتج
# apl-source:25

# apl-source:26
def لوكاس(ن, ك, أولي):
  # apl-source:27
  ناتج = 1
  # apl-source:28
  م_ن = ن
  # apl-source:29
  م_ك = ك
  # apl-source:30
  while م_ن > 0 or م_ك > 0:
    # apl-source:31
    رقم_ن = م_ن % أولي
    # apl-source:32
    رقم_ك = م_ك % أولي
    # apl-source:33
    if رقم_ك > رقم_ن:
      # apl-source:34
      return 0
    # apl-source:35
    ناتج = (ناتج * توافيق_صغيرة(رقم_ن, رقم_ك)) % أولي
    # apl-source:36
    م_ن = م_ن // أولي
    # apl-source:37
    م_ك = م_ك // أولي
  # apl-source:38
  return ناتج
# apl-source:39

# apl-source:40
print("C(8,3) mod 5 =", لوكاس(8, 3, 5))
# apl-source:41
print("C(10,3) mod 7 =", لوكاس(10, 3, 7))
# apl-source:42

# apl-source:43
# C(8,3)=56 و56 مودولو 5 = 1
# apl-source:44
تأكد_يساوي(لوكاس(8, 3, 5), 1, "C(8,3) مودولو 5")
# apl-source:45
# C(10,3)=120 و120 مودولو 7 = 1
# apl-source:46
تأكد_يساوي(لوكاس(10, 3, 7), 1, "C(10,3) مودولو 7")
# apl-source:47
# حالة رقم ك أكبر من رقم ن: صفر
# apl-source:48
تأكد_يساوي(لوكاس(2, 3, 5), 0, "ك أكبر من ن")
# apl-source:49

# apl-source:50
# يطابق الحساب المباشر على القيم الصغيرة
# apl-source:51
تأكد_يساوي(لوكاس(15, 5, 3), توافيق_صغيرة(15, 5) % 3, "مطابقة مباشرة 3")
# apl-source:52
تأكد_يساوي(لوكاس(20, 7, 11), توافيق_صغيرة(20, 7) % 11, "مطابقة مباشرة 11")
# apl-source:53
