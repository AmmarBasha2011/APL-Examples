
# apl-source:1
# مثال 875 — مفارقة مونتي هول
# apl-source:2
# Monty Hall
# apl-source:3
# Demonstrates: عد منهجي للحالات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/875-monty-hall.apl
# apl-source:6

# apl-source:7
# مفارقة مونتي هول: التبديل يفوز بثلثين والإبقاء بثلث
# apl-source:8
# إثبات بالعد المنهجي لكل الحالات بدل المحاكاة
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
# لكل (سيارة, اختيار): المضيف يفتح الباب المتبقي الوحيد الممكن
# apl-source:19
# التبديل يفوز دائماً عندما يكون الاختيار الأول خاطئاً
# apl-source:20
فوز_تبديل = 0
# apl-source:21
فوز_إبقاء = 0
# apl-source:22
حالات = 0
# apl-source:23
for سيارة in range(3):
  # apl-source:24
  for اختيار in range(3):
    # apl-source:25
    حالات = حالات + 1
    # apl-source:26
    if اختيار == سيارة:
      # apl-source:27
      فوز_إبقاء = فوز_إبقاء + 1
    # apl-source:28
    else:
      # apl-source:29
      # المضيف يكشف الثالثة والتبديل يصيب السيارة
      # apl-source:30
      فوز_تبديل = فوز_تبديل + 1
# apl-source:31

# apl-source:32
print("فوز التبديل:", فوز_تبديل, "من", حالات)
# apl-source:33
print("فوز الإبقاء:", فوز_إبقاء, "من", حالات)
# apl-source:34

# apl-source:35
تأكد_يساوي(حالات, 9, "تسع حالات")
# apl-source:36
تأكد_يساوي(فوز_تبديل, 6, "التبديل يفوز في 6 من 9")
# apl-source:37
تأكد_يساوي(فوز_إبقاء, 3, "الإبقاء يفوز في 3 من 9")
# apl-source:38
تأكد_يساوي(فوز_تبديل * 3 == حالات * 2, 1 == 1, "التبديل = 2/3 بالضبط")
# apl-source:39
