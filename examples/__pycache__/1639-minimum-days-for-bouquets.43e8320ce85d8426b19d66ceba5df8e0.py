
# apl-source:1
# مثال 1639 — أقل أيام لصنع باقات
# apl-source:2
# Minimum days to make bouquets
# apl-source:3
# Demonstrates: بحث ثنائي
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1639-minimum-days-for-bouquets.apl
# apl-source:6

# apl-source:7
# الباقة من أزهار متجاورة متفتحة
# apl-source:8
# نجرب يوماً ونعد الباقات الممكنة
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
def باقات_في_يوم(تفتح, يوم, حجم):
  # apl-source:19
  عد = 0
  # apl-source:20
  متتالية = 0
  # apl-source:21
  for ت in تفتح:
    # apl-source:22
    if ت <= يوم:
      # apl-source:23
      متتالية = متتالية + 1
      # apl-source:24
      if متتالية == حجم:
        # apl-source:25
        عد = عد + 1
        # apl-source:26
        متتالية = 0
    # apl-source:27
    else:
      # apl-source:28
      متتالية = 0
  # apl-source:29
  return عد
# apl-source:30

# apl-source:31
def أقل_أيام(تفتح, باقات, حجم):
  # apl-source:32
  if باقات * حجم > len(تفتح):
    # apl-source:33
    return -1
  # apl-source:34
  ي = 1
  # apl-source:35
  ج = 1
  # apl-source:36
  for ت in تفتح:
    # apl-source:37
    if ت > ج:
      # apl-source:38
      ج = ت
  # apl-source:39
  while ي < ج:
    # apl-source:40
    م = (ي + ج) // 2
    # apl-source:41
    if باقات_في_يوم(تفتح, م, حجم) >= باقات:
      # apl-source:42
      ج = م
    # apl-source:43
    else:
      # apl-source:44
      ي = م + 1
  # apl-source:45
  return ي
# apl-source:46

# apl-source:47
تأكد_يساوي(أقل_أيام([1, 10, 3, 10, 2], 3, 1), 3, "ثلاث باقات")
# apl-source:48
تأكد_يساوي(أقل_أيام([1, 10, 3, 10, 2], 3, 2), -1, "مستحيل")
# apl-source:49
تأكد_يساوي(أقل_أيام([7, 7, 7, 7, 12, 7, 7], 2, 3), 12, "اثنا عشر")
# apl-source:50
