import json
import requests
import getdata
import arg
import openai

gd = getdata
model_engine = "text-davinci-003"
openai.api_key = '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'

def translate_gpt3(text, source_lang, target_lang):
    response = openai.Completion.create(
        engine=model_engine,
        prompt=f"Translate from {source_lang} to {target_lang}: {text}",
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    translation = response.choices[0].text.strip()
    return translation

def preprocess_data(label,language):
    #Lấy Link dựa trên title người dùng chọn
    link_title = gd.get_link_by_title(label,arg.url)
    
    #Label:
    label_translate = translate_gpt3(label, "Vietnamese", language)

    #Xác định tag của bài viét
    tag = gd.get_tag(link_title)
    tag = translate_gpt3(tag,"Vietnamese", language)

    #Xác định hình ảnh và caption của hình ảnh
    img = gd.get_main_image_vnexpress(link_title)
    caption=gd.get_caption_image(link_title)
    caption = translate_gpt3(caption,"Vietnamese", language)

    #Xác định content
    content = gd.get_content(link_title)
    content_result = []
    for line in content:
        content_result.append(translate_gpt3(line, "Vietnamese", language))
    
    return label_translate, tag, img, caption, content_result


def preprocess_data_2(label,language):
        #Lấy Link dựa trên title người dùng chọn
    link_title = gd.get_link_by_title(label,arg.url)
    
    #Label:
    label_translate = translate_gpt3(label, "Vietnamese", language)

    #Xác định content
    content = gd.get_content(link_title)
    content_result = []
    for line in content:
        content_result.append(translate_gpt3(line, "Vietnamese", language))
    
    return label_translate, content_result