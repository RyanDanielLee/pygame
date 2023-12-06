# How to Play

## Controls
- **Right Arrow Key:** Move Right
- **Left Arrow Key:** Move Left
- **Space Bar:** Jump

## How to Play/Restart
1. Run `game.py` to start the game.
2. Use the arrow keys to move and jump.
3. Reach the last platform to complete the level.
4. Game Over? Press SPACE to restart.

## How to Change Level
In the `constants.py` file:
- Modify the `LEVEL` variable to the path of your desired level CSV file.
  ```python
  LEVEL = "levels/Your_Level.csv"

# Project Structure
**game.py**: Main game script.

**constants.py**: Configuration file, including the level file path.

**screens/**: Contains different game screens (start, end, game).

**components/**: Components used in the game (player, level, platform).

## Screens
**Location**: components/player.py

**Description**: Represents the player character in the game.

**Velocity Handling**: Player velocity is controlled by the arrow keys. Left and right arrow keys control horizontal movement, and the space bar initiates jumping.

### Start Screen
**Location**: screens/start.py

**Description**: The initial screen that prompts the player to start the game.

**Transition**: Pressing SPACE switches to the Game Screen.

### End Screen
**Location**: screens/end.py

**Description**: Displayed upon game over or finished game, showing the player's elapsed time and prompting to restart.

**Transition**: Pressing SPACE restarts the game.

## Level
**Location**: components/level.py

**Description**: Manages the game level by loading platform data from a CSV file.

**Platform Types**: Regular platforms and end platforms. End platforms trigger the transition to the end screen.

## Platforms
**Location**: components/platform.py

**Description**: Represents a platform that the player can interact with.

**Collision Handling**: Determines how the player interacts with platforms, preventing the player from falling through and handling jumps.