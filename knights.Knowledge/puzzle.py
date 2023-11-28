from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

L = Symbol("Truth")

# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0 = And(
    Or(AKnave,AKnight),
    Not(And(AKnave,AKnight)),
    Implication(AKnight,And(AKnight,AKnave)),
    Implication(AKnave,And(Or(AKnight,AKnave),Not(And(AKnave,AKnight))))
    
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(
    Or(AKnave,AKnight),
    Or(BKnave,BKnight),
    Not(And(AKnave,AKnight)),
    Not(And(BKnave,BKnight)),
    Implication(AKnight,And(AKnave,BKnave)),
    Implication(AKnave, And( Or(And(AKnight,BKnave),And(BKnight,AKnave),And(AKnight,BKnight))  ,Not(And(AKnave,BKnave))))
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
    Or(AKnave,AKnight),
    Or(BKnave,BKnight),
    Not(And(AKnave,AKnight)),
    Not(And(BKnave,BKnight)),
    Implication(AKnight,And(BKnight)),
    Implication(AKnave,And(BKnight)),
    Implication(BKnight,And(AKnave)),
    Implication(BKnave,And(AKnave))
    
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
    Or(AKnave,AKnight),
    Or(BKnave,BKnight),
    Or(CKnave,CKnight),
    Not(And(AKnave,AKnight)),
    Not(And(BKnave,BKnight)),
    Not(And(CKnave,CKnight)),
    Implication(AKnight,And(BKnave)),
    Implication(AKnave,And(BKnave)),
    #Implication(BKnight,And(CKnave,AKnave)),
    Implication(BKnave,And(CKnight,AKnight)),
    Implication(CKnight,And(AKnight)),
    Implication(CKnave,And(AKnave)),
    
)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
