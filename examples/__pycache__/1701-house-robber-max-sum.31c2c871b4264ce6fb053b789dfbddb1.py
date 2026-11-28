
# apl-source:1
# مثال 1701 — أقصى مجموع دون جارين
# apl-source:2
# Max sum without adjacent items
# apl-source:3
# Demonstrates: برمجة ديناميكية
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1701-house-robber-max-sum.apl
# apl-source:6

# apl-source:7
# نحتفظ بأفضل مجموع مع الأخذ ودونه
# apl-source:8
# نحدث مع كل عنصر
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
def أقصى_غير_متجاور(ق):
  # apl-source:19
  أخذ = 0
  # apl-source:20
  ترك = 0
  # apl-source:21
  for ع in ق:
    # apl-source:22
    جديد = ترك + ع
    # apl-source:23
    ترك = max(ترك, أخذ)
    # apl-source:24
    أخذ = جديد
  # apl-source:25
  return max(أخذ, ترك)
# apl-source:26

# apl-source:27
تأكد_يساوي(أقصى_غير_متجاور([1, 2, 3, 1]), 4, "أربعة")
# apl-source:28
تأكد_يساوي(أقصى_غير_متجاور([2, 7, 9, 3, 1]), 12, "اثنا عشر")
# apl-source:29
تأكد_يساوي(أقصى_غير_متجاور([5]), 5, "واحد")
# apl-source:30
