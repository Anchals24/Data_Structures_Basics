def sum_of_last_nodes(self, M):
        N = self.length()
        temp = self.head
        pt = 1
        sum = 0
        #iprint("Hi")
        while(temp):
            diff = N - M
            if (pt <= diff):
                temp = temp.next
                pt += 1
            else:
                sum = sum + temp.data
                temp = temp.next
                pt += 1
        print(sum)