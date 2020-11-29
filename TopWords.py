def get_list_of_words_json():
    import json

    with open('newsafr.json', encoding='utf-8') as json_file:
        data = json.load(json_file)
    items = data['rss']['channel']['items']
    text_list = []
    for item in items:
        for key, value in item.items():
            if key == 'description':
                splited_text = value.split(' ')
                text_list.append(splited_text)
    return text_list


def get_list_of_words_xml():
    import xml.etree.ElementTree as ET
    parser = ET.XMLParser(encoding='utf-8')
    tree = ET.parse('newsafr.xml', parser)
    root = tree.getroot()
    items = root.findall('channel/item')
    text_list = []
    for news in items:
        description = news.find('description')
        text = description.text.split(' ')
        text_list.append(text)
    return text_list


def get_top_words(text_list, min_word_length, quantity):
    filtered_words = []
    unique_filtered_words = []
    for splited_text in text_list:
        for word in splited_text:
            if len(word) >= min_word_length:
                filtered_words.append(word)
    alph_sort_filtered_words = sorted(filtered_words)
    count_sort_filtered_words = sorted(alph_sort_filtered_words, key=lambda x: filtered_words.count(x), reverse=True)
    for word in count_sort_filtered_words:
        if word not in unique_filtered_words:
            unique_filtered_words.append(word)
    return '\n'.join(unique_filtered_words[:quantity])

print(get_top_words(get_list_of_words_xml(), 7, 10))
print(get_top_words(get_list_of_words_json(), 7, 10))