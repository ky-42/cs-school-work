##
# Recursive function that takes a list of actions and returns
# the number of chests the player went trough. Also tests function.
##

def rerecursed(actionList, chests=0):
  # Base cases
  if len(actionList) <= 0 or actionList[0][-4:] == "Goal":
    return chests

  return rerecursed(actionList[1:], chests+1)

def main():
  actionList = ["Walk", "Walk. Jump", "Swim. Leave Water. Goal", "Jump.", "Walk."]

  chests = rerecursed(actionList)

  print(f"The player entered {chests} chests.")

if __name__ == "__main__":
  main()