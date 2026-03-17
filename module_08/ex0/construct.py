import sys
import os
import site


if __name__ == "__main__":
    # If prefix is different than the base_prefix,
    # it means that we are in the virtual env,
    # or else the prefixes would be the same
    status = "Welcome to the construct"
    if sys.prefix == sys.base_prefix:
        status = "You're still plugged in"
    print(f"\nMATRIX STATUS: {status}")

    print(f"\nCurrent Python: {sys.executable}")

    # We try to check if the prefixes are the same and raise valueerror if so,
    # else, print path to the virtual venv with success message.
    try:
        if sys.prefix == sys.base_prefix:
            raise ValueError()
        virtual_env = os.path.basename(sys.prefix)
        print(f"Virtual Environment: {virtual_env}")
        print(f"Environment Path: {sys.prefix}")
        print("\nSUCCESS: You're in an isolated environment!"
              "\nSafe to install packages without affecting"
              "\nthe global system.")
        print(f"\nPackage installation path:\n{site.getsitepackages()[0]}")

    # If it turns out that we verify that the prefixes are the same,
    # this will trigger the exception and print the warning with instructions
    # on how to create and activate the env.
    except ValueError:
        print(f"Virtual Environment: None detected")
        print("\nWARNING: You're in the global environment!")
        print("The machines can see everything you install.")

        print("\nTo enter the construct, run:")
        print("python -m venv matrix_env")
        print("source matrix_env/bin/activate # on Unix")
        print("matrix_env")
        print("Scripts")
        print("activate   # On Windows")

        print("\nThen run this program again.")

