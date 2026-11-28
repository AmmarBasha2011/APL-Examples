
# apl-source:1
# مثال 1721 — منتجات تحتاج إعادة تخزين
# apl-source:2
# Inventory items needing restock
# apl-source:3
# Demonstrates: محاكاة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1721-inventory-restock-needed.apl
# apl-source:6

# apl-source:7
# القاموس يربط المنتج بكميته
# apl-source:8
# نجمع ما نقص عن الحد
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
def تحتاج(مخزن, حد):
  # apl-source:19
  ناتج = []
  # apl-source:20
  for ك in مخزن:
    # apl-source:21
    if مخزن[ك] < حد:
      # apl-source:22
      ناتج.append(ك)
  # apl-source:23
  ناتج.sort()
  # apl-source:24
  return ناتج
# apl-source:25

# apl-source:26
م = {"قلم": 3, "دفتر": 10, "ممحاة": 1}
# apl-source:27
تأكد_يساوي(تحتاج(م, 5), ["قلم", "ممحاة"], "نقص")
# apl-source:28
تأكد_يساوي(تحتاج(م, 1), [], "لا نقص")
# apl-source:29
تأكد_يساوي(تحتاج({}, 5), [], "فارغ")
# apl-source:30
