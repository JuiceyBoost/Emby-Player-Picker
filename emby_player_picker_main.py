import os
import sys
import subprocess
import msvcrt

def detect_media_players():
    players = []

    # Check for SyncPlay
    syncplay_path = "C:\\Program Files (x86)\\Syncplay\\Syncplay.exe"
    if os.path.exists(syncplay_path):
        players.append(('SyncPlay', syncplay_path))

    # Check for MPV (Various distributions)
    mpv_net_path = os.path.join(os.getenv('USERPROFILE'), 'AppData', 'Local', 'Programs', 'mpv.net', 'mpvnet.exe')
    if os.path.exists(mpv_net_path):
        players.append(('MPV.net', mpv_net_path))

    mpv_standalone_path = "C:\\Program Files\\mpv\\mpv.exe"
    if os.path.exists(mpv_standalone_path):
        players.append(('MPV (Standalone)', mpv_standalone_path))

    celluloid_path = "C:\\Program Files\\Celluloid\\celluloid.exe"
    if os.path.exists(celluloid_path):
        players.append(('Celluloid (MPV Frontend)', celluloid_path))

    # Check for VLC Media Player
    vlc_path = "C:\\Program Files\\VideoLAN\\VLC\\vlc.exe"
    if os.path.exists(vlc_path):
        players.append(('VLC', vlc_path))

    # Check for MPC (Media Player Classic)
    mpc_hc_path = "C:\\Program Files\\MPC-HC\\mpc-hc64.exe"
    if os.path.exists(mpc_hc_path):
        players.append(('MPC-HC', mpc_hc_path))

    mpc_be_path = "C:\\Program Files\\MPC-BE\\mpc-be64.exe"
    if os.path.exists(mpc_be_path):
        players.append(('MPC-BE', mpc_be_path))

    # Check for PotPlayer
    potplayer_path = "C:\\Program Files\\DAUM\\PotPlayer\\PotPlayerMini64.exe"
    if os.path.exists(potplayer_path):
        players.append(('PotPlayer', potplayer_path))

    # Check for ACG Player
    acgplayer_path = "C:\\Program Files\\WindowsApps\\ACGPlayer\\ACGPlayer.exe"
    if os.path.exists(acgplayer_path):
        players.append(('ACG Player', acgplayer_path))

    # Check for KMPlayer
    kmplayer_path = "C:\\Program Files (x86)\\The KMPlayer\\KMPlayer.exe"
    if os.path.exists(kmplayer_path):
        players.append(('KMPlayer', kmplayer_path))

    # Check for GOM Player
    gomplayer_path = "C:\\Program Files\\GRETECH\\GomPlayer\\GOM.exe"
    if os.path.exists(gomplayer_path):
        players.append(('GOM Player', gomplayer_path))

    # Check for BSPlayer
    bsplayer_path = "C:\\Program Files\\Webteh\\BSPlayer\\bsplayer.exe"
    if os.path.exists(bsplayer_path):
        players.append(('BSPlayer', bsplayer_path))

    # Check for SMPlayer
    smplayer_path = "C:\\Program Files\\SMPlayer\\smplayer.exe"
    if os.path.exists(smplayer_path):
        players.append(('SMPlayer', smplayer_path))

    # Check for Zoom Player
    zoomplayer_path = "C:\\Program Files\\Zoom Player\\zplayer.exe"
    if os.path.exists(zoomplayer_path):
        players.append(('Zoom Player', zoomplayer_path))

    # Check for 5KPlayer
    fivekplayer_path = "C:\\Program Files\\5KPlayer\\5KPlayer.exe"
    if os.path.exists(fivekplayer_path):
        players.append(('5KPlayer', fivekplayer_path))

    # Check for RealPlayer
    realplayer_path = "C:\\Program Files\\Real\\RealPlayer\\realplay.exe"
    if os.path.exists(realplayer_path):
        players.append(('RealPlayer', realplayer_path))

    # Check for SPlayer
    splayer_path = "C:\\Program Files\\SPlayer\\SPlayer.exe"
    if os.path.exists(splayer_path):
        players.append(('SPlayer', splayer_path))

    # Check for Kodi
    kodi_path = "C:\\Program Files\\Kodi\\kodi.exe"
    if os.path.exists(kodi_path):
        players.append(('Kodi', kodi_path))

    # Check for MediaMonkey
    mediamonkey_path = "C:\\Program Files\\MediaMonkey\\MediaMonkey.exe"
    if os.path.exists(mediamonkey_path):
        players.append(('MediaMonkey', mediamonkey_path))

    # Check for JetAudio
    jetaudio_path = "C:\\Program Files\\JetAudio\\JetAudio.exe"
    if os.path.exists(jetaudio_path):
        players.append(('JetAudio', jetaudio_path))

    # Check for foobar2000
    foobar2000_path = "C:\\Program Files\\foobar2000\\foobar2000.exe"
    if os.path.exists(foobar2000_path):
        players.append(('foobar2000', foobar2000_path))

    return players

def main():
    # Check if two arguments are provided
    if len(sys.argv) < 3:
        print("Error: First and second arguments are required.")
        sys.exit(1)

    arg1 = sys.argv[1]
    arg2 = sys.argv[2]

    # Detect available media players
    players = detect_media_players()

    if not players:
        print("Error: No supported media players found on this system.")
        sys.exit(1)

    # Display the available media players
    print("Choose a media player:")
    for i, (name, _) in enumerate(players, 1):
        print(f"{i} - {name}")

    # Read a single key press
    choice = msvcrt.getch().decode('ascii')

    try:
        choice_idx = int(choice) - 1
        if choice_idx < 0 or choice_idx >= len(players):
            raise ValueError

        player_name, player_path = players[choice_idx]

        print(f"\nOpening {player_name} with arguments: {arg1}")

        # Build command and arguments based on the chosen player
        if 'MPV' in player_name:
            subprocess.Popen([player_path, f"--start={arg2}", arg1])
        elif player_name == 'VLC':
            subprocess.Popen([player_path, arg1, f"--start-time={arg2}"])
        elif 'MPC' in player_name:
            milliseconds = int(arg2 * 1000)
            subprocess.Popen([player_path, arg1, f"/start {milliseconds}"])
        elif player_name == 'PotPlayer':
            subprocess.Popen([player_path, arg1, f"/seek={arg2}"])
        elif player_name == 'SMPlayer':
            subprocess.Popen([player_path, f"--start={arg2}", arg1])
        elif player_name == 'Zoom Player':
            subprocess.Popen([player_path, arg1, f"/seek:{arg2}"])
        else:
            subprocess.Popen([player_path, arg1])

    except ValueError:
        print("\nInvalid choice. Please select a valid option.")
        sys.exit(1)

if __name__ == "__main__":
    main()
