import re

TAGS_WHITELIST = [
    "electronic",
    "experimental",
    "alternative",
    "rock",
    "ambient",
    "metal",
    "punk",
    "indie",
    "noise",
    "techno",
    "indie rock",
    "pop",
    "instrumental",
    "hip hop",
    "drone",
    "rap",
    "house",
    "folk",
    "acoustic",
    "electronica",
    "psychedelic",
    "singer-songwriter",
    "dark ambient",
    "hardcore",
    "lo-fi",
    "industrial",
    "jazz",
    "alternative rock",
    "hip-hop",
    "indie pop",
    "experimental electronic",
    "electro",
    "world",
    "beats",
    "lofi",
    "black metal",
    "deep house",
    "soundtrack",
    "post-punk",
    "post-rock",
    "punk rock",
    "soul",
    "downtempo",
    "shoegaze",
    "death metal",
    "dance",
    "funk",
    "minimal",
    "avant-garde",
    "improvisation",
    "synthwave",
    "idm",
    "vaporwave",
    "drum & bass",
    "blues",
    "progressive",
    "synthpop",
    "dub",
    "emo",
    "indie folk",
    "synth",
    "trap",
    "underground hip hop",
    "ambient electronic",
    "underground",
    "r&b",
    "electronic music",
    "folk rock",
    "piano",
    "tech house",
    "garage",
    "instrumental hip-hop",
    "dubstep",
    "harsh noise",
    "chillout",
    "americana",
    "pop rock",
    "classical",
    "guitar",
    "chill",
    "psychedelic rock",
    "soundscape",
    "hardcore punk",
    "progressive rock",
    "edm",
    "atmospheric",
    "pop punk",
    "garage rock",
    "psytrance",
    "grunge",
    "dream pop",
    "trance",
    "reggae",
    "hard rock",
    "country",
    "hiphop",
    "grindcore",
    "bass",
    "darkwave",
    "noise rock",
    "trip hop",
    "acid",
    "diy",
    "glitch",
    "doom",
    "new wave",
    "devotional",
    "experimental rock",
    "post-hardcore",
    "heavy metal",
    "dark",
    "new age",
    "breakbeat",
    "spoken word",
    "field recordings",
    "jungle",
    "thrash metal",
    "sound art",
    "experiemental",
    "disco",
    "doom metal",
    "free jazz",
    "electroacoustic",
    "world music",
    "cinematic",
    "breaks",
    "meditation",
    "boom bap",
    "metalcore",
    "chiptune",
    "rock & roll",
    "progressive metal",
    "bedroom pop",
    "orchestral",
    "drone ambient",
    "chillwave",
    "acoustic guitar",
    "fusion",
    "stoner rock",
    "alternative pop",
    "instrumentals",
    "soundscapes",
    "music",
    "power pop",
    "black-bandcamp",
    "blues rock",
    "electropop",
    "comedy",
    "breakcore",
    "bass music",
    "free improvisation",
    "sludge",
    "dungeon synth",
    "alt-country",
    "abstract",
    "roots",
    "goth",
    "melodic",
    "deep",
    "art rock",
    "progressive house",
    "harsh noise wall",
    "musique concrete",
    "contemporary",
    "rave",
    "power electronics",
    "drum and bass",
    "math rock",
    "ebm",
    "space",
    "experimental hip-hop",
    "latin",
    "stoner",
    "dub techno",
    "plunderphonics",
    "retrowave",
    "dnb",
    "psychedelic trance",
    "alternative hip-hop",
    "psych",
    "space rock",
    "live",
    "poetry",
    "folk punk",
    "minimal techno",
    "krautrock",
    "garage punk",
    "improvised music",
    "hip hop instrumentals",
    "house music",
    "remix",
    "minimalism",
    "deep techno",
    "independent",
    "improv",
    "beat tape",
    "gothic",
    "80s",
    "atmospheric black metal",
    "synthesizer",
    "surf",
    "nu disco",
    "ska",
    "modern classical",
    "samples",
    "post-metal",
    "hard techno",
    "rock and roll",
    "bedroom",
    "screamo",
    "synth pop",
    "weird",
    "avant garde",
    "folk pop",
    "film music",
    "experimental pop",
    "spiritual",
    "prog",
    "contemporary classical",
    "christian",
    "songwriter",
    "groove",
    "horror",
    "avantgarde",
    "crust",
    "field recording",
    "acoustic rock",
    "underground rap",
    "video game music",
    "boombap",
    "neo-soul",
    "powerviolence",
    "loops",
    "thrash",
    "neoclassical",
    "video game",
    "prog rock",
    "noise pop",
    "chillhop",
    "dreampop",
    "improvised",
    "rap & hip-hop",
    "classic rock",
    "minimalist",
    "rnb",
    "grime",
    "instrumental rock",
    "jam",
    "drums",
    "dance music",
    "female vocals",
    "jazz fusion",
    "raw black metal",
    "industrial techno",
    "retro",
    "deathcore",
    "noisecore",
    "heavy",
    "cassette",
    "sample-based",
    "post rock",
    "vocal",
    "deep tech",
    "lounge",
    "jazzy",
    "hnw",
    "leftfield",
    "cyberpunk",
    "sad",
    "tape",
    "indiepop",
    "space music",
    "sound collage",
    "soulful",
    "stoner metal",
    "future bass",
    "heavy rock",
    "analog",
    "neo-classical",
    "microhouse",
    "dancehall",
    "post punk",
    "melodic hardcore",
    "sludge metal",
    "love",
    "club",
    "surf rock",
    "meditative",
    "free",
    "funky",
    "christmas",
    "progressive trance",
    "djent",
    "bluegrass",
    "swing",
    "grind",
    "melodic death metal",
    "footwork",
    "coldwave",
    "art",
    "tribal",
    "piano solo",
    "witch house",
    "easy listening",
    "modular",
    "melodic techno",
    "punkrock",
    "gospel",
    "relaxing",
    "acid techno",
    "holland",
    "underground hip-hop",
    "relaxation",
    "rock'n'roll",
    "modern jazz",
    "chill out",
    "soulful house",
    "beat",
    "uk garage",
    "triphop",
    "lofi hiphop",
    "punk hardcore",
    "ambient rock",
    "post-industrial",
    "ethereal",
    "traditional",
    "rock n roll",
    "dreamy",
    "dark techno",
]

KEYWORD_TO_HASHTAG = {
    "drum & bass": "drumnbass",
    "r&b": "rnb",
    "rock & roll": "rocknroll",
    "rock'n'roll": "rocknroll",
}

def convert_keyword(k):
    lk = k.lower()
    if lk in KEYWORD_TO_HASHTAG.keys():
        return "#" + KEYWORD_TO_HASHTAG.get(lk)
    if lk not in TAGS_WHITELIST:
        return None
    nk = re.sub(r'[^\w\s-]','', lk).replace(" ", "_").replace("-", "_")
    return "#" + nk