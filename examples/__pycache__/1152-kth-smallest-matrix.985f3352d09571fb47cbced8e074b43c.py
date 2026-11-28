
# apl-source:1
# مثال 1152 — أصغر عنصر ترتيبه k
# apl-source:2
# Kth smallest in sorted matrix
# apl-source:3
# Demonstrates: بحث على القيمة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1152-kth-smallest-matrix.apl
# apl-source:6

# apl-source:7
# نبحث ثنائياً عن القيمة نفسها
# apl-source:8
# ونعد كم عنصراً لا يتجاوزها
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
def عدّ_اقل_او_يساوي(م, قيمة):
  # apl-source:19
  ع = 0
  # apl-source:20
  for صف in م:
    # apl-source:21
    for س in صف:
      # apl-source:22
      if س <= قيمة:
        # apl-source:23
        ع = ع + 1
  # apl-source:24
  return ع
# apl-source:25

# apl-source:26
def الترتيب_ك(م, ك):
  # apl-source:27
  يسار = م[0][0]
  # apl-source:28
  يمين = م[-1][-1]
  # apl-source:29
  while يسار < يمين:
    # apl-source:30
    وسط = (يسار + يمين) // 2
    # apl-source:31
    if عدّ_اقل_او_يساوي(م, وسط) >= ك:
      # apl-source:32
      يمين = وسط
    # apl-source:33
    else:
      # apl-source:34
      يسار = وسط + 1
  # apl-source:35
  return يسار
# apl-source:36

# apl-source:37
م = [[1,5,9],[10,11,13],[12,13,15]]
# apl-source:38
تأكد_يساوي(الترتيب_ك(م, 8), 13, "الثامن")
# apl-source:39
تأكد_يساوي(الترتيب_ك(م, 1), 1, "الأول")
# apl-source:40
تأكد_يساوي(الترتيب_ك(م, 9), 15, "الأخير")
# apl-source:41
تأكد_يساوي(الترتيب_ك([[-5]], 1), -5, "عنصر")
# apl-source:42
