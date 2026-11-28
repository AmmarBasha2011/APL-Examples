
# apl-source:1
# مثال 1459 — منظم حرارة بفارق تشغيل
# apl-source:2
# Thermostat with hysteresis
# apl-source:3
# Demonstrates: محاكاة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1459-thermostat-hysteresis.apl
# apl-source:6

# apl-source:7
# يعمل عند تجاوز الحد الأعلى
# apl-source:8
# يتوقف عند النزول تحت الحد الأدنى
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
def حالات_المكيف(قراءات, أدنى, أعلى):
  # apl-source:19
  يعمل = False
  # apl-source:20
  نتيجة = []
  # apl-source:21
  for ق in قراءات:
    # apl-source:22
    if ق > أعلى:
      # apl-source:23
      يعمل = True
    # apl-source:24
    elif ق < أدنى:
      # apl-source:25
      يعمل = False
    # apl-source:26
    نتيجة.append(يعمل)
  # apl-source:27
  return نتيجة
# apl-source:28

# apl-source:29
تأكد_يساوي(حالات_المكيف([20, 26, 24, 21, 19, 22], 21, 25), [False, True, True, True, False, False], "دورة كاملة")
# apl-source:30
تأكد_يساوي(حالات_المكيف([23, 23], 21, 25), [False, False], "داخل المجال")
# apl-source:31
