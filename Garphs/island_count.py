
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
    count=0
    # iterating through rows and columns
    for r in range(len(grid)):
        for c in range(len(grid[0])):
           # exploring each row and column
           if explore(grid,r,c,visited) == True:
               count+=1

    #final unique isalnds
    return count

#recursive Code
def explore(grid,r,c,visited):

    # checking bounds and r>=0 where we need to count the first row too.
    rowbound= r>=0 and r<len(grid)
    columnbound= c>=0 and c<len(grid[0])
    # when even one is false- return false will execute
    if not rowbound or not columnbound: return False

    # checking visited nodes
    if (r,c) in visited: return False
    visited[(r,c)]=''

    #checking W or L
    if grid[r][c] == 'W': return False

    #exploring all directions
    explore(grid,r+1,c,visited)
    explore(grid,r-1,c,visited)
    explore(grid,r+1,c+1,visited)
    explore(grid,r+1,c-1,visited)

    # when all the above doesnt return False this will execute
    return True


print(island_count(grid))