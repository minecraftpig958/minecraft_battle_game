# minecraft_battle_game

A Python command-line game where you can simulate a battle between two different Minecraft mobs!


⚔️ **How to Play**

- Clone the Repository: Download or clone this repository to your local machine.

- Run the Script: Open a terminal or command prompt, navigate to the folder containing the main.py file, and run the following command:

```python
python3 main.py
```

- Choose Your Mobs: Follow the on-screen prompts to either have a random battle or choose your own mobs to fight. You can even create custom mobs with your own stats and special attacks!


✨ **Features**

- Randomized Battles: Let the program choose two random mobs and items for a surprise fight.

- Custom Selection: Pick any two mobs from the extensive list to see who would win.

- Create Your Own Mobs: Design a custom mob by setting its health, damage points, and special attacks.

- Real-time Battle Log: Watch as each turn of the battle unfolds in the console.


🔍 **Troubleshooting**

If one of the two mobs die as soon as the battle starts, it might be that 

- you chose to select your own mob, and entered one that is not in the game code

- you created a mob and set the health to 0, meaning it dies immediately


If you get an error message, it is most likely that you entered something wrong, for example, a string when it asks you for mob health.


📝 **Planned Improvements**

- Adding more mobs and items.

- Improving the special attack logic for a wider variety of battle scenarios.

- Refactoring the code to remove repetitive code and separate mob data from fighting logic.

- Displaying a warning when an unsupported mob is selected.
