import argparse
from password_module import generate_password, estimate_strength

def parse_args():
    p = argparse.ArgumentParser(description="Password Generator")
    p.add_argument("-l", "--length", type=int, default=12, help="Password length")
    p.add_argument("--no-upper", action="store_true", help="Exclude uppercase letters")
    p.add_argument("--no-lower", action="store_true", help="Exclude lowercase letters")
    p.add_argument("--no-digits", action="store_true", help="Exclude digits")
    p.add_argument("--no-symbols", action="store_true", help="Exclude symbols")
    return p.parse_args()

def main():
    args = parse_args()

    try:
        pwd = generate_password(
            length=args.length,
            use_upper=not args.no_upper,
            use_lower=not args.no_lower,
            use_digits=not args.no_digits,
            use_symbols=not args.no_symbols
        )
    except ValueError as e:
        print("Error:", e)
        return

    strength = estimate_strength(pwd)

    print("\nGenerated Password:", pwd)
    print("Strength:", strength)

if __name__ == "__main__":
    main()
