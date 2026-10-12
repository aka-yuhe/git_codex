# 导入随机数工具，用来生成随机测试数据并选择目标值。
import random
# 导入 Python 自带的单元测试框架。
import unittest

# 导入要测试的二分查找函数。
from binarySearch import binary_search


# 定义二分查找相关的测试用例集合。
class BinarySearchTests(unittest.TestCase):
    # 验证随机生成的数组中存在的目标值可以被找到。
    def test_finds_random_value_in_sorted_array(self) -> None:
        # 从 0 到 999 中随机抽取 100 个不重复整数，并按升序排列。
        values = sorted(random.sample(range(1000), 100))
        # 从已排序数组中随机选取一个一定存在的目标值。
        target = random.choice(values)

        # 调用二分查找函数，获取目标值所在的下标。
        index = binary_search(values, target)

        # 检查返回下标对应的元素确实等于目标值。
        self.assertEqual(values[index], target)

    # 验证数组中不存在的目标值会得到 -1。
    def test_returns_minus_one_when_value_is_missing(self) -> None:
        # 从 0 到 999 中随机抽取并排序 100 个不重复整数。
        values = sorted(random.sample(range(1000), 100))

        # 1000 不可能出现在上述取值范围中，检查函数返回 -1。
        self.assertEqual(binary_search(values, 1000), -1)


# 只有直接运行本文件时，才启动单元测试。
if __name__ == "__main__":
    # 执行当前文件中定义的所有测试用例。
    unittest.main()
