
# apl-source:1
# مثال 1318 — طرق الهدف
# apl-source:2
# Count ways to reach target by signs
# apl-source:3
# Demonstrates: برمجة ديناميكية
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1318-target-sum-combos.apl
# apl-source:6

# apl-source:7
# نتتبع كل المجاميع الممكنة وعدد طرقها
# apl-source:8
# نضيف أو نطرح كل عنصر
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
def عدد_الطرق(أ, هدف):
  # apl-source:19
  طرق = {0: 1}
  # apl-source:20
  for س in أ:
    # apl-source:21
    جديد = {}
    # apl-source:22
    for م in طرق:
      # apl-source:23
      جديد[م + س] = جديد.get(م + س, 0) + طرق[م]
      # apl-source:24
      جديد[م - س] = جديد.get(م - س, 0) + طرق[م]
    # apl-source:25
    طرق = جديد
  # apl-source:26
  return طرق.get(هدف, 0)
# apl-source:27

# apl-source:28
تأكد_يساوي(عدد_الطرق([1,1,1,1,1], 3), 5, "مثال أول")
# apl-source:29
تأكد_يساوي(عدد_الطرق([1], 1), 1, "عنصر")
# apl-source:30
تأكد_يساوي(عدد_الطرق([1], 2), 0, "مستحيل")
# apl-source:31
تأكد_يساوي(عدد_الطرق([0,0,0], 0), 8, "أصفار")
# apl-source:32
