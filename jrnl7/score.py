import sys

if len(sys.argv) > 1:
    scores = sys.argv[1:]
    print("User provided scores:")
else:
    print("No input given - using default scores:")
    scores = ["80", "90", "75"]

scores = [eval(x) for x in scores]
total = sum(scores)
average = total / len(scores)

print("Scores:", scores)
print("Sum =", total)
print("Average =", average)
