
#r- rows
#c- columns

#time complexity - O(rc) 
#space complexity- O(rc)


grid=[['W','L','W','W','W'],
      ['W','L','W','W','W'],
      ['W','W','W','L','W'],
      ['W','W','L','L','W'],
      ['L','W','W','L','L'],
      ['L','L','W','W','W']]


#Iterative code
def island_count(grid):
    visited={}
    #represent positive infinity
    min=float('inf')
    # iterating through rows and columns
    for r in range(len(grid)):
        for c in range(len(grid[0])):
           # exploring each row and column
            temp = explore(grid,r,c,visited)
            if temp>0 and temp<min:
                min=temp

    #final unique isalnds
    return min

#recursive Code
def explore(grid,r,c,visited):

    # checking bounds
    rowbound= r>=0 and r<len(grid)
    columnbound= c>=0 and c<len(grid[0])
    # when even one is false- return false will execute
    if not rowbound or not columnbound: return 0

    # checking visited nodes
    if (r,c) in visited: return 0
    visited[(r,c)]=''

    #checking W or L
    if grid[r][c] == 'W': return 0

    # if we pass all above logic. it means we are on a land so count is 1
    count=1

    #exploring all directions
    count+=explore(grid,r+1,c,visited)
    count+=explore(grid,r-1,c,visited)
    count+=explore(grid,r+1,c+1,visited)
    count+=explore(grid,r+1,c-1,visited)

    # when all the above doesnt return False this will execute
    return count


print(island_count(grid))