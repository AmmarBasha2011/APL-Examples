
# apl-source:1
# مثال 1271 — مصفوفة الفروق
# apl-source:2
# Difference array range updates
# apl-source:3
# Demonstrates: فروق
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1271-difference-array.apl
# apl-source:6

# apl-source:7
# نضيف الزيادة عند بداية المجال ونطرحها بعد نهايته
# apl-source:8
# ثم نجمع تراكمياً
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
def طبق(ن, تحديثات):
  # apl-source:19
  فروق = [0] * (ن + 1)
  # apl-source:20
  for ت in تحديثات:
    # apl-source:21
    فروق[ت[0]] = فروق[ت[0]] + ت[2]
    # apl-source:22
    فروق[ت[1] + 1] = فروق[ت[1] + 1] - ت[2]
  # apl-source:23
  ناتج = []
  # apl-source:24
  مج = 0
  # apl-source:25
  for ع in range(ن):
    # apl-source:26
    مج = مج + فروق[ع]
    # apl-source:27
    ناتج = ناتج + [مج]
  # apl-source:28
  return ناتج
# apl-source:29

# apl-source:30
تأكد_يساوي(طبق(5, [[1,3,2],[2,4,3],[0,2,-2]]), [-2,0,3,5,3], "مثال أول")
# apl-source:31
تأكد_يساوي(طبق(3, []), [0,0,0], "بلا تحديثات")
# apl-source:32
تأكد_يساوي(طبق(4, [[0,3,1]]), [1,1,1,1], "كل المجال")
# apl-source:33
