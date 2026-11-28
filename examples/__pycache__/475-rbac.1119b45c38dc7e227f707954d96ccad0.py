
# apl-source:1
# مثال 475 — التحكم بالصلاحيات
# apl-source:2
# Role-based access control
# apl-source:3
# Demonstrates: أدوار وصلاحيات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/475-rbac.apl
# apl-source:6

# apl-source:7
صلاحيات = {
    # apl-source:8
    "مدير": ["قراءة", "كتابة", "حذف"],
    # apl-source:9
    "محرر": ["قراءة", "كتابة"],
    # apl-source:10
    "زائر": ["قراءة"]
# apl-source:11
}
# apl-source:12

# apl-source:13
def مسموح(دور, عمل):
    # apl-source:14
    قائمة = صلاحيات.get(دور, [])
    # apl-source:15
    return قائمة.count(عمل) > 0
# apl-source:16

# apl-source:17
print("مدير يحذف؟", مسموح("مدير", "حذف"))
# apl-source:18
print("محرر يحذف؟", مسموح("محرر", "حذف"))
# apl-source:19
print("زائر يقرأ؟", مسموح("زائر", "قراءة"))
# apl-source:20
