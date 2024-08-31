# Emby Player Picker

This project is a Python-based application designed to be used as an external media player option for [Emby Theatre](https://emby.media/emby-theater.html). It allows you to select from various media players via a simple command-line interface. This tool was initially created to enable the use of [Syncplay](https://syncplay.pl/) for synchronized media viewing with others, but it also provides the flexibility to select other media players when watching alone.

## Features

- **Multiple Media Player Support**: Easily choose from a list of detected media players.
- **Syncplay Compatibility**: Seamlessly integrates with Syncplay for synchronized viewing experiences.
- **Playback Resume**: Supports resuming playback on started files in some media players.
- **Simple Command-Line Interface**: User-friendly interface to select and launch your preferred media player.
- **Playback Progress**: Note that this tool cannot report playback progress back to Emby.

## Setup Instructions

To set up this external player option in Emby:

1. **Open Emby Theater**.
2. **Hit your profile button in the top right**
   - Then select "App Settings" from the drop down
4. **Navigate to External Players**:
   - Click "Add"
   - Set the **Player Path** to the application. (For example C:\Users\Jane\Documents\emby_player_picker.exe)
   - Ensure **Enable for** is ticked for at least **Video Files & Internet Streams**.
6. **Command Line Arguments**:
   - Enter the following arguments on **separate lines**:
     ```
     {path}
     {seconds}
     ```
   - Ensure that `{path}` and `{seconds}` are on separate lines to function correctly.

## Usage

1. When playing media through Emby, the external player selection interface will appear.
2. Enter the number corresponding to the media player you wish to use.
3. The selected media player will launch with the specified media file.

Enjoy your media with the flexibility of choosing your preferred media player!

## Download
Latest releases are found [here](https://github.com/JuiceyBoost/Emby-Player-Picker/releases)

## Todo
- Add config file with things such as
  - customisable settings to media players, such as launching full screen
  - The ability to set SyncPlay server/room options
- Linux Support
- ~~MacOS Support~~ Emby Theatre on MacOS doesn't support external players so this program cannot work there
- Add resume playback to more clients
- Look into ways of reporting back playback progress to Emby
