# Ham-Ham Games Save Editor
Some scripts and a graphic user interface to edit saves from the GBA game Hamtaro: Ham-Ham Games.

## Currently Supported Features

### User Interface

- Set seeds count
- Set current location (currently just a number)
- Set current language (currently just a number)
- Set completion flags for the minigames (9999 score)
- Set any general message (Greeting, favorite phrase, favorite food, ...)

- Set all best scores and world records

- Set G/S/B medals count for each team
- Set the results (currently it doesn't affect the winner if you are after the marathon)

- Set/remove any obtained costume

- Set/remove any obtained hamigo card

- Set all the attributes of the Player Card (even the year of birth which is not used after you set it)
- Set all the attributes of the Friend Cards (even the year of birth which is not used at all)
- Export Player Card/Friend Card
- Add an empty Friend Card to the list
- Delete a Friend Card
- Import a Friend Card from file (there are some samples of event cards in "res/Cards")

### Scripts

- Nearly anything you can do with the GUI, but with less restrictions and more possibilities (e.g. automated tests)

## Planned Features

- Add color support any text (general messages, friend cards names and messages, ...).
- Add descriptive names for locations and languages
- Find and add more event flags
- Find and add tournament event results
- Add multi-language support for the GUI
