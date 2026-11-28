
# apl-source:1
# مثال 1315 — عيدان ثقاب مربع
# apl-source:2
# Matchsticks to square
# apl-source:3
# Demonstrates: رجوع
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1315-matchsticks-square.apl
# apl-source:6

# apl-source:7
# مجموع الأطوال يقبل القسمة على أربعة
# apl-source:8
# نوزع كل عود على ضلع من الأضلاع الأربعة
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
def نوزع(عيدان, ع, اضلاع, هدف):
  # apl-source:19
  if ع == len(عيدان):
    # apl-source:20
    return (اضلاع[0] == هدف) and (اضلاع[1] == هدف) and (اضلاع[2] == هدف)
  # apl-source:21
  for ض in range(4):
    # apl-source:22
    if اضلاع[ض] + عيدان[ع] <= هدف:
      # apl-source:23
      اضلاع[ض] = اضلاع[ض] + عيدان[ع]
      # apl-source:24
      ن = نوزع(عيدان, ع + 1, اضلاع, هدف)
      # apl-source:25
      اضلاع[ض] = اضلاع[ض] - عيدان[ع]
      # apl-source:26
      if ن:
        # apl-source:27
        return True
  # apl-source:28
  return False
# apl-source:29

# apl-source:30
def مربع(عيدان):
  # apl-source:31
  مج = 0
  # apl-source:32
  for س in عيدان:
    # apl-source:33
    مج = مج + س
  # apl-source:34
  if (len(عيدان) < 4) or (مج % 4 != 0):
    # apl-source:35
    return False
  # apl-source:36
  ق = sorted(عيدان)
  # apl-source:37
  ق.reverse()
  # apl-source:38
  return نوزع(ق, 0, [0, 0, 0, 0], مج // 4)
# apl-source:39

# apl-source:40
تأكد_يساوي(مربع([1,1,2,2,2]), True, "ممكن")
# apl-source:41
تأكد_يساوي(مربع([3,3,3,3,4]), False, "غير ممكن")
# apl-source:42
تأكد_يساوي(مربع([5,5,5,5]), True, "متساوية")
# apl-source:43
تأكد_يساوي(مربع([1,2,3]), False, "قليلة")
# apl-source:44
