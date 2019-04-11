'''
广度优先搜索

假设你经营着一个芒果农场，需要寻找芒果销售商，以便将芒果卖给他。
为此，你可在朋友中查找。假设你没有朋友是芒果销售商，那么你就必须在朋友的朋友中查找。
使用这种算法将搜遍你的整个人际关系网，直到找到芒果销售商。
'''
from collections import deque


def search(graph, name):
    search_queue = deque()
    search_queue += graph[name]
    # 这个数组用来记录检查过的人
    searched = []

    # 只要队列不为空
    while search_queue:
        # 取出其中的第一个人
        person = search_queue.popleft()
        # 如果此人没有检查过
        if not person in searched:
            if person_is_seller(person):
                print(person + " is a mango seller. ")
                return True
            else:
                # 不是芒果经销商，将此人的朋友都加入搜索队列
                search_queue += graph[person]
                # 将此人标记为检查过
                searched.append(person)
    # 到达这里说明没有人是芒果经销商
    return False


# 判断是否是芒果经销商
def person_is_seller(name):
    print(name)
    return name[-1] == 'm'


if __name__ == "__main__":
    # 准备关系图
    graph = {}
    graph["you"] = ["alice", "bob", "claire"]
    graph["bob"] = ["anuj", "peggy"]
    graph["alice"] = ["peggy"]
    graph["claire"] = ["thom", "jonny"]
    graph["anuj"] = []
    graph["peggy"] = []
    graph["thom"] = []
    graph["jonny"] = []

    search(graph, "you")
