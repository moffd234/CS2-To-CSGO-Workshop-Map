# CS2 to CSGO Workshop Map Transfer

This copies `.bin` workshop map files from CS2 and extracts them into your CSGO maps directory.

---

## Usage

### 1. Default Folder Locations

If your CS2 and CSGO Legacy folders are in the default locations on your `C:` drive, simply **double-click the `.exe`** to run the script.  

---

### 2. Non-default Folder Locations (Command Line)

If your CS2 or CSGO folders are in custom locations, run the `.exe` from Command Prompt or PowerShell and provide the appropriate flags:

| Flag           | Description |
|----------------|-------------|
| `-s` / `--src` | Path to your CS2 `730` workshop folder containing all map folders |
| `-d` / `--dst` | Path to your CSGO Legacy `maps` folder |

**Example using long flags:**

```powershell
main.exe --src "D:\SteamLibrary\steamapps\workshop\content\730" --dst "D:steamapps\common\csgo legacy\csgo\maps"