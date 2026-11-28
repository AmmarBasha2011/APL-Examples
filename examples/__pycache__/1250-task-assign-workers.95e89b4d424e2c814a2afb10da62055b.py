
# apl-source:1
# مثال 1250 — إسناد المهام
# apl-source:2
# Assign tasks to workers greedy
# apl-source:3
# Demonstrates: جشع
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1250-task-assign-workers.apl
# apl-source:6

# apl-source:7
# نرتب المهام والعمال
# apl-source:8
# وكل مهمة تذهب لأضعف عامل يقدر عليها
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
def اسند(مهام, عمال):
  # apl-source:19
  م = sorted(مهام)
  # apl-source:20
  ع = sorted(عمال)
  # apl-source:21
  منجز = 0
  # apl-source:22
  ي = 0
  # apl-source:23
  for قدرة in ع:
    # apl-source:24
    if (ي < len(م)) and (م[ي] <= قدرة):
      # apl-source:25
      منجز = منجز + 1
      # apl-source:26
      ي = ي + 1
  # apl-source:27
  return منجز
# apl-source:28

# apl-source:29
تأكد_يساوي(اسند([1,2,3], [1,1]), 1, "عاملان")
# apl-source:30
تأكد_يساوي(اسند([1,2,3], [3,2,1]), 3, "الكل")
# apl-source:31
تأكد_يساوي(اسند([5,6], [1,2]), 0, "لا أحد")
# apl-source:32
تأكد_يساوي(اسند([], [1]), 0, "لا مهام")
# apl-source:33
