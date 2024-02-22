# check availabl languages at: https://cloud.google.com/speech-to-text/docs/speech-to-text-supported-languages
# In case config.voiceTypingModel == "google", config.voiceTypingLanguage should be code list in column BCP-47 at https://cloud.google.com/speech-to-text/docs/speech-to-text-supported-languages
googleSpeeckToTextLanguages = {
    "Afrikaans (South Africa)": "af-ZA",
    "Akan (Ghana)": "ak-GH",
    "Albanian (Albania)": "sq-AL",
    "Amharic (Ethiopia)": "am-ET",
    "Arabic (Algeria)": "ar-DZ",
    "Arabic (Bahrain)": "ar-BH",
    "Arabic (Egypt)": "ar-EG",
    "Arabic (Iraq)": "ar-IQ",
    "Arabic (Israel)": "ar-IL",
    "Arabic (Jordan)": "ar-JO",
    "Arabic (Kuwait)": "ar-KW",
    "Arabic (Lebanon)": "ar-LB",
    "Arabic (Mauritania)": "ar-MR",
    "Arabic (Morocco)": "ar-MA",
    "Arabic (Oman)": "ar-OM",
    "Arabic (Qatar)": "ar-QA",
    "Arabic (Saudi Arabia)": "ar-SA",
    "Arabic (State of Palestine)": "ar-PS",
    "Arabic (Syria)": "ar-SY",
    "Arabic (Tunisia)": "ar-TN",
    "Arabic (United Arab Emirates)": "ar-AE",
    "Arabic (Yemen)": "ar-YE",
    "Armenian (Armenia)": "hy-AM",
    "Azerbaijani (Azerbaijan)": "az-AZ",
    "Basque (Spain)": "eu-ES",
    "Bengali (Bangladesh)": "bn-BD",
    "Bengali (India)": "bn-IN",
    "Bosnian (Bosnia and Herzegovina)": "bs-BA",
    "Bulgarian (Bulgaria)": "bg-BG",
    "Burmese (Myanmar)": "my-MM",
    "Catalan (Spain)": "ca-ES",
    "Chinese, Cantonese (Traditional Hong Kong)": "yue-Hant-HK",
    "Chinese, Mandarin (Simplified, China)": "zh",
    "Chinese, Mandarin (Traditional, Taiwan)": "zh-TW",
    "Croatian (Croatia)": "hr-HR",
    "Czech (Czech Republic)": "cs-CZ",
    "Danish (Denmark)": "da-DK",
    "Dutch (Belgium)": "nl-BE",
    "Dutch (Netherlands)": "nl-NL",
    "English (Australia)": "en-AU",
    "English (Canada)": "en-CA",
    "English (Ghana)": "en-GH",
    "English (Hong Kong)": "en-HK",
    "English (India)": "en-IN",
    "English (Ireland)": "en-IE",
    "English (Kenya)": "en-KE",
    "English (New Zealand)": "en-NZ",
    "English (Nigeria)": "en-NG",
    "English (Pakistan)": "en-PK",
    "English (Philippines)": "en-PH",
    "English (Singapore)": "en-SG",
    "English (South Africa)": "en-ZA",
    "English (Tanzania)": "en-TZ",
    "English (United Kingdom)": "en-GB",
    "English (United States)": "en-US",
    "Estonian (Estonia)": "et-EE",
    "Filipino (Philippines)": "fil-PH",
    "Finnish (Finland)": "fi-FI",
    "French (Belgium)": "fr-BE",
    "French (Canada)": "fr-CA",
    "French (France)": "fr-FR",
    "French (Switzerland)": "fr-CH",
    "Galician (Spain)": "gl-ES",
    "Georgian (Georgia)": "ka-GE",
    "German (Austria)": "de-AT",
    "German (Germany)": "de-DE",
    "German (Switzerland)": "de-CH",
    "Greek (Greece)": "el-GR",
    "Gujarati (India)": "gu-IN",
    "Hausa (Nigeria)": "ha-NG",
    "Hebrew (Israel)": "iw-IL",
    "Hindi (India)": "hi-IN",
    "Hungarian (Hungary)": "hu-HU",
    "Icelandic (Iceland)": "is-IS",
    "Igbo (Nigeria)": "ig-NG",
    "Indonesian (Indonesia)": "id-ID",
    "Italian (Italy)": "it-IT",
    "Italian (Switzerland)": "it-CH",
    "Japanese (Japan)": "ja-JP",
    "Javanese (Indonesia)": "jv-ID",
    "Kannada (India)": "kn-IN",
    "Kazakh (Kazakhstan)": "kk-KZ",
    "Khmer (Cambodia)": "km-KH",
    "Kinyarwanda (Rwanda)": "rw-RW",
    "Korean (South Korea)": "ko-KR",
    "Lao (Laos)": "lo-LA",
    "Latvian (Latvia)": "lv-LV",
    "Lithuanian (Lithuania)": "lt-LT",
    "Macedonian (North Macedonia)": "mk-MK",
    "Malay (Malaysia)": "ms-MY",
    "Malayalam (India)": "ml-IN",
    "Marathi (India)": "mr-IN",
    "Mongolian (Mongolia)": "mn-MN",
    "Nepali (Nepal)": "ne-NP",
    "Norwegian Bokmål (Norway)": "no-NO",
    "Persian (Iran)": "fa-IR",
    "Polish (Poland)": "pl-PL",
    "Portuguese (Brazil)": "pt-BR",
    "Portuguese (Portugal)": "pt-PT",
    "Punjabi (Gurmukhi India)": "pa-Guru-IN",
    "Romanian (Romania)": "ro-RO",
    "Russian (Russia)": "ru-RU",
    "Sepedi (South Africa)": "nso-ZA",
    "Serbian (Serbia)": "sr-RS",
    "Sinhala (Sri Lanka)": "si-LK",
    "Slovak (Slovakia)": "sk-SK",
    "Slovenian (Slovenia)": "sl-SI",
    "South Ndebele (South Africa)": "nr-ZA",
    "Southern Sotho (South Africa)": "st-ZA",
    "Spanish (Argentina)": "es-AR",
    "Spanish (Bolivia)": "es-BO",
    "Spanish (Chile)": "es-CL",
    "Spanish (Colombia)": "es-CO",
    "Spanish (Costa Rica)": "es-CR",
    "Spanish (Dominican Republic)": "es-DO",
    "Spanish (Ecuador)": "es-EC",
    "Spanish (El Salvador)": "es-SV",
    "Spanish (Guatemala)": "es-GT",
    "Spanish (Honduras)": "es-HN",
    "Spanish (Mexico)": "es-MX",
    "Spanish (Nicaragua)": "es-NI",
    "Spanish (Panama)": "es-PA",
    "Spanish (Paraguay)": "es-PY",
    "Spanish (Peru)": "es-PE",
    "Spanish (Puerto Rico)": "es-PR",
    "Spanish (Spain)": "es-ES",
    "Spanish (United States)": "es-US",
    "Spanish (Uruguay)": "es-UY",
    "Spanish (Venezuela)": "es-VE",
    "Sundanese (Indonesia)": "su-ID",
    "Swahili": "sw",
    "Swahili (Kenya)": "sw-KE",
    "Swahili (Tanzania)": "sw-TZ",
    "Swati (Latin, South Africa)": "ss-Latn-ZA",
    "Swedish (Sweden)": "sv-SE",
    "Tamil (India)": "ta-IN",
    "Tamil (Malaysia)": "ta-MY",
    "Tamil (Singapore)": "ta-SG",
    "Tamil (Sri Lanka)": "ta-LK",
    "Telugu (India)": "te-IN",
    "Thai (Thailand)": "th-TH",
    "Tsonga (South Africa)": "ts-ZA",
    "Tswana (Latin, South Africa)": "tn-Latn-ZA",
    "Turkish (Turkey)": "tr-TR",
    "Ukrainian (Ukraine)": "uk-UA",
    "Urdu (India)": "ur-IN",
    "Urdu (Pakistan)": "ur-PK",
    "Uzbek (Uzbekistan)": "uz-UZ",
    "Venda (South Africa)": "ve-ZA",
    "Vietnamese (Vietnam)": "vi-VN",
    "Xhosa (South Africa)": "xh-ZA",
    "Yoruba (Nigeria)": "yo-NG",
    "Zulu (South Africa)": "zu-ZA",
}

# check availabl languages at: https://github.com/openai/whisper/blob/main/whisper/tokenizer.py
# In case config.voiceTypingModel == "whisper", config.voiceTypingLanguage should be uncapitalized full language name like "english" or "chinese"
whisperSpeeckToTextLanguages = (
    "english",
    "chinese",
    "german",
    "spanish",
    "russian",
    "korean",
    "french",
    "japanese",
    "portuguese",
    "turkish",
    "polish",
    "catalan",
    "dutch",
    "arabic",
    "swedish",
    "italian",
    "indonesian",
    "hindi",
    "finnish",
    "vietnamese",
    "hebrew",
    "ukrainian",
    "greek",
    "malay",
    "czech",
    "romanian",
    "danish",
    "hungarian",
    "tamil",
    "norwegian",
    "thai",
    "urdu",
    "croatian",
    "bulgarian",
    "lithuanian",
    "latin",
    "maori",
    "malayalam",
    "welsh",
    "slovak",
    "telugu",
    "persian",
    "latvian",
    "bengali",
    "serbian",
    "azerbaijani",
    "slovenian",
    "kannada",
    "estonian",
    "macedonian",
    "breton",
    "basque",
    "icelandic",
    "armenian",
    "nepali",
    "mongolian",
    "bosnian",
    "kazakh",
    "albanian",
    "swahili",
    "galician",
    "marathi",
    "punjabi",
    "sinhala",
    "khmer",
    "shona",
    "yoruba",
    "somali",
    "afrikaans",
    "occitan",
    "georgian",
    "belarusian",
    "tajik",
    "sindhi",
    "gujarati",
    "amharic",
    "yiddish",
    "lao",
    "uzbek",
    "faroese",
    "haitian creole",
    "pashto",
    "turkmen",
    "nynorsk",
    "maltese",
    "sanskrit",
    "luxembourgish",
    "myanmar",
    "tibetan",
    "tagalog",
    "malagasy",
    "assamese",
    "tatar",
    "hawaiian",
    "lingala",
    "hausa",
    "bashkir",
    "javanese",
    "sundanese",
    "cantonese",
)