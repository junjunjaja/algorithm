def solution(dist):
    answer = [[]]
    return answer


dist = [[0,5,2,4,1],[5,0,3,9,6],[2,3,0,6,3],[4,9,6,0,3],[1,6,3,3,0]]
0 4 2 3 1
1 2 0 4 3
0 4 2 3 1





def solution(grid):
    answer = -1
    return answer
grid = ["??b", "abc", "cc?"]

def is_right(grid):
    col_len = len(grid[0])
    row_len = len(grid)
    coord = list(map(list,grid))
    poss = {'a':set(),'b':set(),'c':set()}
    temp_map = coord.copy()

    st_id = (0,0)
    new_map = [[0]*col_len]*row_len
    st = new_map[st_id[0]][st_id[1]]ㄱ
    for rid in range(row_len):
        for cid in range(col_len):
            next = temp_map[rid][cid]
            if next == '?':
                if st != '?':
                    new_map[rid][cid] = next
            else:
                if st == '?':
                    st = next
                    new_map[st_id[0]][st_id[1]] = next
            st_id = [rid,cid]
