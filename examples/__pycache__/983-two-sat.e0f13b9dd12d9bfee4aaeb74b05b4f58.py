
# apl-source:1
# مثال 983 — قابلية إرضاء 2-SAT
# apl-source:2
# 2-SAT satisfiability
# apl-source:3
# Demonstrates: تقييم قوارض بحدين
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/983-two-sat.apl
# apl-source:6

# apl-source:7
# قابلية إرضاء 2-SAT: صيغة عطفية بحدين في كل قوس
# apl-source:8
# بحث شامل على التعيينات مع تقييم قوس قوساً
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
def يحقق(قناع, قائمة):
  # apl-source:19
  ق = []
  # apl-source:20
  for i in range(3):
    # apl-source:21
    ق = ق + [(قناع >> i) & 1]
  # apl-source:22
  for قوس in قائمة:
    # apl-source:23
    if ق[قوس[0] - 1] != قوس[1]:
      # apl-source:24
      if ق[قوس[2] - 1] != قوس[3]:
        # apl-source:25
        return 0
  # apl-source:26
  return 1
# apl-source:27

# apl-source:28
قوارض = [[1, 1, 2, 1], [1, 0, 3, 1], [2, 0, 3, 0], [1, 1, 3, 0]]
# apl-source:29
عدد = 0
# apl-source:30
قناع_حل = -1
# apl-source:31
for قناع in range(8):
  # apl-source:32
  if يحقق(قناع, قوارض) == 1:
    # apl-source:33
    عدد = عدد + 1
    # apl-source:34
    قناع_حل = قناع
# apl-source:35

# apl-source:36
تأكد_يساوي(عدد, 2, "حلان ممكنان")
# apl-source:37
تأكد_يساوي(قناع_حل, 5, "آخر تعيين محقق")
# apl-source:38
تأكد_يساوي(يحقق(2, قوارض), 1, "التعيين الأول يحقق")
# apl-source:39
تأكد_يساوي(يحقق(5, قوارض), 1, "التعيين الثاني يحقق")
# apl-source:40
تأكد_يساوي(يحقق(0, قوارض), 0, "الصفر لا يحقق")
# apl-source:41

# apl-source:42
# صيغة غير قابلة: (س1 أو س1) و (ليس س1 أو ليس س1)
# apl-source:43
مستحيلة = [[1, 1, 1, 1], [1, 0, 1, 0]]
# apl-source:44
عدد2 = 0
# apl-source:45
for قناع in range(8):
  # apl-source:46
  if يحقق(قناع, مستحيلة) == 1:
    # apl-source:47
    عدد2 = عدد2 + 1
# apl-source:48
تأكد_يساوي(عدد2, 0, "صيغة مستحيلة")
# apl-source:49
