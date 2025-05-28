import streamlit as st
from itertools import permutations

st.set_page_config(page_title="המחדשה", layout="centered")

# Function to make initial replacements in the input
def initial_replacements(word):
    replacements = {
        'ם': 'מ',
        'ן': 'נ',
        'ץ': 'צ',
        'ך': 'כ',
        'ף': 'פ'
    }
    if word[-1] in replacements:
        word = word[:-1] + replacements[word[-1]]
    return word
    
# Function to replace specific letters at the end of each word
def replace_end_letters(word):
    if word.endswith('מ'):
        return word[:-1] + 'ם'
    elif word.endswith('נ'):
        return word[:-1] + 'ן'
    elif word.endswith('צ'):
        return word[:-1] + 'ץ'
    elif word.endswith('כ'):
        return word[:-1] + 'ךְ'
    elif word.endswith('פ'):
        return word[:-1] + 'ף'
    elif word.endswith('יח'):
        return word[:-1] + 'חַ'
    elif word.endswith('וֹח'):
        return word[:-1] + 'חַ'
    elif word.endswith('וּח'):
        return word[:-1] + 'חַ'    
    elif word.endswith('ֵח'):
        return word[:-1] + 'חַ'   
    elif word.endswith('יע'):
        return word[:-1] + 'עַ'
    elif word.endswith('וֹע'):
        return word[:-1] + 'עַ'
    elif word.endswith('וּע'):
        return word[:-1] + 'עַ'    
    elif word.endswith('ֵע'):
        return word[:-1] + 'עַ'  
    else:
        return word

def add_dagesh(word):
    if len(word) > 0 and '\u05BC' not in word[0]:
        return word[0] + '\u05BC' + word[1:]
    return word

        

# Function to replace specific letter combinations
def replace_letters(word):
    replacements = {
        "הִתְזַּ": "הִזְ",
        "הִתְזַ": "הִזְ",
        "מִתְזַ" :"מִזְדַ",
        "הִתְצַ": "הִצְטַ",
        "הִתְצַּ": "הִצְטַּ",
        "הִתְשַּ": "הִשְׁתַּ",
        "הִתְשַ": "הִשְׁתַ",
        "הִתְשּ" :"הִשְתּ"  ,
        "ִאּ": "ֵא",
        "ַאּ": "ָא",
        "ֻאּ": "ֹא",
        "ִרּ": "ֵר",
        "ַרּ": "ָר",
        "ֻרּ": "ֹר",
        "ֻהּ": "ֹה",
        "ֻעּ": "ֹע"
    }
    
    for key, value in replacements.items():
        word = word.replace(key, value)
    return word


# Function to handle four-letter inputs
def process_letters(input_letters):
    if len(input_letters) == 4:
        return [input_letters[:2], input_letters[2], input_letters[3]]
    return input_letters

# Function to generate the output list with replaced letters and transformed end letters
def generate_list(letters, patterns):
    replaced_list = []
    for pattern in patterns:
        modified_pattern = pattern.replace('1', letters[0]) \
                                  .replace('2', letters[1]) \
                                  .replace('3', letters[2])
        transformed_pattern = replace_end_letters(add_dagesh(modified_pattern))
        final_pattern = replace_letters(transformed_pattern)  # Apply replace_letters here
        replaced_list.append(final_pattern)
    return replaced_list

def add_dagesh(word):
    if len(word) > 0 and '\u05BC' not in word[0]:  # Check for dagesh in the first letter
        return word[0] + '\u05BC' + word[1:]
    return word


# Function to generate additional categories based on specific conditions
def generate_additional_categories(input_letters):
    categories = {}


    # Condition for גזרת חפן
    if (len(input_letters) == 3 and input_letters[0] == 'נ') or (len(input_letters) == 3 and input_letters[0] == 'י' and input_letters[1] == 'צ'):
        categories["שורש מגזרת חפ''ן"] = generate_list(input_letters, [
"\nשם עצם מופשט: " +
"נָ2ָ3, נֶ2ֶ3, נֹ2ֶ3, נִ2ְ3ָה, נַ2ְ3ָה, נִ2ְ3ָה, נֶ2ְ3ָה, נִ2ְ3וֹן, נִ2ָּ3וֹן, נַ2ְ3וּת, נִ2ֹּו3ֶת, נְ2ֻ3ָּה, תַּנְ2ִי3, תַּנְ2וּ3ָה, תַּנְ2ֵ3ָה, תִּנְ2ֶ3ֶת, תִּנְ2ֹ3ֶת"
+ "\nבעלי תכונה: " +
"נַ2ּוּ3, נַ2ִּי3, נָ2ִי3, נָ2ֹ3, נִ2ּוֹ3"
+ "\nשמות פעולה: " +
"נְ2ִי3ָה, הִתֲ2ְּ3וּת \ הִנָּ2ְ3וּת, נִ2ּוּ3, הַ2ָּ3ָה \ הַנְ2ָ3ָה, הֶ2ֵּ3 \ הֶנְ2ֵ3, הִתְנַּ2ְּ3וּת, אִ2ּוּ3, תִּ2ּוּ3 \ תִּנְ2וּ3, הִּ2ְ3וּת, (חזרה על פעולה או חידוש) שִׁ2ּוּ3 \ שִׁנְ2וּ3, (פעולה רשמית או מוגברת) נִ2ְ3וּ3"
+ "\nהקטנה: " +
"נַ2ְ3ִי3, נַ2ְ3וּ3, נְ2ַ3ְ2ַ3"
+ "\nמקומות: " +
"2ָּ3 \ מִנְ2ָ3, מִ2ָּ3ָה \ מִנְ2ָ3ָה, מִ2וֹ3, נִ2ְ3ִיָּה"
 +  "\nבעלי מקצוע: " +
"2ְ3ָן, נַ2ְּ3ָן, נַ2ָּ3, נַ2ַּאי, נַ2ְ3ַאי, (מ1ור ארמי) נָ2וֹ3ַאי, (מ1ור ארמי) אַנְ2ְ3ַאי"
+ "\nכלים: " +
"מְִ2ֵ3, מֲ2ֵ3 \ מַנְ2ֵ3, מְַ2ֵ3ָה \ מַנְ2ֵ3ָה, מְַ2ֶ3ֶת \ מִנְ2ֶ3ֶת, מִ2ֹּ3ֶת \ מִנְ2ֹ3ֶת, מִ2ּוֹ3 \ מִנְ2וֹ3, נַ2ִּי3, נַ2ּוּ3, נִ2ּוֹ3, נַ2ֶּ3ֶת, מֶ2ָ3ָה, מְַ2ִי3,מְַ2וֹ3, מְַ2וֹ3ִית"
+ "\nחיבור של כמה אנשים/עצמים: נְ2וּ3ָה, צבעים: נָ2ֹ3, חקלאות: נָ2ִי3, מומים: נִ2ֵּ3, דגים וחיות ים: נְ2ַ3ְנוּן, מחלות: נַ2ֶּ3ֶת"
+ "\n" + "\nשונות: " +
"מַ2ָּ3, אֶ2ָ3, אֶ2וֹ3, אַ2ָ3ָה, יַ2וּ3, מְנַ2ֵּ3, מֻ2ָּ3, מְנֻ2ָּ3וּת, מִנְ2ֵ3, מִ2ָּ3, מִתְנַ2ֵּ3, מֶ2ָּ3ָה, מַ2ִי3, מַ2ֵּ3, מַ2ֵּ3ָה, מַ2ֶּ3ֶת, מְֻ2ָּ3וּת, מַ2ָּ3ָה, מַ2ֹּ3ֶת, מַ2וֹ3ִית, מְַ2וּ3, מַ2וּ3ָה, מֻנְ2ָ3, מֻנְ2ָ3ָה, נִ2ָ3, נִ2ָ3וּת, נְ2ִי3, נְ2ִי3וּת, נְ2ִ3ָּה, נְ2ֵ3, נְ2ֵ3ֶת," + "נְ2ֵ3ָה, נְ2ֶ3ֶת, נְ2ַ3ְ2ֶ3ֶת, נְ2ַ3ְ2ֹ3ֶת, נְ2ָ3,נְ2ָ3ִים, נְ2ָ3ָה, נְ2ֹ3ֶת, נְ2וֹ2ֶ3ֶת, נְ2וֹ3, נְ2וֹ3ָה, נְ2וּ3, נְ2וּ3ִית, נִ2ְ3ָן, נִ2ְ3וֹנִי, נִ2ֵּ3, נִ2ֶּ3ֶת, נִ2ָּ3, נִ2ֹּ3ֶת, נִי2וֹ3, נֵ2ֶ3, נֵ2וּ3, נֶ2ְ3ָה, נַ2ְּ3ָן, נַ2ְ3ִי3, נַ2ְ3ִית, נַ2ְ3ָנִי, נַ2ְ3וֹן, נַ2ְ3וּ3ִי, נַ2ֵּ3, נַ2ָּ3ָה, נַ2ֹּ3ֶת, נַ2וֹ3, נָ2ְ3ָה, נָ2ֵ3, נָ2וֹ3, נָ2וּ3, נֻ2ְ3ָה, נֻ2ְ3ָן, נֻ2ָּ3, מִתְַ2ֵּ3, 2ַ3ְ2ַ3, נֻ2ֹּ3ֶת, נוֹ2ְ3ָה, נוֹ2ְ3ָן, נוֹ2ֵ3, נוֹ2ֶ3ֶת, נוֹ2ָ3, תַּ2ֵ3, תַּ2ֵּ3ָה, תַּ2ָ3ָה, תַּ2וּ3, 2ָ3, מִנָּ3"
+ "\n חֲ1ַ2ֶּ3ֶת,1וּ2ְ3ָה" 
+ "\n הכפלת אות: 2ִ3ְ2ֵ3"
+ "\n שורשים תניינים אפשריים: מ12’’3, א12’’3, ת12’’3, 123’’ת \n"
+ "\n ( ניתן להזין את השורש החדש באתר )"
"\nהוספת אות בתחילת מילה: סִ1ְ2ֵ3, שִׁ1ְ2ֵ3, שִַ1ְ2ֶ3ֶת"
+ "\n ריבוי מיוחד: 1ַ2ְ3וֹנִים, 1ְּ2ִ3ִים"
+ "\n" +
+ "\n נדירים" +
+ "\n הוספת אות באמצע מילה: קע23, 12ע3, 1323, 1ר23 (1ַרְ2ָ3 \ 1ַּרְ2ּוֹ3 \ 1ַרְ2ִי3 \ 1ֻרְ2ָ3 \ 1ִּרְ2ֹּ3 \ 1ַרְ2ַ3ִּים וכיו''ב)"
+ "\n בעברית ישראלית משתמשים בשורשים מגזרת חפ’’ן גם על דרך גזרת השלמים ולהלן: \n"

        ])
        
    # Condition for גזרת השלמים
    if (input_letters[0] not in ['י'] and 
        input_letters[1] not in ['ו', 'י'] and 
        input_letters[2] not in ['י', 'ה', 'א'] and 
        input_letters[1] != input_letters[2]):
        categories["שורש מגזרת השלמים"] = generate_list(input_letters, [
     "\nשם עצם מופשט: " +
'1ָ2ָ3','1ֶ2ֶ3','1ֹ2ֶ3','1ִ2ְ3ָה','1ַ2ְ3ָה','1ִ2ְ3ָה','1ֶ2ְ3ָה','1ִ2ְ3וֹן','1ִ2ָּ3וֹן','1ַ2ְ3וּת','1ִ2ֹּו3ֶת','1ְ2ֻ3ָּה','תַּ1ְ2ִי3','תַּ1ְ2וּ3ָה','תַּ1ְ2ֵ3ָה','תִּ1ְ2ֶ3ֶת','תִּ1ְ2ֹ3ֶת'
+ "\nבעלי תכונה: " +
'1ַ2ּוּ3','1ַ2ִּי3','1ָ2ִי3','1ָ2ֹ3','1ִ2ּוֹ3'
+ "\nשמות פעולה: " +
'1ְ2ִי3ָה', 'הִ1ָּ2ְ3וּת', '1ִ2ּוּ3', 'הַ1ְ2ָ3ָה', 'הֶ1ְ2ֵ3', 'הִתְ1ַּ2ְּ3וּת', 'אִ1ְ2וּ3', 'תּ1ְ2וּ3', '(חזרה על פעולה או חידוש) שִׁ1ְ2וּ3', '(פעולה רשמית או מוגברת) 1ִ2ְ3וּ3'
+ "\nהקטנה: " +
'1ַ2ְ3ִי3','1ַ2ְ3וּ3','1ְ2ַ3ְ2ַ3'
+ "\nמקומות: " +
'מִ1ְ2ָ3','מִ1ְ2ָ3ָה','מִ1ְ2וֹ3','1ִ2ְ3ִיָּה'
 +  "\nבעלי מקצוע: " +
'1ַ2ְ3ָן', '1ַ2ְּ3ָן', '1ַ2ָּ3', '1ַ2ַּאי', '1ַ2ְ3ַאי', '(מקור ארמי) 1ָ2וֹ3ַאי', '(מקור ארמי) אַ1ְ2ְ3ַאי'
+ "\nכלים: " +
'מַ1ְ2ֵ3','מַ1ְ2ֵ3ָה','מִ1ְ2ֶ3ֶת','מִ1ְ2ֹ3ֶת','מִ1ְ2וֹ3','1ַ2ִּי3','1ַ2ּוּ3','1ִ2ּוֹ3','1ַ2ֶּ3ֶת'
+ "\nחיבור של כמה אנשים/עצמים: 1ְ2וּ3ָה, צבעים: 1ָ2ֹ3", 'חקלאות: 1ָ2ִי3', 'מומים: 1ִ2ֵּ3', 'דגים וחיות ים: 1ְ2ַ3ְנוּן', 'מחלות: 1ַ2ֶּ3ֶת'
+ "\n" + "\nשונות: " +
'אֶ1ְ2ָ3', 'אֶ1ְ2וֹ3', 'אַ1ְ2ָ3ָה', 'יַ1ְ2וּ3', 'מְ1ַ2ֵּ3', 'מְ1ֻ2ָּ3', 'מְ1ֻ2ָּ3וּת', 'מִ1ְ2ֵ3', 'מִ1ְ2ָ3', 'מִתְ1ַ2ֵּ3', 'מֶ1ְ2ָ3ָה', 'מַ1ְ2ִי3', 'מַ1ְ2ֵ3', 'מַ1ְ2ֵ3ָה', 'מַ1ְ2ֶ3ֶת', 'מַ1ְ2ָ3ָה', 'מַ1ְ2ֹ3ֶת', 'מַ1ְ2וֹ3', 'מַ1ְ2וֹ3ִית', 'מַ1ְ2וּ3', 'מַ1ְ2וּ3ָה', 'מֻ1ְ2ָ3', 'מֻ1ְ2ָ3ָה', 'נִ1ְ2ָ3', 'נִ1ְ2ָ3וּת', '1ְ2ִי3', '1ְ2ִי3וּת', '1ְ2ִ3ָּה', '1ְ2ֵ3', '1ְ2ֵ3ֶת', '1ְ2ֵ3ָה', '1ְ2ֶ3ֶת', '1ְ2ַ3ְ2ֶ3ֶת', '1ְ2ַ3ְ2ֹ3ֶת', '1ְ2ָ3', '1ְ2ָ3ִים', '1ְ2ָ3ָה', '1ְ2ֹ3ֶת', '1ְ2וֹ2ֶ3ֶת', '1ְ2וֹ3', '1ְ2וֹ3ָה', '1ְ2וּ3', '1ְ2וּ3ִית', '1ִ2ְ3ָן', '1ִ2ְ3וֹנִי', '1ִ2ֵּ3', '1ִ2ֶּ3ֶת', '1ִ2ָּ3', '1ִ2ֹּ3ֶת', '1ִי2וֹ3', '1ֵ2ֶ3', '1ֵ2וּ3', '1ֶ2ְ3ָה', '1ַ2ְּ3ָן', '1ַ2ְ3ִי3', '1ַ2ְ3ִית', '1ַ2ְ3ָנִי', '1ַ2ְ3וֹן', '1ַ2ְ3וּ3ִי', '1ַ2ֵּ3', '1ַ2ָּ3ָה', '1ַ2ֹּ3ֶת', '1ַ2וֹ3', '1ָ2ְ3ָה', '1ָ2ֵ3', '1ָ2וֹ3', '1ָ2וּ3', '1ֻ2ְ3ָה', '1ֻ2ְ3ָן', '1ֻ2ָּ3', '1ֻ2ֹּ3ֶת', '1וֹ2ְ3ָה', '1וֹ2ְ3ָן', '1וֹ2ֵ3', '1וֹ2ֶ3ֶת', '1וֹ2ָ3', 'תַּ1ְ2ֵ3', 'תַּ1ְ2ֵ3ָה', 'תַּ1ְ2ָ3ָה', 'תַּ1ְ2וּ3'
+ "\n נדירים:" 
+ "\nהוספת אות בתחילת מילה: סִ1ְ2ֵ3, שִׁ1ְ2ֵ3, שִַ1ְ2ֶ3ֶת"
+ "\n הוספת אות באמצע מילה: קע23, 12ע3, 1323, 1ר23 (1ַרְ2ָ3 \ 1ַּרְ2ּוֹ3 \ 1ַרְ2ִי3 \ 1ֻרְ2ָ3 \ 1ִּרְ2ֹּ3 \ 1ַרְ2ַ3ִּים וכיו''ב)"
+ "\n ניתן לחפש את השורש החדש כשורש מרובע חדש"
+ "\n חֲ1ַ2ֶּ3ֶת,1וּ2ְ3ָה" 
+ "\n ריבוי מיוחד: 1ַ2ְ3וֹנִים, 1ְּ2ִ3ִים"
+ "\n שורשים תניינים אפשריים: מ12’’3, א12’’3, ת12’’3, 123’’ת \n"

        ])
            
    # Condition for גזרת נפיו
    if len(input_letters) == 3 and input_letters[0] in 'יוׁ':
        categories["שורש מגזרת נפי''ו"] = generate_list(input_letters, [
"\nשם עצם מופשט: " +
"יָ2ָ3, יֶ2ֶ3, יֹ2ֶ3, יִ2ְ3ָה, יַ2ְ3ָה, יִ2ְ3ָה, יֶ2ְ3ָה, יִ2ְ3וֹן, יִ2ָּ3וֹן, יַ2ְ3וּת, יִ2ֹּו3ֶת, יְ2ֻ3ָּה, תּוֹ2ִי3, תּוֹ2ֵ3ָה, תּוֹ2ֶ3ֶת, תִּי2ֹ3ֶת"
+ "\nבעלי תכונה: " +
"יַ2ּוּ3, יַ2ִּי3, יָ2ֹ3, יִ2ּוֹ3, יִ2ְ3וֹנִי"
+ "\nשמות פעולה: " +
"יְ2ִי3ָה, הִוָּ2ְ3וּת, הִתְוַ2ְּ3וּת, יִ2ּוּ3, הוֹ2ָ3ָה, הְִ2ָ3ָה, הֶיְ2ֵ3, הִתְיַּ2ְּ3וּת, תִּי2וּ3, תִּי2וֹ3, (חזרה על פעולה או חידוש) שִׁי2וּ3, (פעולה רשמית או מוגברת) יִ2ְ3וּ3"
+ "\nהקטנה: " +
"יַ2ְ3ִי3, יַ2ְ3וּ3, יְ2ַ3ְ2ַ3"
+ "\nמקומות: " +
"מוֹ2ָ3, מֵי2ָ3, מוֹ2ָ3ָה, מִי2וֹ3, מַ2ֵּ3ָה"
 +  "\nבעלי מקצוע: " +
"יַ2ְ3ָן, יַ2ְּ3ָן, יַ2ָּ3, יַ2ְ3ַאי, (מקור ארמי) יָ2וֹ3ַאי, (מקור ארמי) אַ2ְ3ַאי"
+ "\nכלים: " +
"מוֹ2ֵ3, מוֹ2ֵ3ָה, מוֹ2ֶ3ֶת, יַ2ִּי3, יַ2ּוּ3, יִ2ּוֹ3, יַ2ֶּ3ֶת"
+ "\nחיבור של כמה אנשים/עצמים: יְ2וּ3ָה, צבעים: יָ2ֹ3, חקלאות: יָ2ִי3, מומים: יִ2ֵּ3, דגים וחיות ים: 2ַ3ְנוּן \ יְ2ַ3ְנוּן, מחלות: יַ2ֶּ3ֶת"
+ "\n" + "\nשונות: " +
"מַ2ָּ3, 2ֵי3ָה, 2ֵּ3ָה,מוֹ2ָ3ָה, מְיַ2ֵּ3, מְיֻ2ָּ3, מְיֻ2ָּ3וּת, מוֹ2ֵ3, מוֹ2ָ3, מִתְיַ2ֵּ3, מוֹ2ִי3, מוֹ2ֵ3ָה, מוֹ2ֶ3ֶת, מַיְ2ֹ3ֶת, מִי2וֹ3ִית, מִי2וּ3, מִי2וּ3ָה, מוּ2ָ3, מוּ2ָ3ָה, נִי2ָ3, נִי2ָ3וּת, יְ2ִי3, יְ2ִי3וּת, יְ2ִ3ָּה, יְ2ֵ3, יְ2ֵ3ֶת, יְ2ֵ3ָה, יְ2ֶ3ֶת, יְ2ַ3ְ2ֶ3ֶת, יְ2ַ3ְ2ֹ3ֶת, יְ2ָ3, יְ2ָ3ִים, יְ2ָ3ָה, יְ2ֹ3ֶת, יְ2וֹ2ֶ3ֶת, יְ2וֹ3, יְ2וֹ3ָה, יְ2וּ3, יְ2וּ3ִית, יִ2ְ3ָן, יִ2ְ3וֹנִי, יִ2ֵּ3, יִ2ֶּ3ֶת, יִ2ָּ3, יִ2ֹּ3ֶת, יִי2וֹ3, יֵ2ֶ3, יֵ2וּ3, יֶ2ְ3ָה, יַ2ְּ3ָן, יַ2ְ3ִי3, יַ2ְ3ִית, יַ2ְ3ָנִי, יַ2ְ3וֹן, יַ2ְ3וּ3ִי, יַ2ֵּ3, יַ2ָּ3ָה, יַ2ֹּ3ֶת, יַ2וֹ3, יָ2ְ3ָה, יָ2ֵ3, יָ2וֹ3, יָ2וּ3, יֻ2ְ3ָה, יֻ2ְ3ָן, יֻ2ָּ3, יֻ2ֹּ3ֶת, יוֹ2ְ3ָה, יוֹ2ְ3ָן, יוֹ2ֵ3, יוֹ2ֶ3ֶת, יוֹ2ָ3, תֵּ2ֵ3, תֵּי2ָ3, תֶּ2ֶ3, תּוֹ2ָ3, תּוֹ2ָ3ָה" 
+ "\n שורשים תניינים אפשריים: מ2''3, ת2''3\n"
        ])


    # Condition for גזרת נליה
    if len(input_letters) == 3 and input_letters[-1] in 'יה':
        categories["שורש מגזרת נלי''ה"] = generate_list(input_letters, [
"\nשם עצם מופשט: " +
"1ָ2ָי,1ָ2ָה,1ֶ2ֶי, 1ֹ2ִי,1ֹ2ֶה, 1ִ2ְיָה, 1ַ2ְיָה,1ְּ2ָיָה, 1ִ2ְיָּה, 1ֶ2ְיָה, 1ִ2ְיוֹן, 1ִ2ָּיוֹן, 1ְ2וּת, 1ִ2ֹּויֶת, 1ְ2ֻיָּה, תַּ1ְ2ִיה, תַּ1ְ2וּאָה, תַּ1ְ2וּאָה, תַּ1ְ2ֵיָה, תַּ1ְ2ִית"
+ "\nבעלי תכונה: " +
"1ַּ2ּוּי, 1ַּ2ִּי, 1ָּ2ִי, 1ָּ2ֹי, 1ִּ2ּוֹי, 1ָ2וֹן"
+ "\nשמות פעולה: " +
"1ְ2ִיָה, הִ1ָּ2ְוּת, 1ִ2ּוּי, הַ1ְ2ָיָה, הֶ1ְ2ֵה, הִתְ1ַּ2ּוּת, אִ1ְ2וּי, תּ1ְ2וּי, (חזרה על פעולה או חידוש) שִׁ1ְ2וּי, (פעולה רשמית או מוגברת) 1ִ2ְיוּי"
+ "\nמקומות: " +
"מִ1ְ2ֶה, מִ1ְ2ָיָה, 1ִ2ִיָּה"
 +  "\nבעלי מקצוע: " +
"1ַ2ְיָן, 1ַ2ְּיָן, 1ַ2ָּי, 1ַ2ַּאי, 1ְ2ַאי, 1ַ2ְיַאי, (מקור ארמי) 1ָ2וֹיַאי, (מקור ארמי) אַ1ְ2ְיַאי" 
+ "\nכלים: " +
"מַ1ְ2ֵה, מַ1ְ2ֶה, מַ1ְ2ֵיָה, מִ1ְ2ִית, 1ִ2ּוֹי, 1ַ2ֶּיֶת"
+ "\nחיבור של כמה אנשים\עצמים: "+
"1ְ2וּיָה"
+ " צבעים: 1ָ2ֹי \ 1ָ2ֹה , חקלאות: 1ָ2ִיָה, מומים: 1ִ2ֵּה, דגים וחיות ים: 1ְ2ַנוּן, מחלות: 1ַ2ֶּיֶת"
+ "\n" + "\nשונות: " +
"אֶ1ְ2ָה,הַ1ְ2ָאָה, אַ1ְ2ָאָה, אַ1ְ2ָיָה, 1ָ2ֶה, מְ1ַ2ֵּה, מְ1ֻ2ָּה, מְ1ֻ2ָּיוּת, מִ1ְ2ֵה, מִ1ְ2ָה, מַ1ְ2ִה, מִתְ1ַ2ֵּה, מֶ1ְ2ָיָה, מַ1ְ2ֵה, מַ1ְ2ֵהַ, מַ1ְ2ִית, מַ1ְ2ָיָה, מַ1ְ2וֹא, מַ1ְ2וֹאִית, מַ1ְ2וּא, מַ1ְ2וּאָה, מֻ1ְ2ָה, מֻ1ְ2ָאָה, מִ1ְ2ָאָה, מַ1ֲ2ַיִם, נִ1ְ2ָה, נִ1ְ2ָאוּת, 1ְ2ִיה, 1ְ2ִיוּת, 1ְ2ִיָּה, 1ְ2ֵה, 1ְ2ֵיָה, 1ְ2ֶיֶת,1ְ2ָה, 1ְ2ָיִם, 1ְ2ָיָה, 1ֵ2וּת, 1ְ2וּת, 1ָ2וּת, 1ְ2ֹיֶת, 1ְ2וֹ2ִית, 1ְ2וֹא, 1ְ2ִיאָה, 1ְ2וֹיָה, 1ְ2וּאִית, 1ִ2ְיָן"
+ "\n נדירים:" 
+ "\n הכפלת אות: 1212 (1ִּ2ֲ1ֵ2 \ 1ִּ2ְ1ֵ2 \ 1ַּ2ְ1ַּ2ִּים \ 1ָּ2ְ1ָ2ִּית וכיו''ב)" 
+ "\n שורשים תניינים אפשריים: ת1''2, 12י''נ, ת12''ת \n"

        ])

    # Condition for  גזרת נלא
    if len(input_letters) == 3 and input_letters[-1] == 'א':
        categories["שורש מגזרת נל''א"] = generate_list(input_letters, [
"\nשם עצם מופשט: " +
"1ֹ2ִי, 1ֵ2וּת, 1ְ2וּת, 1ָ2וּת, 1ָ2וֹן, מִ1ְ2ָה, מַ1ְ2ִית, תַּ1ְ2וּת, תִּ1ְ2ָה, תְַ1ְ2ִית, 1ָ2ָ3, 1ֶ2ֶ3, 1ֹ2ֶ3, 1ִ2ְ3ָה, 1ַ2ְ3ָה, 1ִ2ְ3ָה, 1ֶ2ְ3ָה, 1ִ2ְ3וֹן, 1ִי2ָּאוֹן, 1ַ2ְ3וּת, 1ְ2ֻ3ָּה, תַּ1ְ2ִי3, תַּ1ְ2וּ3ָה, תִּ1ְ2ֶ3ֶת, תִּ1ְ2ֹ3ֶת"
+ "\nבעלי תכונה: " +
"1ַ2ּוּא,1ַ2ּוּי,1ָ2ֶה, 1ֵ2ֶה, 1ַ2ִּי3, 1ָ2ִי3, 1ָ2ֹ3, 1ִ2ּוֹ3, 1ַ2ַּאי"
+ "\nשמות פעולה: " +
"1ְ2ִי3ָה, הִ1ָּ2ְ3וּת, 1ִ2ּוּ3, הַ1ְ2ָ3ָה, הֶ1ְ2ֵ3, הִתְ1ַּ2ְּ3וּת, אִ1ְ2וּ3, תּ1ְ2וּ3, (חזרה על פעולה או חידוש) שִׁ1ְ2וּ3 \ שִׁ1ְ2וּי"
+ "\nמקומות: " +
'מִ1ְ2ָ3','מִ1ְ2ָ3ָה','מִ1ְ2וֹ3','1ִ2ְ3ִיָּה'
 +  "\nבעלי מקצוע: " +
"1וֹ2ֶא, 1ַ2ַּאי, 1ַ2ְיָן, 1ַ2ְּיָן, מַ1ְ2ִיא, 1ַ2ָּ3, 1ַ2ְ3ַאי, (מקור ארמי) אַ1ְ2ְ3ַאי"
+ "\nכלים: " +
"מַ1ְ2ֵ3, מַ1ְ2ֵ3ָה, מִ1ְ2ֶ3ֶת, מִ1ְ2ֹ3ֶת, מִ1ְ2וֹ3, 1ַ2ִּי3, 1ַ2ּוּ3, 1ַ2ּוּי, 1ִ2ּוֹ3, 1ַ2ֶּ3ֶת, מַ1ְ2ִיא"
+ "\nחיבור של כמה אנשים/עצמים: 1ְ2וּ3ָה, צבעים: 1ָ2ֹ3", 'חקלאות: 1ָ2ִי3', 'מומים: 1ִ2ֵּ3', 'דגים וחיות ים: 1ְ2ַ3ְנוּן', 'מחלות: 1ַ2ֶּ3ֶת'
+ "\n" + "\nשונות: " +
'1ָ2וּי',' מִ1ְ2ָא',' 1ִ2ּוּא',' 1ִ2ּוּי', 'תַּ1ְ2ִּית', 'תַּ1ְ2ִּיוֹת','אֶ1ְ2ָ3', 'אֶ1ְ2וֹ3', 'אַ1ְ2ָ3ָה', 'יַ1ְ2וּ3', 'מְ1ַ2ֵּ3', 'מְ1ֻ2ָּ3', 'מְ1ֻ2ָּ3וּת', 'מִ1ְ2ֵ3', 'מִ1ְ2ָ3', 'מִתְ1ַ2ֵּ3', 'מֶ1ְ2ָ3ָה', 'מַ1ְ2ִי3', 'מַ1ְ2ֵ3', 'מַ1ְ2ֵ3ָה', 'מַ1ְ2ֶ3ֶת', 'מַ1ְ2ָ3ָה', 'מַ1ְ2ֹ3ֶת', 'מַ1ְ2וֹ3', 'מַ1ְ2וֹ3ִית', 'מַ1ְ2וּ3', 'מַ1ְ2וּ3ָה', 'מֻ1ְ2ָ3', 'מֻ1ְ2ָ3ָה', 'נִ1ְ2ָ3', 'נִ1ְ2ָ3וּת', '1ְ2ִי3', '1ְ2ִי3וּת', '1ְ2ִ3ָּה', '1ְ2ֵ3', '1ְ2ֵ3ֶת', '1ְ2ֵ3ָה', '1ְ2ֶ3ֶת', '1ְ2ַ3ְ2ֶ3ֶת', '1ְ2ַ3ְ2ֹ3ֶת', '1ְ2ָ3', '1ְ2ָ3ִים', '1ְ2ָ3ָה', '1ְ2ֹ3ֶת', '1ְ2וֹ2ֶ3ֶת', '1ְ2וֹ3', '1ְ2וֹ3ָה', '1ְ2וּ3', '1ְ2וּ3ִית', '1ִ2ְ3ָן', '1ִ2ְ3וֹנִי', '1ִ2ֵּ3', '1ִ2ֶּ3ֶת', '1ִ2ָּ3', '1ִ2ֹּ3ֶת', '1ִי2וֹ3', '1ֵ2ֶ3', '1ֵ2וּ3', '1ֶ2ְ3ָה', '1ַ2ְּ3ָן', '1ַ2ְ3ִי3', '1ַ2ְ3ִית', '1ַ2ְ3ָנִי', '1ַ2ְ3וֹן', '1ַ2ְ3וּ3ִי', '1ַ2ֵּ3', '1ַ2ָּ3ָה', '1ַ2ֹּ3ֶת', '1ַ2וֹ3', '1ָ2ְ3ָה', '1ָ2ֵ3', '1ָ2וֹ3', '1ָ2וּ3', '1ֻ2ְ3ָה', '1ֻ2ְ3ָן', '1ֻ2ָּ3', '1ֻ2ֹּ3ֶת', '1וֹ2ְ3ָה', '1וֹ2ְ3ָן', '1וֹ2ֵ3', '1וֹ2ֶ3ֶת', '1וֹ2ָ3', 'תַּ1ְ2ֵ3', 'תַּ1ְ2ֵ3ָה', 'תַּ1ְ2ָ3ָה', 'תַּ1ְ2וּ3'
+ "\n נדירים:" +
"\nהוספת אות בתחילת מילה: סִ1ְ2ֵ3, שִׁ1ְ2ֵ3, שִַ1ְ2ֶ3ֶת"
+ "\n הוספת אות באמצע מילה: קע23, 12ע3, 1323, 1ר23 (1ַרְ2ָ3 \ 1ַּרְ2ּוֹ3 \ 1ַרְ2ִי3 \ 1ֻרְ2ָ3 \ 1ִּרְ2ֹּ3 \ 1ַרְ2ַ3ִּים וכיו''ב)"
+ "\n ניתן לחפש את השורש החדש כשורש מרובע חדש"
+ "\n ריבוי מיוחד: 1ַ2ְ3וֹנִים, 1ְּ2ִ3ִים"
+ "\n שורשים תניינים אפשריים: מ12’’3, א12’’3, ת12’’3, 123’’ת \n"


        ])

    # Condition for שורש מגזרת ע"וי
    if len(input_letters) == 3 and input_letters[1] in 'וי':
        categories["שורש מגזרת נעו''י"] = generate_list(input_letters, [
"\nשם עצם מופשט: " +
"1ָיָ3, 1ֶיֶ3, 1ֹיֶ3, 1ִוְ3ָה, 1ִוְ3וֹן, 1ִוָּ3וֹן, 1ַ3וּת"
+ "\nבעלי תכונה: " +
"מוּ1ָ3 \ מֻ1ָ3, נָ1וֹ3"
+ "\nשמות פעולה: " +
"1ִי3ָה, 1ִיּוּ3, 1ִי3וּ3, 1וֹ3ְ3וּת, 1ַּוָּ3ָה, הֲ1ָ3ָה, הַ1ְוָ3ָה, הִתְ1וֹ3ְ3וּת, תְּ1וּ3ָה, 1וֹ2ְ2ִיּוּת"
+ "\nהקטנה: " +
"1וֹ3ִי3"
+ "\nמקומות: " +
"מָ1וֹ3, מְ1וּ3ָה"
 +  "\nבעלי מקצוע: " +
"1ָ3, מְ1וֹ3ֵ3, 1ַיְּ3ָן, 1ַיָּ3, (מקור ארמי) 1ַ3ַּאי"
+ "\nכלים: " +
"מְ1וֹ3ֵ3, מֵ1ִי3, מֵ1ִי3ָה, מִ1ְ3וֹ3"
+ "\nחיבור של כמה אנשים/עצמים: "+
"1וּ3ָה," +
" צבעים: 1ָיֹ3, חקלאות: 1ָיִ3, דגים וחיות ים: 1ָ3ְנוּן, מחלות: 1ַיֶּ3ֶת"
+ "\n" + "\nשונות: " +
"1ַוָּ3, 1ִיָּ3, 1ָ3ָה, 1וּ3,1וּ3ִים, הֶ1ָ3ָה, הִתְ1ַּוְ3וּת, הִתְ1ַיְּ3וּת, נִ1ּוֹ3, מְ1ִי3ָה, מְ1ָ3, מַ1ָ3, מְמְּ1וּ3ָה, 1ַ3ְ1ַ3, 1ַ3ְ1וּ3, יֶ1ֶ3, מִתְ1וֹ3ֵ3, מוּ1ָ3וּת, 1ָ3וֹא, 1ָ3וֹי,מֵ1ְוֹ3, מַ1ֹ3ֶת, מַ1וֹ3ִית, מַ1וּ3, מַ1וּ3ָה, מֻ1ָ3ָה,נְ1וֹ3וּת, 1ֲוִי3, 1ֶוִי3, 1ְוִי3, 1ִי3וּת,1ְיָ3, 1ְיָ3ִים, 1ְוָ3, 1ְוָ3ִים, 1ְוָ3ָה, 1וֹ3ֶת,1וּ3, 1וּ3ִית, 1ָ3ָן, 1ָ3וֹנִי, 1ִוֵּ3, 1ִוֶּ3ֶת, 1ִיָּ3, 1ֵ3, 1ִי3ָן, 1ַּוְ3ָן, 1ִי3ִית, 1וּ3ָנִי, 1וֹ3ָנִי, 1ַ3וֹן, 1ַ3וּ3ִי, 1ַ3, 1ֹ3ֶת, 1ֹ3, 1ֻ3ָן, 1ָ3, תַּ1וּ3"
+ "\n נדירים:" 
+ "\n הכפלת אות: 1313 (1ַּ3ְ1ָ3 \ 1ַּ3ְ1ָ3וֹת \ 1ַּ3ְ1וּ3ִי וכיוצ''ב)"
+ "\n שורשים תניינים אפשריים: מ1''3, ת1''3 \n"
        ])
        
    # Condition for תיקון לגזרת חפן ונליה
    if len(input_letters) == 3 and input_letters[0] == 'נ' and input_letters[2] in 'יו':
        categories["שורש משותף לגזרת חפ''ן וגזרת נלי''ה"] = generate_list(input_letters, [
    'מִ2ָּה',
    'מַ2ֶּה',
    'מֻ2ָּה',
    '2ֵית',
    'הַ2ָּאָה',
    'מַ2ָּה',
    'נָ2ֶה'
        ])
        
    # Condition for תיקון לגזרת הכפולים
    if len(input_letters) == 3 and input_letters[1] == input_letters[2]:
        categories["שורש מגזרת הכפולים"] = generate_list(input_letters, [
"\nשם עצם מופשט: " +
"1ָ3ָ3, 1ָ3, 1ֶ3ֶ3, 1ֹ3, 1ִ3ָּה, 1ַ3ָּה, 1ִ3ָּה, 1ֶ3ָה, 1ִ3וֹן, 1ִ3ָּ3וֹן, 1ַ3וּת, 1ִ3ֹּו3ֶת, 1ְ3ֻ3ָּה, תַּ1ְ3ִי3, תַּ1ְ3וּ3ָה, תַּ1ָּ3ָה, תִּ1ְ3ֹ3ֶת"
+ "\nבעלי תכונה: " +
"1ַ3ּוּ3, 1ַ3ִּי3, 1ָ3ִי3, 1ָ3ֹ3, 1ִ3ּוֹ3"
+ "\nשמות פעולה: " +
"1ִ3ָּה, 1ְ3ִי3ָה, הִ1ָּ3וּת, 1ִ3ּוּ3,1ִי3וּ3, הֲ1ָ3ָה, הֶ1ְ3ֵ3,הִתְ1ּוֹ3ְּ3וּת, הִתְ1ַּ3ְּ3וּת, אִ1ְ3וּ3, תּ1ְ3וּ3, (חזרה על פעולה או חידוש) שִׁ1ְ3וּ3, (פעולה רשמית או מוגברת) 1ִ3וּ3"
+ "\nהקטנה: " +
"1ַ3ִי3, 1ַ3וּ3"
+ "\nמקומות: " +
"מִ1ְ3ָ3, מְ1ִ3ָּה, מִ1ְ3וֹ3"
 +  "\nבעלי מקצוע: " +
"1ַיָּ3, 1ַ3ְ3ָן, 1ַ3ְּ3ָן, 1ַ3ָּ3, 1ַ3ַּאי, 1ַ3ְ3ַאי, (מקור ארמי) 1ָ3וֹ3ַאי, (מקור ארמי) אַ1ְ3ְ3ַאי"
+ "\nכלים: " +
"מַ1ֵ3, מַ1ֵ3ָה, מִ1ְ3ֶ3ֶת, מִ1ְ3ֹ3ֶת, מִ1ְ3וֹ3, 1ַ3ִּי3, 1ַ3ּוּ3, 1ִ3ּוֹ3, 1ַ3ֶּ3ֶת"
+ "\nחיבור של כמה אנשים/עצמים: 1ְ3וּ3ָה, צבעים: 1ָ3ֹ3, חקלאות: 1ָ3ִי3, מומים: 1ִ3ֵּ3, דגים וחיות ים: 1ְ3ַנוּן\ 1ְ3ַ3ְנוּן, מחלות: 1ַ3ֶּ3ֶת"
+ "\n" + "\nשונות: " +
"1ַ3, 1ֻ3ָּה, 1ִי3, 1וֹ3, אֶ1ְ3ָ3, אֶ1ְ3וֹ3, אַ1ְ3ָ3ָה, יַ1ְ3וּ3, מְ1ַ3ֵּ3, מְ1ֻ3ָּ3, מְ1ֻ3ָּ3וּת, מִ1ֵ3, מִ1ְ3ָ3, מִ1ָ3, מִתְ1ַ3ֵּ3, מֶ1ְ3ָ3ָה, מַ1ְ3ִי3, מַ1ֵ3, מַ1ֵ3ָה, מְ1וֹ3ֵ3, מָ1ֵ3, מָ1ַ3, מֵ1ַ3, מָ1ֹ3, מֵ1ַ3, מֵ1ֵ3, מַ1ְ3ֶ3ֶת, מַ1ְ3ָ3ָה, מַ1ְ3ֹ3ֶת, מַ1ְ3וֹ3, מַ1ְ3וֹ3ִית, מַ1ְ3וּ3, מַ1ְ3וּ3ָה, מוּ1ָ3, מוּ1ָ3ָה, נִ1ְ3ָ3,נִ1ָ3, נִ1ְ3ָ3וּת, 1ְ3ִי3, 1ְ3ִי3וּת, 1ִ3ָּה, 1ְ3ֵ3ֶת, 1ְ3ֵ3ָה, 1ְ3ֶ3ֶת,1ְ3ָ3, 1ְ3ָ3ִים, 1ְ3ָ3ָה, 1ְ3ֹ3ֶת,1ְ3וֹ3ֶ3ֶת, 1ְ3וֹ3, 1ְ3וֹ3ָה, 1ְ3וּ3, 1ְ3וּ3ִית, 1ִ3ָּן, 1ִ3ּוֹנִי, 1ִ3ֵּ3, 1ִ3ֶּ3ֶת, 1ִ3ָּ3, 1ִ3ֹּ3ֶת, 1ִי3וֹ3, 1ֵ3ֶ3, 1ֵ3וּ3, 1ֶ3ָּה, 1ַ3ָּן, 1ַ3ִּי3, 1ַ3ִּית, 1ַ3ָּנִי, 1ַ3ּוֹן, 1ַ3ּוּ3ִי, 1ַ3ֵּ3, 1ַ3ָּ3ָה, 1ַ3ֹּ3ֶת, 1ַ3וֹ3, 1ָ3ָּה, 1ָ3ֵ3, 1ָ3וֹ3, 1ָ3וּ3, 1ֻ3ָּה, 1ֻ3ָּן, 1ֻ3ָּ3, 1ֻ3ֹּ3ֶת, 1וֹ3ְ3ָה, 1ִ3ְ1וּ3, 1וֹ3ְ3ָן, 1וֹ3ֵ3, 1וֹ3ֶ3ֶת, 1וֹ3ָ3, תְּ1וּ3ָה, תַּ1ַ3, תְּ1ִ3ָּה, תַּ1ְ3ָ3ָה, תַּ1ְ3וּ3, 1ַ3ְ1ַ3, 1ַ3ְ1וּ3, 1ַּ3ְ1ָ3ָה"
+ "\n נדירים:" +
"\nהוספת אות בתחילת מילה: סִ1ְ2ֵ3, שִׁ1ְ2ֵ3, שִַ1ְ2ֶ3ֶת"
+ "\n הוספת אות באמצע מילה: קע23, 12ע3, 1323, 1ר23 (1ַרְ2ָ3 \ 1ַּרְ2ּוֹ3 \ 1ַרְ2ִי3 \ 1ֻרְ2ָ3 \ 1ִּרְ2ֹּ3 \ 1ַרְ2ַ3ִּים וכיו''ב)"
+ "\n ניתן לחפש את השורש החדש כשורש מרובע חדש"
+ "\n ריבוי מיוחד: 1ַ2ְ3וֹנִים, 1ְּ2ִ3ִים"
+ "\n קפיצת אות: 133 > 113"
+ "\n הכפלת אות: קלקל"
        ])
                
        
    return categories

# Function to swap letters with their "brothers" and generate all variations
def generate_brother_swaps(input_letters):
    brother_groups = {
        "חילופי אותיות - גרוניים (אהחע)": ['א', 'ה', 'ע', 'ח'],
        "חילופי אותיות - חיככיים (גיכק)": ['ג', 'כ', 'ק'],
        "חילופי אותיות - לשוניים (דטלנת)": ['ד', 'ט', 'ל', 'נ', 'ת'] ,
        "חילופי אותיות - שפתיים (בומפ -הואו עיצורית)" : ['ב', 'מ', 'פ', 'ו'],
        "חילופי אותיות - שיניים (זסצרש)" : ['ר', 'ש', 'ז', 'צ', 'ס'],
        "חילופי אותיות - שוטפים (למנר)" : ['ל', 'מ', 'נ', 'ר']
    }

    common_swaps = {
        'ל': 'ר', 'ר': 'ל',
        'ש': 'ת', 'ת': 'ש',
        'צ': 'ק', 'ק': 'צ',
        'צ': 'ט', 'ט': 'צ',
        'ב': 'פ', 'פ': 'ב',
        'ז': 'ד', 'ד': 'ז',
        'ע': 'ח', 'ח': 'ע'
    }
    brother_swaps = {}

    for group_name, group_letters in brother_groups.items():
        for i, letter in enumerate(input_letters):
            if letter in group_letters:
                variations = [input_letters[:i] + brother + input_letters[i+1:] for brother in group_letters if brother != letter]
                brother_swaps[group_name] = variations

    # Generate swaps for common letter pairs
    common_variations = set()
    for i, letter in enumerate(input_letters):
        if letter in common_swaps:
            swapped = input_letters[:i] + common_swaps[letter] + input_letters[i+1:]
            common_variations.add(swapped)
    common_variations = list(common_variations - {input_letters})  # Remove the original root if present
    brother_swaps["חילופי אותיות נפוצים במיוחד"] = common_variations

    # Generate all permutations of the input letters
    all_permutations = set(''.join(p) for p in permutations(input_letters))
    all_permutations = list(all_permutations - {input_letters})  # Remove the original root if present
    brother_swaps["כל שיכולי האותיות"] = all_permutations
    
    # Additional condition for גרוניים וגרוניים־חטופים
    if any(letter in input_letters for letter in 'אהחעכקר'):
        variations = set()
        for letter in 'כקר':
            for swap in 'אהחע':
                if letter in input_letters:
                    variations.add(input_letters.replace(letter, swap))
        for letter in 'אהחע':
            for swap in 'כקר':
                if letter in input_letters:
                    variations.add(input_letters.replace(letter, swap))
        variations = list(variations - {input_letters})  # Remove the original root if present
        brother_swaps["חילופי אותיות - גרוניים (אהחע) וגרוניים־חטופים (כקר)"] = variations

    # Additional condition for לשוניים ושורקים
    if any(letter in input_letters for letter in 'דטלנתשצסז'):
        variations = set()
        for letter in 'שצסז':
            for swap in 'דטלנת':
                if letter in input_letters:
                    variations.add(input_letters.replace(letter, swap))
        for letter in 'דטלנת':
            for swap in 'שצסז':
                if letter in input_letters:
                    variations.add(input_letters.replace(letter, swap))
        variations = list(variations - {input_letters})  # Remove the original root if present
        brother_swaps["חילופי אותיות - לשוניים (דטלנת) ושורקים (זסצש)"] = variations
        
    # Additional condition for לשוניים וחיכיים
    if any(letter in input_letters for letter in 'דטלנתגכק'):
        variations = set()
        for letter in 'גכק':
            for swap in 'דטלנת':
                if letter in input_letters:
                    variations.add(input_letters.replace(letter, swap))
        for letter in 'דטלנת':
            for swap in 'גכק':
                if letter in input_letters:
                    variations.add(input_letters.replace(letter, swap))
        variations = list(variations - {input_letters})  # Remove the original root if present
        brother_swaps["ב חילופי אותיות - לשוניים (דטלנת)וחיכיים (גיכק) "] = variations

    return brother_swaps


def generate_double_gronit_swaps(input_letters):
    double_gronit_swaps = []

    # Check if the first letter is one of א, ה, ח, ע
    if input_letters[0] in 'אהחע':
        patterns = [
            '2ַ3ְ2ַ3',
            '2ַ3ְ2ַ3ִים',
            '2ַ3ְ2ֶ3ֶת'
        ]
        double_gronit_swaps = [pattern.replace('2', input_letters[1]).replace('3', input_letters[2]) for pattern in patterns]

    # Check if the second letter is one of א, ה, ח, ע
    elif input_letters[1] in 'אהחע':
        patterns = [
            '1ַ3ְ1ַ3',
            '1ַ3ְ1ַ3ִים',
            '1ַ3ְ1ֶ3ֶת'
        ]
        double_gronit_swaps = [pattern.replace('1', input_letters[0]).replace('3', input_letters[2]) for pattern in patterns]

    return double_gronit_swaps


# Function to get input and display the output lists

# (Paste all the rest of your functions below, no changes!)
# -------------------------------------------
# Example placeholder for the other functions:
# def replace_end_letters(word): ...
# def replace_letters(word): ...
# def process_letters(input_letters): ...
# def generate_list(letters, patterns): ...
# def generate_additional_categories(input_letters): ...
# def generate_brother_swaps(input_letters): ...
# def generate_double_gronit_swaps(input_letters): ...
# (Copy and paste them all!)

# -------------------------------------------
# --------- Streamlit Interface -------------
# -------------------------------------------

# ------------------------- Streamlit App -------------------------


# ------------------------- Streamlit Layout -------------------------

st.set_page_config(page_title="המחדשה", layout="centered")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Frank+Ruhl+Libre&display=swap');

    html, body, [class*="css"]  {
        font-family: 'Frank Ruhl Libre', serif;
        text-align: center;
        direction: rtl;
    }

    .logo-text {
        font-family: 'Frank Ruhl Libre', serif;
        font-size: 64px;
        font-weight: normal;
        margin-top: 20px;
        margin-bottom: 10px;
    }

    .tagline-text {
        font-family: 'Frank Ruhl Libre', serif;
        font-size: 28px;
        font-weight: normal;
        margin-bottom: 30px;
    }

    .stTextInput>div>div>input {
        text-align: center;
        direction: rtl;
        font-size: 32px;
        font-family: 'Courier New', monospace;
        width: 150px !important;
    }
    </style>
    """, unsafe_allow_html=True)

st.markdown('<div class="logo-text">הַמַחְדֵשָׁה</div>', unsafe_allow_html=True)
st.markdown('<div class="tagline-text">של אילון</div>', unsafe_allow_html=True)

root = st.text_input("יש להזין שורש עברי:", key="root_input")



# Button to generate results
if st.button("חדש־נא!"):
    if 3 <= len(root) <= 4:
        root_processed = initial_replacements(root)
        root_processed = process_letters(root_processed)

        results = generate_additional_categories(root_processed)
        double_gronit = generate_double_gronit_swaps(root_processed)
        brothers = generate_brother_swaps(root_processed)

        # Display results
        st.subheader("תוצאות:")

        final_output = ""

        special_sections = ["הוספת אות בתחילת מילה", "ריבוי מיוחד", "שורשים תניינים אפשריים"]
        all_keys = list(results.keys())
        
        for key in all_keys:
            if key not in special_sections and key != "נדירים":
                final_output += f"{key}: {', '.join(results[key])}\n"
        
        for key in special_sections:
            if key in results:
                final_output += f"{key}: {', '.join(results[key])}\n"
        
        if double_gronit:
            final_output += f"חֲ1ַ2ֶּ3ֶת, 1וּ2ְ3ָה: {', '.join(double_gronit)}\n"
            final_output += "הכפלת אות: 2ִ3ְ2ֵ3\n"
        
        if "נדירים" in results:
            final_output += f"נדירים: {', '.join(results['נדירים'])}\n"
        
        for key, words in brothers.items():
            final_output += f"{key}: {', '.join(words)}\n"


        if final_output:
            # Format the final output: make titles bold, lists in one line
            formatted_output = ""
            for line in final_output.strip().split("\n"):
                if ":" in line:
                    parts = line.split(":", 1)
                    title = parts[0].strip()
                    content = parts[1].strip()
                    formatted_output += f"<b>{title}:</b> {content}<br>"
                else:
                    formatted_output += f"{line}<br>"


            st.markdown(f"""
                <div style="text-align: right; direction: rtl; font-family: 'Frank Ruhl Libre', serif; font-size: 18px; border: 1px solid #ddd; padding: 15px; border-radius: 8px; background-color: #f9f9f9; width: 100%;">
                {formatted_output}
                </div>
                """, unsafe_allow_html=True)
        else:
            st.info("לא נמצאו תבניות עבור השורש.")
    else:
        st.warning("הקלידו שורש בן 3 או 4 אותיות בלבד.")

