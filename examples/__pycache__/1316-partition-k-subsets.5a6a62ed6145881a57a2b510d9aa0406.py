
# apl-source:1
# مثال 1316 — تقسيم إلى k مجموعات
# apl-source:2
# Partition to k equal sum subsets
# apl-source:3
# Demonstrates: رجوع
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1316-partition-k-subsets.apl
# apl-source:6

# apl-source:7
# الهدف مجموع الكل على k
# apl-source:8
# نملأ كل مجموعة بالعناصر الأكبر أولاً
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
def املأ(أ, ع, مجاميع, هدف):
  # apl-source:19
  if ع == len(أ):
    # apl-source:20
    return True
  # apl-source:21
  جرب = []
  # apl-source:22
  for ك in range(len(مجاميع)):
    # apl-source:23
    if (مجاميع[ك] + أ[ع] <= هدف) and (مجاميع[ك] not in جرب):
      # apl-source:24
      جرب = جرب + [مجاميع[ك]]
      # apl-source:25
      مجاميع[ك] = مجاميع[ك] + أ[ع]
      # apl-source:26
      ن = املأ(أ, ع + 1, مجاميع, هدف)
      # apl-source:27
      مجاميع[ك] = مجاميع[ك] - أ[ع]
      # apl-source:28
      if ن:
        # apl-source:29
        return True
  # apl-source:30
  return False
# apl-source:31

# apl-source:32
def يقسم_ك(أ, ك):
  # apl-source:33
  مج = 0
  # apl-source:34
  for س in أ:
    # apl-source:35
    مج = مج + س
  # apl-source:36
  if مج % ك != 0:
    # apl-source:37
    return False
  # apl-source:38
  ق = sorted(أ)
  # apl-source:39
  ق.reverse()
  # apl-source:40
  if ق[0] > مج // ك:
    # apl-source:41
    return False
  # apl-source:42
  return املأ(ق, 0, [0] * ك, مج // ك)
# apl-source:43

# apl-source:44
تأكد_يساوي(يقسم_ك([4,3,2,3,5,2,1], 4), True, "أربع مجموعات")
# apl-source:45
تأكد_يساوي(يقسم_ك([1,2,3,4], 3), False, "لا يقسم")
# apl-source:46
تأكد_يساوي(يقسم_ك([2,2,2,2,3,4,5], 4), False, "سبعة عناصر")
# apl-source:47
تأكد_يساوي(يقسم_ك([1,1,1,1], 2), True, "اثنتان")
# apl-source:48
