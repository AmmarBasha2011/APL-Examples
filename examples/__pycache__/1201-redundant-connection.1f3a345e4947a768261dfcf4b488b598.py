
# apl-source:1
# مثال 1201 — وصلة زائدة
# apl-source:2
# Redundant connection
# apl-source:3
# Demonstrates: اتحاد وبحث
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1201-redundant-connection.apl
# apl-source:6

# apl-source:7
# نوصل العقد بالتتابع باتحاد وبحث
# apl-source:8
# والحافة التي تصل عقدتين متصلتين أصلاً هي الزائدة
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
def اوجد(اب, س):
  # apl-source:19
  while اب[س] != س:
    # apl-source:20
    اب[س] = اب[اب[س]]
    # apl-source:21
    س = اب[س]
  # apl-source:22
  return س
# apl-source:23

# apl-source:24
def وصلة_زائدة(حواف):
  # apl-source:25
  اب = list(range(len(حواف) + 1))
  # apl-source:26
  for ح in حواف:
    # apl-source:27
    أ = اوجد(اب, ح[0])
    # apl-source:28
    ب = اوجد(اب, ح[1])
    # apl-source:29
    if أ == ب:
      # apl-source:30
      return ح
    # apl-source:31
    اب[أ] = ب
  # apl-source:32
  return []
# apl-source:33

# apl-source:34
تأكد_يساوي(وصلة_زائدة([[1,2],[1,3],[2,3]]), [2, 3], "مثلث")
# apl-source:35
تأكد_يساوي(وصلة_زائدة([[1,2],[2,3],[3,4],[1,4],[1,5]]), [1, 4], "مربع")
# apl-source:36
تأكد_يساوي(وصلة_زائدة([[1,2],[2,1]]), [2, 1], "مكررة")
# apl-source:37
