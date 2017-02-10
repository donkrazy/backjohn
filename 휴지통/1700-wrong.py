(n, k) = tuple(map(int, input().strip().split(" ")))
multi_tab = []
priority_dict = {}
problem_queue = list(map(int, input().strip().split(" ")))

for item in problem_queue:
    if item in priority_dict:
        priority_dict[item] += 1
    else:
        priority_dict[item] = 1

ordered_keys = sorted(priority_dict, key=priority_dict.get)
multi_tab_count = 0
num_unplugged = 0


def work(i):
    for key in ordered_keys:
        # 우선 순위가 가장 낮은 놈이 멀티탭에 있을 때 그놈을 뺀다
        if key in multi_tab:
            multi_tab.remove(key)
            multi_tab.append(i)
            global num_unplugged
            num_unplugged += 1
            print("unplug " + str(key) + ", becomes " + str(multi_tab))
            return
        else:
            continue

for item in problem_queue:
    if item in multi_tab:
        continue
    elif item not in multi_tab and multi_tab_count < n:
        multi_tab.append(item)
        multi_tab_count += 1
    elif item not in multi_tab and multi_tab_count is n:
        work(item)
    else:
        print("something wrong happened")
    print("plug " + str(item) + ", becomes " + str(multi_tab))

# print(num_unplugged)
