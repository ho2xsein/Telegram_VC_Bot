HEROKU = False   # NOTE Make it false if you're not deploying on heroku.

# NOTE these values are for heroku.
if HEROKU:
    from os import environ
    API_ID = int(environ["5378568"])
    API_HASH = environ["89ffcb590951a70b2f00d51a3689458b"]
    SUDO_CHAT_ID = int(environ["SUDO_CHAT_ID"]) # Chat where the bot will play the music.
    SUDOERS = list(int(x) for x in environ.get("SUDOERS", "63180149").split()) # Users which have special control over the bot.
    SESSION_STRING = environ["SESSION_STRING"] # Check Readme for session

# NOTE Fill this if you are not deploying on heroku.
if not HEROKU:
    API_ID = 5378568
    API_HASH = "89ffcb590951a70b2f00d51a3689458b"
    SUDO_CHAT_ID = -1001359346286
    SUDOERS = [63180149]

# don't make changes below this line
ARQ_API = "https://thearq.tech"
