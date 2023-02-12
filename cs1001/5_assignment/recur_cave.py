##
# A recursive function that given a map and starting coords
# will figure out if there is a way to the end of the cave
# returning a bool. Also includes tests for said function.
##

def caveExit(map, x, y):
  # If in open space places bread crumb and checks all spaces around it
  # for an exit
  if map[y][x] == " ":
    map[y][x] = "*"
    return caveExit(map, x, y+1) or caveExit(map, x, y-1) or caveExit(map, x+1, y) or caveExit(map, x-1, y)
  
  # Checks if at exit
  elif map[y][x] == "E":
    return True
  
  # returns if at wall or breadcrumb
  return False

def main():
  cave_map = [['W','W','W','W','W','W','W'],\
    ['W',' ',' ',' ','W','W','W'],\
    ['W',' ','W',' ',' ','W','W'],\
    ['W',' ','W','W',' ','W','W'],\
    ['W',' ','W','W',' ',' ','W'],\
    ['W',' ','W','W','W',' ','W'],\
    ['W',' ',' ','W','W',' ','W'],\
    ['W',' ',' ',' ',' ',' ','E'],\
    ['W','W','W','W','W','W','W']]
    
  canExit = caveExit(cave_map, 1, 1)

  if canExit:
    print("A path can be found.")
  else:
    print("A path can not be found")

if __name__ == "__main__":
  main()