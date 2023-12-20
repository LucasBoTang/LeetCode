class Solution(object):
    def timeTaken(self, arrival, state):
        """
        :type arrival: List[int]
        :type state: List[int]
        :rtype: List[int]
        """
        # init
        t = 0
        prev_s = 1
        queues = [[], []]
        res = [-1] * len(arrival)
        # start loop
        for i, (a, s) in enumerate(zip(arrival, state)):
            # clear queues util t
            while t < a:
                # same as previous state
                if queues[prev_s]:
                    res[queues[prev_s].pop(0)] = t
                # different state
                elif queues[~prev_s]:
                    res[queues[~prev_s].pop(0)] = t
                    prev_s = ~prev_s
                # no arriving
                else:
                    prev_s = 1
                # update time
                t += 1
            queues[s].append(i)
        # remaining queue
        while any(queues):
            # same as previous state
            if queues[prev_s]:
                res[queues[prev_s].pop(0)] = t
            # different state
            else:
                res[queues[~prev_s].pop(0)] = t
                prev_s = ~prev_s
            # update time
            t += 1
        return res
