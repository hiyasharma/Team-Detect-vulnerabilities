import winreg

def main():
    subkey_path = r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\Google Chrome"

    try:
        subkey_hkey = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, subkey_path)
        value, reg_type = winreg.QueryValueEx(subkey_hkey, "DisplayName")

        if reg_type == winreg.REG_SZ or reg_type == winreg.REG_EXPAND_SZ:
            print(f"Value of 'DisplayName':")
            print(value)
        else:
            print("Value type of 'DisplayName' is not REG_SZ or REG_EXPAND_SZ.")
    except FileNotFoundError:
        print(f"Key '{subkey_path}' not found.")

if __name__ == "__main__":
    main()
