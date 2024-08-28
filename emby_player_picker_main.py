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

    # Check for LAV Filter Megamix MPC and PotPlayer
    lav_mpc_x64_path = "C:\\Program Files (x86)\\LAV Filters\\x64\\mpc-hc\\shoukaku.exe"
    if os.path.exists(lav_mpc_x64_path):
        players.append(('LAV Megamix MPC-HC (x64)', lav_mpc_x64_path))

    lav_mpc_x32_path = "C:\\Program Files (x86)\\LAV Filters\\x32\\mpc-hc\\shoukaku.exe"
    if os.path.exists(lav_mpc_x32_path):
        players.append(('LAV Megamix MPC-HC (x32)', lav_mpc_x32_path))

    lav_potplayer_x64_path = "C:\\Program Files (x86)\\LAV Filters\\x64\\PotPlayer\\zuikaku.exe"
    if os.path.exists(lav_potplayer_x64_path):
        players.append(('LAV Megamix PotPlayer (x64)', lav_potplayer_x64_path))

    lav_potplayer_x32_path = "C:\\Program Files (x86)\\LAV Filters\\x32\\PotPlayer\\zuikaku.exe"
    if os.path.exists(lav_potplayer_x32_path):
        players.append(('LAV Megamix PotPlayer (x32)', lav_potplayer_x32_path))

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

    media_url = sys.argv[1] # HLS Stream URL from Emby/Jellyfin
    seconds = sys.argv[2] # Resume time measured in Seconds
    
    # Convert Seconds into milliseconds for relevant players
    milliseconds = int(seconds) * 1000

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

        print(f"\nOpening {player_name}")
        

        # Build command and arguments based on the chosen player
        if 'MPV' in player_name:
            print(f"\nOpening: {player_path} --start={seconds} {media_url}")
            subprocess.Popen([player_path, f"--start={seconds}", media_url])
            
        elif player_name == 'VLC':
            print(f"\nOpening: {player_path} {media_url} --start-time={seconds}")
            subprocess.Popen([player_path, media_url, f"--start-time={seconds}"])
            
        elif 'PotPlayer' in player_name:
            print(f"\nOpening: {player_path} {media_url} /seek {seconds}")
            subprocess.Popen([player_path, media_url, f"/seek={seconds}"])
            
        elif player_name == 'SMPlayer':
            print(f"\nOpening: {player_path} --start={seconds} {media_url}")
            subprocess.Popen([player_path, f"--start={seconds}", media_url])
            
        #Disabled MPC custom arguments for now as adding arguments beyond media_url causes "unknown switches" error in MPC
        #elif 'MPC' in player_name:
        #    print(f"\nOpening: {player_path} {media_url} /start {milliseconds}")
        #    subprocess.Popen([player_path, f'"{media_url}"', f"/start {seconds}"])
        
        else:
            print(f"\nOpening: {player_path} {media_url}")
            subprocess.Popen([player_path, media_url])

    except ValueError:
        print("\nInvalid choice. Please select a valid option.")
        sys.exit(1)

if __name__ == "__main__":
    main()
