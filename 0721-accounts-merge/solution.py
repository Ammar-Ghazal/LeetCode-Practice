class Solution:
    def accountsMerge(self, accounts: list[list[str]]) -> list[list[str]]:
        # Time complexity: O(NK log NK), N -> no of accounts, K -> max account length
        # Space complexity: O(NK)
        graph = defaultdict(set)
        emailToName = {}

        # create the graph, nodes point both ways for easy access either way
        for account in accounts:
            name = account[0]

            for email in account[1:]:
                graph[email].add(account[1]) # add only the first email
                graph[account[1]].add(email)

                emailToName[email] = name

        out = []
        visited = set() # to ensure we dont get stuck in an infinite loop

        # visit each email in the graph at least once
        for email in graph:
            if email not in visited:
                stack = [email]
                visited.add(email)

                mergedEmails = []

                # dfs: we can also use bfs with a queue
                # dfs/bfs necessary to help find deeper connections, if these are emails:
                # a: b
                # b: a, c
                # c: b
                # only way to know that c is connected to a is to use bfs/dfs to discover these deeper connections
                while stack:
                    node = stack.pop()
                    mergedEmails.append(node)

                    # go through all connecting nodes and add if they havent been visited yet
                    for neighbor in graph[node]:
                        if neighbor not in visited:
                            stack.append(neighbor)
                            visited.add(neighbor)
                
                # add the email list to the name and make sure its sorted, because the problem description required it
                out.append([emailToName[email]] + sorted(mergedEmails))
        
        return out


