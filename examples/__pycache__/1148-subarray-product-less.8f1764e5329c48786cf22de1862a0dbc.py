
# apl-source:1
# مثال 1148 — جداء أقل من حد
# apl-source:2
# Subarrays with product less than k
# apl-source:3
# Demonstrates: نافذة منزلقة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1148-subarray-product-less.apl
# apl-source:6

# apl-source:7
# نوسع النافذة يميناً ونضيق يساراً
# apl-source:8
# وكل توسعة تضيف بعدد طول النافذة
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
def عدّ_جداء(أ, ك):
  # apl-source:19
  if ك <= 1:
    # apl-source:20
    return 0
  # apl-source:21
  جداء = 1
  # apl-source:22
  يسار = 0
  # apl-source:23
  عدد_ = 0
  # apl-source:24
  for يمين in range(len(أ)):
    # apl-source:25
    جداء = جداء * أ[يمين]
    # apl-source:26
    while جداء >= ك:
      # apl-source:27
      جداء = جداء // أ[يسار]
      # apl-source:28
      يسار = يسار + 1
    # apl-source:29
    عدد_ = عدد_ + (يمين - يسار + 1)
  # apl-source:30
  return عدد_
# apl-source:31

# apl-source:32
تأكد_يساوي(عدّ_جداء([10,5,2,6], 100), 8, "مثال أول")
# apl-source:33
تأكد_يساوي(عدّ_جداء([1,2,3], 0), 0, "حد صفر")
# apl-source:34
تأكد_يساوي(عدّ_جداء([1,1,1], 2), 6, "واحدات")
# apl-source:35
تأكد_يساوي(عدّ_جداء([5], 5), 0, "مساوٍ للحد")
# apl-source:36
