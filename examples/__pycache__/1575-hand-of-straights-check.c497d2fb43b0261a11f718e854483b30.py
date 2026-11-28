
# apl-source:1
# مثال 1575 — هل تقسم الأوراق إلى متتاليات
# apl-source:2
# Hand of straights check
# apl-source:3
# Demonstrates: جشع
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1575-hand-of-straights-check.apl
# apl-source:6

# apl-source:7
# نبدأ من أصغر رقم متبق
# apl-source:8
# نخصم متتالية كاملة منه
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
def تقسيم_ممكن(أوراق, حجم):
  # apl-source:19
  if len(أوراق) % حجم != 0:
    # apl-source:20
    return False
  # apl-source:21
  عد = {}
  # apl-source:22
  for و in أوراق:
    # apl-source:23
    عد[و] = عد.get(و, 0) + 1
  # apl-source:24
  مفاتيح = []
  # apl-source:25
  for ك in عد:
    # apl-source:26
    مفاتيح.append(ك)
  # apl-source:27
  مفاتيح.sort()
  # apl-source:28
  for ك in مفاتيح:
    # apl-source:29
    if عد[ك] > 0:
      # apl-source:30
      كمية = عد[ك]
      # apl-source:31
      for ز in range(حجم):
        # apl-source:32
        if عد.get(ك + ز, 0) < كمية:
          # apl-source:33
          return False
        # apl-source:34
        عد[ك + ز] = عد[ك + ز] - كمية
  # apl-source:35
  return True
# apl-source:36

# apl-source:37
تأكد_يساوي(تقسيم_ممكن([1, 2, 3, 6, 2, 3, 4, 7, 8], 3), True, "ممكن")
# apl-source:38
تأكد_يساوي(تقسيم_ممكن([1, 2, 3, 4, 5], 4), False, "العدد لا يقبل")
# apl-source:39
تأكد_يساوي(تقسيم_ممكن([1, 2, 4, 5], 2), True, "زوجان")
# apl-source:40
