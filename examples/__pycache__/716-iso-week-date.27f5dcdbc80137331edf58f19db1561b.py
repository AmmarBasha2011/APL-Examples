
# apl-source:1
# مثال 716 — تاريخ الأسبوع ISO
# apl-source:2
# ISO 8601 week date
# apl-source:3
# Demonstrates: قاعدة الخميس، أسبوع 53، حدود سنة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/716-iso-week-date.apl
# apl-source:6

# apl-source:7
# Assertion style:
# apl-source:8
#   دالة تأكد_يساوي(فعلي, متوقع, اسم):
# apl-source:9
#     لو فعلي != متوقع:
# apl-source:10
#       اطبع "فشل:", اسم
# apl-source:11
#       اطبع "  متوقع:", متوقع
# apl-source:12
#       اطبع "  فعلي:", فعلي
# apl-source:13
#       قياسي_نظام_اخرج(1)
# apl-source:14
#     اطبع "ناجح:", اسم
# apl-source:15

# apl-source:16
def تأكد_يساوي(فعلي, متوقع, اسم):
  # apl-source:17
  if فعلي != متوقع:
    # apl-source:18
    print("فشل:", اسم)
    # apl-source:19
    print("  متوقع:", متوقع)
    # apl-source:20
    print("  فعلي:", فعلي)
    # apl-source:21
    قياسي_نظام_اخرج(1)
  # apl-source:22
  print("ناجح:", اسم)
# apl-source:23

# apl-source:24
# تاريخ الأسبوع ISO 8601: سنة الأسبوع ورقمها ويومها
# apl-source:25
# Demonstrates: قاعدة الخميس, الأسابيع 52/53, حدود السنة
# apl-source:26
# 2021-01-01 تنتمي إلى الأسبوع 53 من 2020
# apl-source:27

# apl-source:28
def إلى_جولياني(سنة, شهر, يوم):
  # apl-source:29
  أ = (14 - شهر) // 12
  # apl-source:30
  س2 = سنة + 4800 - أ
  # apl-source:31
  ش2 = شهر + 12 * أ - 3
  # apl-source:32
  return يوم + (153 * ش2 + 2) // 5 + 365 * س2 + س2 // 4 - س2 // 100 + س2 // 400 - 32045
# apl-source:33

# apl-source:34
def من_جولياني(ج):
  # apl-source:35
  ل = ج + 68569
  # apl-source:36
  ن = (4 * ل) // 146097
  # apl-source:37
  ل = ل - (146097 * ن + 3) // 4
  # apl-source:38
  ي = (4000 * (ل + 1)) // 1461001
  # apl-source:39
  ل = ل - (1461 * ي) // 4 + 31
  # apl-source:40
  ش = (80 * ل) // 2447
  # apl-source:41
  يوم = ل - (2447 * ش) // 80
  # apl-source:42
  ل = ش // 11
  # apl-source:43
  return [100 * (ن - 49) + ي + ل, ش + 2 - 12 * ل, يوم]
# apl-source:44

# apl-source:45
def ايزو_يوم(ج):
  # apl-source:46
  فهرس = (ج + 1) % 7
  # apl-source:47
  if فهرس == 0:
    # apl-source:48
    return 7
  # apl-source:49
  return فهرس
# apl-source:50

# apl-source:51
def أسبوع_ايزو(سنة, شهر, يوم):
  # apl-source:52
  ج = إلى_جولياني(سنة, شهر, يوم)
  # apl-source:53
  يوم_أ = ايزو_يوم(ج)
  # apl-source:54
  خميس = ج + 4 - يوم_أ
  # apl-source:55
  سنة_ايزو = من_جولياني(خميس)[0]
  # apl-source:56
  ج4 = إلى_جولياني(سنة_ايزو, 1, 4)
  # apl-source:57
  اثنين_أول = ج4 - ايزو_يوم(ج4) + 1
  # apl-source:58
  رقم = (ج - اثنين_أول) // 7 + 1
  # apl-source:59
  return [سنة_ايزو, رقم, يوم_أ]
# apl-source:60

# apl-source:61
تأكد_يساوي(أسبوع_ايزو(2024, 1, 1), [2024, 1, 1], "أول 2024 اثنين أسبوع أول")
# apl-source:62
تأكد_يساوي(أسبوع_ايزو(2021, 1, 1), [2020, 53, 5], "أول 2021 من 2020")
# apl-source:63
تأكد_يساوي(أسبوع_ايزو(2020, 12, 31), [2020, 53, 4], "آخر 2020 أسبوع 53")
# apl-source:64
تأكد_يساوي(أسبوع_ايزو(2023, 1, 1), [2022, 52, 7], "أول 2023 أحد من 2022")
# apl-source:65
تأكد_يساوي(أسبوع_ايزو(2024, 6, 15), [2024, 24, 6], "منتصف 2024")
# apl-source:66
تأكد_يساوي(أسبوع_ايزو(2026, 11, 24), [2026, 48, 2], "اليوم الحالي")
# apl-source:67
print(أسبوع_ايزو(2021, 1, 1))
# apl-source:68
