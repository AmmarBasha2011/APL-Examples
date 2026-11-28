
# apl-source:1
# مثال 982 — المسار الهاملتوني
# apl-source:2
# Hamiltonian path
# apl-source:3
# Demonstrates: تراجع عودي بعلامات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/982-hamiltonian-path.apl
# apl-source:6

# apl-source:7
# المسار الهاملتوني: زيارة كل عقدة مرة واحدة بالتراجع العودي
# apl-source:8
# يمر بكل رأس دون اشتراط العودة إلى البداية
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
جوار = [[1, 2], [0, 2, 3], [0, 1, 3, 4], [1, 2, 4], [2, 3]]
# apl-source:19
مسار = [0, -1, -1, -1, -1]
# apl-source:20
عمق = [1]
# apl-source:21
مستخدم = [1, 0, 0, 0, 0]
# apl-source:22
وجد = [0]
# apl-source:23

# apl-source:24
def تتبع(عقدة):
  # apl-source:25
  if عمق[0] == 5:
    # apl-source:26
    وجد[0] = 1
    # apl-source:27
    return 0
  # apl-source:28
  for جار in جوار[عقدة]:
    # apl-source:29
    if (مستخدم[جار] == 0) and (وجد[0] == 0):
      # apl-source:30
      مسار[عمق[0]] = جار
      # apl-source:31
      عمق[0] = عمق[0] + 1
      # apl-source:32
      مستخدم[جار] = 1
      # apl-source:33
      تتبع(جار)
      # apl-source:34
      if وجد[0] == 0:
        # apl-source:35
        عمق[0] = عمق[0] - 1
        # apl-source:36
        مسار[عمق[0]] = -1
        # apl-source:37
        مستخدم[جار] = 0
  # apl-source:38
  return 0
# apl-source:39

# apl-source:40
تتبع(0)
# apl-source:41
تأكد_يساوي(وجد[0], 1, "مسار موجود")
# apl-source:42
تأكد_يساوي(مسار[0], 0, "البداية")
# apl-source:43
تأكد_يساوي(مسار[1], 1, "الثانية")
# apl-source:44
تأكد_يساوي(مسار[4], 4, "النهاية")
# apl-source:45
مجموع = 0
# apl-source:46
for عقدة in مسار:
  # apl-source:47
  مجموع = مجموع + عقدة
# apl-source:48
تأكد_يساوي(مجموع, 10, "كل عقدة مرة واحدة")
# apl-source:49
