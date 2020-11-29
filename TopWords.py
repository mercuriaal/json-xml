def get_top_words_json():
    import json

    with open('newsafr.json', encoding='utf-8') as json_file:
        data = json.load(json_file)
    items = data['rss']['channel']['items']
    filtered_words = []
    unique_filtered_words = []
    for item in items:
        for key, value in item.items():
            if key == 'description':
                splited_text = value.split(' ')
                for word in splited_text:
                    if len(word) > 6:
                        filtered_words.append(word)
    alph_sort_filtered_words = sorted(filtered_words)
    count_sort_filtered_words = sorted(alph_sort_filtered_words, key=lambda x: filtered_words.count(x), reverse=True)
    for word in count_sort_filtered_words:
        if word not in unique_filtered_words:
            unique_filtered_words.append(word)
    return '\n'.join(unique_filtered_words[:10])


def get_top_words_xml():
    import xml.etree.ElementTree as ET
    parser = ET.XMLParser(encoding='utf-8')
    tree = ET.parse('newsafr.xml', parser)
    root = tree.getroot()
    items = root.findall('channel/item')
    filtered_words = []
    unique_filtered_words = []
    for news in items:
        description = news.find('description')
        splited_text = description.text.split(' ')
        for word in splited_text:
            if len(word) > 6:
                filtered_words.append(word)
    alph_sort_filtered_words = sorted(filtered_words)
    count_sort_filtered_words = sorted(alph_sort_filtered_words, key=lambda x: filtered_words.count(x), reverse=True)
    for word in count_sort_filtered_words:
        if word not in unique_filtered_words:
            unique_filtered_words.append(word)
    return '\n'.join(unique_filtered_words[:10])

print(get_top_words_xml())
print(get_top_words_json())