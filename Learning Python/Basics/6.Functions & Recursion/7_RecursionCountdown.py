def countdown(n):
    if n == 0:           # Base case
        print("Done!")
        return

    print(n)
    countdown(n - 1)     # Recursive call

countdown(5)


# countdown(5)
# │
# ├── print(5)
# └── countdown(4)
#       │
#       ├── print(4)
#       └── countdown(3)
#             │
#             └── ...
#                   │
#                   └── countdown(0)
#                         │
#                         └── Done!