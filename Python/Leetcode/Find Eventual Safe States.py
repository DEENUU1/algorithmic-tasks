from enum import Enum

class State(Enum):
    init = 0
    visiting = 1
    visited = 2

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        states = [State.init] * len(graph)


        def has_cycle(u: int) -> bool:
            if states[u] == State.visiting:
                return True
            elif states[u] == State.visited:
                return False

            states[u] = State.visiting
            if any(has_cycle(v) for v in graph[u]):
                return True
            states[u] = State.visited

        return [i for i in range(len(graph)) if not has_cycle(i)]