import json

def connected(start, end, dungeon_map, visited) :
    cur_cave = start
    #with open("visited.txt","w") as f:
    while True :
        #f.write(json.dumps(visited,indent=4))
        if end in dungeon_map[cur_cave] :
            return True
    
        for connected_cave in dungeon_map[cur_cave] :
            if not visited[connected_cave] :
                visited[connected_cave] = True
                cur_cave = connected_cave
                break
    
        else :
            return False

# initialize a map with empty dictionary
dungeon_map = {}

# read and fill connections between caves
words = input().split()
while len(words) == 2:
    first_cave, second_cave = words

    conn_to_first = dungeon_map.get(first_cave, [])
    if second_cave not in conn_to_first:
        dungeon_map[first_cave] = conn_to_first + [second_cave]

    conn_to_second = dungeon_map.get(second_cave, [])
    if first_cave not in conn_to_second:
        dungeon_map[second_cave] = conn_to_second + [first_cave]
    
    words = input().split()

#with open("1.txt","w") as f :
#    f.write(json.dumps(dungeon_map, indent=4))

# read starting and endig caves
start = words[0]
end   = input()

# initialize dictionary of vizited caves with Falses
visited = {cave : False for cave in dungeon_map}
visited[start] = True

print('YES') if connected(start, end, dungeon_map, visited) else print('NO')