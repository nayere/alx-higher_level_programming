#!/usr/bin/python3

if __name__ == "__main__":
    """Print the value of variable a from variable_load_5."""
    try:
        from variable_load_5 import a
        print(a)
    except ImportError as e:
        print(f"Error: {e}. Unable to import variable a from variable_load_5.")
