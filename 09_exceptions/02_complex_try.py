def serve_burger(type):
    try:
        print(f"Preparing {type} Burger")
        if type == "unknown":
            raise ValueError("we don't about that burger")
    except ValueError as e:
        print("Error:", e)
    else:
        print(f"{type} burger is served")
    finally:
        print("Next Customer Please...")

serve_burger("Veggi")
serve_burger("unknown")