
# apl-source:1
# مثال 1480 — مجاميع الصفوف والأعمدة
# apl-source:2
# Row and column sums
# apl-source:3
# Demonstrates: مصفوفات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1480-row-and-column-sums.apl
# apl-source:6

# apl-source:7
# نحتفظ بمجموع لكل صف ولكل عمود
# apl-source:8
# نضيف كل خانة للمجموعين
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
def المجاميع(م):
  # apl-source:19
  صفوف = []
  # apl-source:20
  أعمدة = []
  # apl-source:21
  for ع in range(len(م[0])):
    # apl-source:22
    أعمدة.append(0)
  # apl-source:23
  for ص in م:
    # apl-source:24
    مجموع = 0
    # apl-source:25
    for ع in range(len(ص)):
      # apl-source:26
      مجموع = مجموع + ص[ع]
      # apl-source:27
      أعمدة[ع] = أعمدة[ع] + ص[ع]
    # apl-source:28
    صفوف.append(مجموع)
  # apl-source:29
  return [صفوف, أعمدة]
# apl-source:30

# apl-source:31
تأكد_يساوي(المجاميع([[1, 2, 3], [4, 5, 6]]), [[6, 15], [5, 7, 9]], "اثنان في ثلاثة")
# apl-source:32
تأكد_يساوي(المجاميع([[5]]), [[5], [5]], "وحيدة")
# apl-source:33
