def intro():
    """Displays the introductory graphic."""
    print("""
        ;LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL;LLLLL
        ;LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL;LLLLL
        ;LLLL;;;;L;;;;;L;;;;L;;;;L;;;;L;;;;L;;;;
        ;LLLL;LL;L;L;L;L;LL;L;LL;LLLL;L;LL;L;LL;
        ;LLLL;;;;L;L;L;L;LL;L;LL;L;;;;L;LL;L;;;;
        ;LLLL;LLLL;L;L;L;LL;L;LL;L;LL;L;LL;L;LLL
        ;;;;L;;;;L;LLL;L;;;;L;LL;L;;;;L;;;;L;;;;

        LLLLLLLL;;;;;LL;LLLLLLLLLLLLLLL;LLLLLLLL
        LLLLLLLL;LLLLLL;LLLLLLLLLLLLLLL;LLLLLLLL
        LLLLLLLL;LLLLL;;;L;;;;L;;;;L;;;;LLLLLLLL
        LLLLLLLL;;;;;LL;LLLLL;L;LL;L;LL;LLLLLLLL
        LLLLLLLLLLLL;LL;LL;;;;L;LL;L;LL;LLLLLLLL
        LLLLLLLLLLLL;LL;LL;LL;L;LL;L;LL;LLLLLLLL
        LLLLLLLL;;;;;LL;LL;;;;L;LL;L;;;;LLLLLLLL
        """)

def title():
    """Displays title message, choose new or resume game."""
    pass

def main():
    """Main method for the game loop."""

    #Display the introductory graphic
    intro()

    #Display the title message
    title()

#Start the game loop
main()
