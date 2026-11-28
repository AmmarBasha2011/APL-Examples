
# apl-source:1
# مثال 2074 — تعبئة منطقة في صورة بدلو الطلاء
# apl-source:2
# Flood fill paint bucket
# apl-source:3
# Demonstrates: شبكات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2074-flood-fill-image-paint-bucket-stack.apl
# apl-source:6

# apl-source:7
# # نستخدم مكدسا بدل التكرار
# apl-source:8
# # نغير اللون عند الزيارة فلا نكرر
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
def املأ(صورة, ص, س, جديد):
  # apl-source:19
  قديم = صورة[ص][س]
  # apl-source:20
  if قديم == جديد:
    # apl-source:21
    return صورة
  # apl-source:22
  مكدس = [[ص, س]]
  # apl-source:23
  while len(مكدس) > 0:
    # apl-source:24
    خ = مكدس.pop()
    # apl-source:25
    if خ[0] >= 0 and خ[0] < len(صورة) and خ[1] >= 0 and خ[1] < len(صورة[0]):
      # apl-source:26
      if صورة[خ[0]][خ[1]] == قديم:
        # apl-source:27
        صورة[خ[0]][خ[1]] = جديد
        # apl-source:28
        مكدس = مكدس + [[خ[0] + 1, خ[1]], [خ[0] - 1, خ[1]], [خ[0], خ[1] + 1], [خ[0], خ[1] - 1]]
  # apl-source:29
  return صورة
# apl-source:30

# apl-source:31
تأكد_يساوي(املأ([[1, 1, 1], [1, 1, 0], [1, 0, 1]], 1, 1, 2), [[2, 2, 2], [2, 2, 0], [2, 0, 1]], "كلاسيكي")
# apl-source:32
تأكد_يساوي(املأ([[0, 0]], 0, 0, 0), [[0, 0]], "نفس اللون")
# apl-source:33
