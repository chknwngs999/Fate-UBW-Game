# Changelog
All notable changes for this project will be logged in the file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

## [Unreleased]
 - Follow [Semantic Versionin](https://semver.org/)
 - Convert code from FP to OOP
 - Change window scaling to be more enjoyable
 - Scale ALL assets with window size?
 - Remove unused mp3 files, use other wav files
 - Move other functions into classes? (is it fine to have some FP?)

## [0.0.8] - 2021-08-04
### ADDED
 - Created assets folder
 - Added LEMONMILK font
### CHANGED
 - Moved art_prototypes folder into log folder
 - Updated gitignore to match updated file structure
 - Moved art and audio folders into assets folder
 - Updated references to audio and art files in main.py to match updated file structure
### DEPRECATED
### REMOVED
### FIXED
### SECURITY

## [0.0.7] - 2021-08-03
### ADDED
 - Added mp3 and wav file for new song
 - Added wav file for existing bgm
### CHANGED
### DEPRECATED
### REMOVED
### FIXED
 - Changed code to play wav files instead of mp3 file. mp3 files don't work with pygame but wav files do.
### SECURITY

## [0.0.6] - 2021-08-03
### ADDED
 - Added code to scale window size to screen size
 - Scaled all positions and some assets with window size
 - Slightly randomized spawn rate
### CHANGED
### DEPRECATED
### REMOVED
### FIXED
### SECURITY

## [0.0.5] - 2021-07-29
### ADDED
### CHANGED
 - Changed display for level, time, and score
 - Replaced timer with tick checking every loop to spawn weapons
### DEPRECATED
### REMOVED
 - Removed use of pygame.time.set_timer and new USEREVENT for spawning weapons
### FIXED
### SECURITY

## [0.0.4] - 2021-07-29
### ADDED
 - Added code to generate random character for each weapon, display it with the weapon, and remove itself and corresponding weapon when typed.
 - Changed random module import
 - Changed random module references to match updated import statement
### CHANGED
### DEPRECATED
### REMOVED
 - Removed commented out obstacle movement in code
 - Removed other commented out code no longer being used
### FIXED
### SECURITY

## [0.0.3] - 2021-07-29
### ADDED
### CHANGED
 - Reorgranized log files into a single folder
 - Updated gitignore to ignore log folder
### DEPRECATED
### REMOVED
### FIXED
### SECURITY

## [0.0.2] - 2021-07-28
### ADDED
### CHANGED
 - Minor updates to README.md
 - Renamed assets folder
 - Changed assets references in main.py to match new folder name.
### DEPRECATED
### REMOVED
### FIXED
### SECURITY

## [0.0.1] - 2021-07-28
### ADDED
 - Added instructions.txt for how to play the game.
 - Pushed initial playable game version.
 - Created empty README.md
 - Added several assets (sprites, image, and bgm) for game.
### CHANGED
### DEPRECATED
 - Commented out obstacle movement - moved from main code to function
### REMOVED
### FIXED
### SECURITY