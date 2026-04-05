'''
highest frequent task = needs to be picked first
you can track how many more tries each task is awaiting --> pick the one with lowest wait


["A","A","A","B","C"], n = 3

A = 3, B = 3, C = 1


A B C _ A B 


'''
class Solution:
    def remainingTasks(self, remaining_tasks):
        remains = [task for (task, remaining) in remaining_tasks.items() if remaining > 0]
        return len(remains)

    def leastInterval(self, tasks: List[str], n: int) -> int:
        remaining_tasks = {}
        waiting_count = {}
        for task in tasks:
            remaining_tasks[task] = 1 + remaining_tasks.get(task, 0)
            waiting_count[task] = 0
    
        waiting_tasks = []

        for task_key in remaining_tasks.keys():
            heapq.heappush(waiting_tasks, (-remaining_tasks[task_key], 0, task_key))
        
        task_order = []

        while self.remainingTasks(remaining_tasks) > 0:
            if len(waiting_tasks) > 0:
                (total, waiting, next_task) = waiting_tasks[0]
                if waiting_count[next_task] == 0:
                    (total, waiting, next_task) = heapq.heappop(waiting_tasks)
                    task_order.append(next_task)
                    waiting_count[next_task] = n+1
                    remaining_tasks[next_task] = remaining_tasks.get(next_task, 0) - 1
                    # if remaining_tasks.get(next_task, 0)  > 0:
                    #     heapq.heappush(waiting_tasks, (-remaining_tasks.get(next_task, 0), len(task_order), next_task))
                else:
                    task_order.append('')
            else:
                task_order.append('')

            for t in waiting_count.keys():
                if waiting_count[t] == 1:
                    if remaining_tasks.get(t, 0)  > 0:
                        heapq.heappush(waiting_tasks, (-remaining_tasks.get(t, 0), len(task_order), t))

            for t in waiting_count.keys():
                if waiting_count[t] != 0:
                    waiting_count[t]-=1
               

            # print('remain:', remaining_tasks)
            # print('waiting:', waiting_tasks)
            # print('count: ', waiting_count)
            # print(task_order)
            # print()


        print(task_order)
        return len(task_order)

