# 定义二分查找函数，接收已升序排列的整数列表和要查找的目标值。
def binary_search(values: list[int], target: int) -> int:
    """返回目标值在有序列表中的下标；如果目标值不存在则返回 -1。"""
    # 左边界从列表第一个元素开始。
    left = 0
    # 右边界从列表最后一个元素开始。
    right = len(values) - 1

    # 当左右边界没有交错时，搜索范围内仍可能存在目标值。
    while left <= right:
        # 取当前搜索区间的中间下标。
        middle = (left + right) // 2

        # 如果中间元素就是目标值，返回它的下标。
        if values[middle] == target:
            return middle
        # 如果中间元素比目标值小，目标只可能在右半边。
        if values[middle] < target:
            # 将左边界移到中间位置的右侧，排除已经检查过的元素。
            left = middle + 1
        # 否则目标只可能在左半边。
        else:
            # 将右边界移到中间位置的左侧，排除已经检查过的元素。
            right = middle - 1

    # 搜索区间已经为空，说明列表中没有目标值。
    return -1
