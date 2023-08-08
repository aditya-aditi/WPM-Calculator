import random as rd
import time

paragraphs = [
    "The sun dipped below the horizon, painting the sky in hues of orange and pink. As darkness crept in, the stars emerged, sprinkling the night canvas with their shimmering light. A gentle breeze rustled the leaves, and the world seemed to exhale as the day came to a close.",
    "The old bookstore stood with its weathered facade, inviting passersby with the aroma of old paper and ink. Shelves upon shelves of books lined the walls, each one telling a different story. It was a sanctuary for book lovers, a place where time seemed to slow down as they immersed themselves in the worlds created by words.",
    "The little girl giggled as she chased after the butterflies, her laughter echoing through the meadow. The butterflies flitted around her, dancing in the sunlight. Her eyes sparkled with wonder as she tried to catch one, but they always slipped through her tiny fingers, leaving her in fits of laughter.",
    "The rain poured relentlessly, drumming on the roof and windows. Inside, a cozy fireplace crackled, casting a warm glow over the room. The sound of raindrops created a soothing melody, and the scent of wet earth filled the air. It was a perfect day to stay indoors with a good book and a cup of hot cocoa.",
    "The old oak tree stood tall and proud, its gnarlaed branches reaching toward the sky. It had witnessed generations pass by, and its bark held the stories of time. Birds nested in its branches, and children sought refuge in its shade on sunny days. It was a silent guardian, standing firm through the changing seasons.",
    "The city came alive as the night descended. Neon lights illuminated the streets, and the hustle and bustle of life continued. Each person carried their own story, their dreams, and aspirations, woven into the tapestry of the urban landscape. In the midst of the chaos, there was a strange beauty in the symphony of lives intertwining.",
    "The aroma of freshly baked bread filled the bakery, drawing people in like a magnet. The baker worked with practiced hands, kneading the dough with love and skill. Each loaf was a work of art, and as they emerged from the oven, they were met with appreciative smiles from customers eager to savor the warm goodness."
]


def generate_random_int():
    random_int = rd.randint(0, len(paragraphs) - 1)
    return random_int


def calculate_WPM(time_minutes, number_of_words):
    WPM = number_of_words/time_minutes
    return WPM


start_yn = input(
    "Welcome to the WPM calculator. Write start to continue or write exit to exit."
).lower()
if start_yn == "start":
    print(f"\n{paragraphs[generate_random_int()]}")
    start_time = time.time()
    userParagraph = input("Write the paragraph \n")
    end_time = time.time()
    elapsed_time = (end_time - start_time) / 60
    userParagraph_Splited = userParagraph.split(" ")
    print(f"Your WPM is {calculate_WPM(elapsed_time, len(userParagraph_Splited))}")
else:
    print("That game is being exited")
    exit()
