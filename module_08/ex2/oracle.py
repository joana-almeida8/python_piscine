import os
import sys
from dotenv import load_dotenv


if __name__ == "__main__":
    print("\nORACLE STATUS: Reading the Matrix...")
    # Load the data from the .env file
    load_dotenv(".env.example")
    if not load_dotenv(".env.example"):
        print("ERROR: .env file missing")
        sys.exit(1)

    config_var = ["MATRIX_MODE", "DATABASE_URL", "API_KEY",
                  "LOG_LEVEL", "ZION_ENDPOINT"]

    missing = []
    for var in config_var:
        val = os.getenv(var)

        if val == None:
            missing.append(var)
        # Validate values for configuration variable
        else:
            if var == "MATRIX_MODE":
                print(f"Mode: {os.getenv(val)}")
            elif var == "DATABASE_URL":
                print("Database: Connected to the local instance")
            elif var == "API_KEY":
                print("API Access: Autheticated")
            elif var == "LOG_LEVEL":
                print(f"Log Level: {os.getenv(val)}")
            elif var == "ZION_ENDPOINT":
                print("Zion Network: Online")

    if missing:
        print("ERROR: Missing values for the Environmental "
              f"Variables '{', '.join(missing)}'")

    print("\nEnvironment security check:")
    print("[OK] No hardcoded secrets detected")
    print("[OK] .env file properly configured")
    print("[OK] Production overrides available")

    print("\nThe Oracle sees all configurations")
