
# apl-source:1
# مثال 956 — استيفاء لاغرانج
# apl-source:2
# Lagrange interpolation
# apl-source:3
# Demonstrates: حدود أساس متعامدة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/956-lagrange.apl
# apl-source:6

# apl-source:7
# استيفاء لاغرانج: كثير الحدود الوحيد المار بنقاط معطاة
# apl-source:8
# أساس مشاركة الأسرار والاستيفاء العددي
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
def استوف(نقاط_س, نقاط_ص, س):
  # apl-source:19
  مجموع = 0
  # apl-source:20
  for i in range(len(نقاط_س)):
    # apl-source:21
    حد = نقاط_ص[i]
    # apl-source:22
    for ج in range(len(نقاط_س)):
      # apl-source:23
      if i != ج:
        # apl-source:24
        حد = حد * (س - نقاط_س[ج]) / (نقاط_س[i] - نقاط_س[ج])
    # apl-source:25
    مجموع = مجموع + حد
  # apl-source:26
  return مجموع
# apl-source:27

# apl-source:28
# النقاط (0,1) (1,3) (2,7) تقع على ص = س^2 + س + 1
# apl-source:29
نقاط_س = [0, 1, 2]
# apl-source:30
نقاط_ص = [1, 3, 7]
# apl-source:31

# apl-source:32
print("عند 3:", استوف(نقاط_س, نقاط_ص, 3))
# apl-source:33
print("عند 1.5:", استوف(نقاط_س, نقاط_ص, 1.5))
# apl-source:34

# apl-source:35
# 3^2+3+1 = 13
# apl-source:36
تأكد_يساوي(round(استوف(نقاط_س, نقاط_ص, 3), 6), 13, "استيفاء عند 3")
# apl-source:37
# 1.5^2+1.5+1 = 4.75
# apl-source:38
تأكد_يساوي(round(استوف(نقاط_س, نقاط_ص, 1.5), 6), 4.75, "استيفاء عند 1.5")
# apl-source:39

# apl-source:40
# يمر بنقاط العينة نفسها
# apl-source:41
for i in range(3):
  # apl-source:42
  تأكد_يساوي(round(استوف(نقاط_س, نقاط_ص, نقاط_س[i]), 6), نقاط_ص[i], "نقطة " + str(i))
# apl-source:43
