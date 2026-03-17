import sys
import importlib


if __name__ == "__main__":
    print("\nLOADING STATUS: Loading programs...")
    # List all modules intended to install
    packages = ["numpy", "pandas", "matplotlib", "requests"]
    modules = {}
    module_description = ""

    print("\nChecking dependencies:")
    # Try to install package by package and raise error if unsuccessfull
    for package in packages:
        try:
            module = importlib.import_module(package)
            if not module:
                raise ModuleNotFoundError
            # Add installed module to a dict
            modules[package] = module

            # Specify each module description
            if module.__name__ == "numpy":
                module_description = "Numerical Computations ready"
            elif module.__name__ == "pandas":
                module_description = "Data manipulation ready"
            elif module.__name__ == "matplotlib":
                module_description = "Visualization ready"
            elif module.__name__ == "requests":
                module_description = "Network access ready"

            # Print sucessfull message
            print(f"[OK] {module.__name__} ({module.__version__}) - "
                  f"{module_description}")

        # Print error message indentifying the failed module and exit
        except ModuleNotFoundError:
            print(f"[KO] {package} - Could not install")
            sys.exit(1)

    print("Analyzing Matrix data...")
    # Getting data using NumPy (1000 random numbers)
    data = modules["numpy"].random.normal(0, 1, 1000)
    # Structuring data for analysis using Pandas
    structured_data = modules['pandas'].DataFrame({'numbers': data})

    print(f"Processing {len(data)} data points...")
    # Calculate the mean of the 1000 numbers using Pandas's data
    avg_value = structured_data['numbers'].mean()

    print("Generating visualization...")
    # Import matplotlib.pyplot separately to create the plot
    plt = importlib.import_module("matplotlib.pyplot")
    # Plot the original signal data
    plt.plot(structured_data["numbers"])
    # Plot the rolling mean line
    plt.plot(structured_data["rolling_mean"])
    # Save the generated visualization to the current environment path
    plt.savefig("matrix_analysis.png")

    print("\nAnalysis complete!")
    print("Results saved to: matrix_analysis.png")
