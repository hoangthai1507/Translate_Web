
import os

import time
import requests


url = 'https://vnexpress.net'
model = "https://api.openai.com/v1/engines/davinci-codex/completions"


language = ['Vietnamese','English','German', 'Danish', 'Dutch', 'Norwegian', 'Italian', 'Spanish', 'Japanese', 'Chinese (Mandarin)',  'Thai', 'Korean', 'Russian', 'Romanian', 'Lao',  'Hindi', 'French', 'Arabic', 'Afrikaans', 'Albanian', 'Amharic', 'Armenian', 'Azerbaijani', 'Basque', 'Belarusian', 'Bengali', 'Bosnian', 'Bulgarian', 'Burmese', 'Catalan', 'Cebuano', 'Chichewa', 'Chinese (Cantonese)', 'Corsican', 'Croatian', 'Czech', 'Esperanto', 'Estonian', 'Finnish', 'Frisian', 'Galician', 'Georgian', 'Greek', 'Gujarati', 'Haitian Creole', 'Hausa', 'Hebrew', 'Hmong', 'Hungarian', 'Icelandic', 'Igbo', 'Indonesian', 'Irish', 'Javanese', 'Kannada', 'Kazakh', 'Khmer', 'Kurdish', 'Kyrgyz', 'Laothian', 'Latin', 'Latvian', 'Lithuanian', 'Luxembourgish', 'Macedonian', 'Malagasy', 'Malay', 'Malayalam', 'Maltese', 'Maori', 'Marathi', 'Mongolian', 'Nepali', 'Odia (Oriya)', 'Pashto', 'Persian', 'Polish', 'Portuguese', 'Punjabi', 'Quechua', 'Russian', 'Samoan', 'Scots Gaelic', 'Serbian', 'Sesotho', 'Shona', 'Sindhi', 'Sinhala', 'Slovak', 'Slovenian', 'Somali', 'Southern Sotho', 'Sundanese', 'Swahili', 'Swedish', 'Tagalog (Filipino)', 'Tajik', 'Tamil', 'Tatar', 'Telugu', 'Thai', 'Turkish', 'Turkmen', 'Ukrainian', 'Urdu', 'Uyghur', 'Uzbek', 'Vietnamese', 'Welsh', 'Xhosa', 'Yiddish', 'Yoruba', 'Zulu']
