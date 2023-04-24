PAGE_STYLING_JS = """
async () => {
    document.head.insertAdjacentHTML("beforeend", `<style>
        body {
            background-image: url("https://storage.cloud.google.com/public-file-hosting/ScrollBg11.jpg");
            background-size: cover;
            filter: brightness(0.45) sepia(0.7) contrast(2) brightness(2) saturate(0.1);
            opacity: 70%;
        }
    </style>`)
}
"""

TOP_OF_SCREEN_PADDING_DIV = """
<div style="height: 5vh;">
</div
"""

PLEASE_BE_PATIENT_DIV = """
<div style="background-color: white; font-family: cursive; font-size: 19px; padding: 2px 17px;">
After clicking Run Next Turn, please be patient as it may take up to a minute for the game state to update.
</div>
"""


MUSIC_PLAYER = """
<div style="background-color: white; font-family: cursive; font-size: 19px; padding: 2px 17px;">
Optional:  Click player below to play Nepali music.
<audio controls src="https://storage.cloud.google.com/public-file-hosting/NepaliFolkMusic.mp3"></audio>
</div>
"""
