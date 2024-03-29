"""
假设有n个活动，这些活动要占用同一片场地，而场地在某时刻只能供一个活动使用。
每个活动都有一个开始时间s和结束时间（题目中时间以整数表示），表示活动在[s，f)区间占用场地
问： 安排那些活动能够使该场地举办的活动个数最多


•贪心结论：最先结束的活动一定是最优解的一部分。
。证明：假设a是所有活动中最先结束的活动，b是最优解中最先结束的活动。
    。如果a=b，结论成立。
    。如果a大b，则b的结束时间一，定晚于a的结束时间，则此时用a替换掉最优解中的b，a—定不与最优解中的其他活动时问重叠，因此替换后的解也是最优解
"""
activities = [(1, 4), (3, 5), (0, 6), (5, 7), (3, 9), (5, 9), (6, 10), (8, 11), (8, 12), (2, 14), (12, 16)]
# 保证活动是按照结束时间排好序的

activities.sort(key=lambda x: x[1])


def activity_selection(a):
    res = [a[0]]
    for i in range(1, len(a)):
        # 如果当前活动的开始时间大于等于最后一个入选活动的结束时间不冲突
        if a[i][0] >= res[-1][-1]:
            res.append(a[i])
    return res


print(activity_selection(activities))