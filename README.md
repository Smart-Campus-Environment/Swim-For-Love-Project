# *Swim For Love* Lap Counter

A project for counting laps and displaying a leaderboard for the Swim For Love event.


# Demo
![GIF of demonstration](https://github.com/Smart-Campus-Environment/Swim-For-Love-Project/blob/master/assets/demo.gif)

# Functionalities

1. Swimmer as an Object
2. Add Swimmer
3. Update stat_all.json
4. Update stat.json of each swimmer
5. Save Function
5. Read from Save Function


# To-Do's

1. Read from RFID Reader
2. Check swimmer status
3. Individual Swimmer Stat Page
4. Certificate HTML5 Page
5. Playground_Auth HTML5 Page
6. Milestone Congrats

# How to Run

1. Clone this repository under your web server directory.

```git clone https://github.com/Smart-Campus-Environment/Swim-For-Love-Project.git```

2. `cd` to your web server directory.

3. Run `python3 back-end/back-end.py -n`, the option `-n` lets the Python script generate a new data, if you want to use existing data, ignore the `-n` option, and just do `python3 back-end/back-end.py`

4. In the browser, open `localhost/Swim-For-Love-Project`.

5. To stop the demo, simply do `Ctrl + c` in the terminal, your data will be automatically saved to `Swimmer_Database.pickle` for you to use next time.
