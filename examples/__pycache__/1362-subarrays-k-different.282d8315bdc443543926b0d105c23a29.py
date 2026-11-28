
# apl-source:1
# مثال 1362 — مصفوفات جزئية بعناصر مختلفة
# apl-source:2
# Subarrays with exactly K distinct
# apl-source:3
# Demonstrates: نافذة منزلقة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1362-subarrays-k-different.apl
# apl-source:6

# apl-source:7
# العدد بالضبط ك يساوي حتى ك ناقص حتى ك ناقص واحد
# apl-source:8
# نحسب حتى ك بنافذة منزلقة
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
def حتى_ك(أرقام, ك):
  # apl-source:19
  if ك == 0:
    # apl-source:20
    return 0
  # apl-source:21
  عدّ = {}
  # apl-source:22
  يسار = 0
  # apl-source:23
  مختلف = 0
  # apl-source:24
  مجموع = 0
  # apl-source:25
  for يمين in range(len(أرقام)):
    # apl-source:26
    عدّ[أرقام[يمين]] = عدّ.get(أرقام[يمين], 0) + 1
    # apl-source:27
    if عدّ[أرقام[يمين]] == 1:
      # apl-source:28
      مختلف = مختلف + 1
    # apl-source:29
    while مختلف > ك:
      # apl-source:30
      عدّ[أرقام[يسار]] = عدّ[أرقام[يسار]] - 1
      # apl-source:31
      if عدّ[أرقام[يسار]] == 0:
        # apl-source:32
        مختلف = مختلف - 1
      # apl-source:33
      يسار = يسار + 1
    # apl-source:34
    مجموع = مجموع + يمين - يسار + 1
  # apl-source:35
  return مجموع
# apl-source:36

# apl-source:37
def بالضبط_ك(أرقام, ك):
  # apl-source:38
  return حتى_ك(أرقام, ك) - حتى_ك(أرقام, ك - 1)
# apl-source:39

# apl-source:40
تأكد_يساوي(بالضبط_ك([1,2,1,2,3], 2), 7, "سبعة")
# apl-source:41
تأكد_يساوي(بالضبط_ك([1,2,1,3,4], 3), 3, "ثلاثة")
# apl-source:42
تأكد_يساوي(بالضبط_ك([1,1], 1), 3, "كلها")
# apl-source:43
