
# apl-source:1
# مثال 1298 — اختيار موزون
# apl-source:2
# Weighted random pick index
# apl-source:3
# Demonstrates: مجاميع تراكمية
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1298-random-pick-weight.apl
# apl-source:6

# apl-source:7
# نبني مجاميع تراكمية للأوزان
# apl-source:8
# وعدد عشوائي يقع في مجال فهرس معين
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
class موزون:
  # apl-source:19
  def __init__(ذات, اوزان):
    # apl-source:20
    ذات.تراكمي = []
    # apl-source:21
    مج = 0
    # apl-source:22
    for و in اوزان:
      # apl-source:23
      مج = مج + و
      # apl-source:24
      ذات.تراكمي = ذات.تراكمي + [مج]
    # apl-source:25
    ذات.كل = مج
# apl-source:26

  # apl-source:27
  def اختر(ذات, عدد_):
    # apl-source:28
    ع = عدد_ % ذات.كل
    # apl-source:29
    ي = 0
    # apl-source:30
    ن = len(ذات.تراكمي) - 1
    # apl-source:31
    while ي < ن:
      # apl-source:32
      م = (ي + ن) // 2
      # apl-source:33
      if ذات.تراكمي[م] > ع:
        # apl-source:34
        ن = م
      # apl-source:35
      else:
        # apl-source:36
        ي = م + 1
    # apl-source:37
    return ي
# apl-source:38

# apl-source:39
م = موزون([1, 3])
# apl-source:40
نتائج = []
# apl-source:41
for ع in range(4):
  # apl-source:42
  نتائج = نتائج + [م.اختر(ع)]
# apl-source:43
تأكد_يساوي(نتائج, [0, 1, 1, 1], "توزيع")
# apl-source:44
تأكد_يساوي(م.اختر(4), 0, "التفاف")
# apl-source:45
