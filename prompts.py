PROMPT_MAP = {
    "Describe Image": "Describe this image in detail.",

    "Quick Summary":
    "Give a concise summary of this image.",

    "Detect Objects":(
    "Detect all unique objects visible in the image. "
    "Output only object names. "
    "Do not provide explanations, descriptions, attributes, actions, or repeated items. "
    "Merge similar objects into a single category. "
    "Return a bullet list containing one object per line."
    ),

    "Generate Caption": (
    "Generate a concise and engaging caption of 2 to 5 words only. "
    "Do not write a complete sentence. "
    "Do not use punctuation, quotation marks, hashtags, emojis, or explanations. "
    "Return only the caption."
    )
}
MAX_TOKENS = {
    "Describe Image": 350,
    "Quick Summary": 150,
    "Detect Objects": 100,
    "Generate Caption": 10
}
