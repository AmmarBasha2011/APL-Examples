
# apl-source:1
# مثال 1857 — مجموع أكبر عددين مختلفين
# apl-source:2
# Sum of two largest distinct values
# apl-source:3
# Demonstrates: مصفوفات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1857-sum-of-two-largest-distinct.apl
# apl-source:6

# apl-source:7
# نحدث الأكبر والثاني
# apl-source:8
# نتجاهل التكرار
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
def مجموع_الأكبرين(ق):
  # apl-source:19
  أول = -1000000
  # apl-source:20
  ثان = -1000000
  # apl-source:21
  for ع in ق:
    # apl-source:22
    if ع > أول:
      # apl-source:23
      ثان = أول
      # apl-source:24
      أول = ع
    # apl-source:25
    elif ع > ثان and ع != أول:
      # apl-source:26
      ثان = ع
  # apl-source:27
  return أول + ثان
# apl-source:28

# apl-source:29
تأكد_يساوي(مجموع_الأكبرين([1, 5, 3, 5]), 8, "تكرار")
# apl-source:30
تأكد_يساوي(مجموع_الأكبرين([2, 9]), 11, "اثنان")
# apl-source:31
تأكد_يساوي(مجموع_الأكبرين([-1, -2, -3]), -3, "سالبة")
# apl-source:32
