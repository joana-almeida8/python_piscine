import sys


if __name__ == "__main__":
    print("=== Player Score Analytics ===")
    scores = []
    if len(sys.argv) == 1:
        print("No scores provided. Usage: "
              "python3 ft_score_analytics.py <score1> <score2> ...")
    elif len(sys.argv) > 1:
        try:
            index = 1
            while index < len(sys.argv):
                scores.append(int(sys.argv[index]))
                index += 1
            print(f"Scores processed: {scores}")
            print(f"Total players: {len(sys.argv) - 1}")
            total_score = sum(int(args) for args in scores)
            print(f"Total score: {total_score}")
            print(f"Average score: {(total_score / len(scores)):.0f}")
            print(f"High score: {max(scores)}")
            print(f"Low score: {min(scores)}")
            print(f"Score range: {max(scores) - min(scores)}")

        except ValueError as error:
            print(f"{error}")
