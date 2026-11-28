
# apl-source:1
# مثال 1064 — مسار السقوط
# apl-source:2
# Minimum falling path sum
# apl-source:3
# Demonstrates: برمجة ديناميكية بالصفوف
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1064-falling-path-sum.apl
# apl-source:6

# apl-source:7
# من كل خانة ننزل للصف التالي إلى خانة مباشرة أو قطرية
# apl-source:8
# كلفة الخانة هي قيمتها مع أقل كلفة من الصف الأعلى
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
def اقل_سقوط(م):
  # apl-source:19
  ن = len(م)
  # apl-source:20
  سابق = list(م[0])
  # apl-source:21
  for ر in range(1, ن):
    # apl-source:22
    جديد = [0] * ن
    # apl-source:23
    for ك in range(ن):
      # apl-source:24
      افضل = سابق[ك]
      # apl-source:25
      if (ك > 0) and (سابق[ك - 1] < افضل):
        # apl-source:26
        افضل = سابق[ك - 1]
      # apl-source:27
      if (ك < (ن - 1)) and (سابق[ك + 1] < افضل):
        # apl-source:28
        افضل = سابق[ك + 1]
      # apl-source:29
      جديد[ك] = م[ر][ك] + افضل
    # apl-source:30
    سابق = جديد
  # apl-source:31
  افضل = سابق[0]
  # apl-source:32
  for س in سابق:
    # apl-source:33
    if س < افضل:
      # apl-source:34
      افضل = س
  # apl-source:35
  return افضل
# apl-source:36

# apl-source:37
تأكد_يساوي(اقل_سقوط([[2, 1, 3], [6, 5, 4], [7, 8, 9]]), 13, "ثلاثة في ثلاثة")
# apl-source:38
تأكد_يساوي(اقل_سقوط([[-19, 57], [-40, -5]]), -59, "اثنان في اثنين")
# apl-source:39
تأكد_يساوي(اقل_سقوط([[7]]), 7, "خلية واحدة")
# apl-source:40
