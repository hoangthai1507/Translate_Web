from transformers import pipeline

# #Mô hình sang tiếng Anh
translator_English = pipeline("translation_vi_to_en", model="facebook/m2m100_418M")
translator_English.model.save_pretrained("Save_model/VietnamesetoEnglish")
#Mô hình sang tiếng Pháp
translator_French = pipeline("translation_vi_to_fr", model="facebook/m2m100_418M")
translator_French.model.save_pretrained("Save_model/VietnamesetoFrench")
#Mô hình sang tiếng Thai
translator_Thai = pipeline("translation_vi_to_th", model="facebook/m2m100_418M")
translator_Thai.model.save_pretrained("Save_model/VietnamesetoThai")
#Mô hình sang tiếng Nga
translator_Russia = pipeline("translation_vi_to_ru", model="facebook/m2m100_418M")
translator_Russia.model.save_pretrained("Save_model/VietnamesetoRussian")
#Mô hình sang tiếng Nhật
translator_Japanese = pipeline("translation_vi_to_ja", model="facebook/m2m100_418M")
translator_Japanese.model.save_pretrained("Save_model/VietnamesetoJapanese")
#Mô hình sang tiếng Hàn
translato_Korean = pipeline("translation_vi_to_ko", model="facebook/m2m100_418M")
translato_Korean.model.save_pretrained("Save_model/VietnamesetoKorean")
#Mô hình sang tiếng Đức
translator_German = pipeline("translation_vi_to_de", model="facebook/m2m100_418M")
translator_German.model.save_pretrained("Save_model/VietnamesetoTGerman")
#Mô hình sang tiếng Ý
translator_Italian = pipeline("translation_vi_to_it", model="facebook/m2m100_418M")
# translator_Italian.model.save_pretrained("Save_model/VietnamesetoItalian")
#Mô hình sang tiếng Trung Quốc
translator_Chinese = pipeline("translation_vi_to_zh", model="facebook/m2m100_418M")
translator_Chinese.model.save_pretrained("Save_model/VietnamesetoChinese")
#Mô hình sang tiếng Thổ nhỉ kì
translator_Turkish = pipeline("translation_vi_to_tr", model="facebook/m2m100_418M")
translator_Turkish.model.save_pretrained("Save_model/VietnamesetoTurkish")




# # #Mô hình sang tiếng Anh
# translator_English = pipeline("translation_vi_to_en", model="Save_model/VietnamesetoEnglish")
# #Mô hình sang tiếng Pháp
# translator_French = pipeline("translation_vi_to_fr", model="Save_model/VietnamesetoFrench")
# #Mô hình sang tiếng Thai
# translator_Thai = pipeline("translation_vi_to_th", model="Save_model/VietnamesetoThai")
# #Mô hình sang tiếng Nga
# translator_Russia = pipeline("translation_vi_to_ru", model="Save_model/VietnamesetoRussian")
# #Mô hình sang tiếng Nhật
# translator_Japanese = pipeline("translation_vi_to_ja", model="Save_model/VietnamesetoJapanese")
# #Mô hình sang tiếng Hàn
# translato_Korean = pipeline("translation_vi_to_ko", model="Save_model/VietnamesetoKorean")
# #Mô hình sang tiếng Đức
# translator_German = pipeline("translation_vi_to_de", model="Save_model/VietnamesetoTGerman")
# #Mô hình sang tiếng Ý
# translator_Italian = pipeline("translation_vi_to_it", model="Save_model/VietnamesetoItalian")
# #Mô hình sang tiếng Trung Quốc
# translator_Chinese = pipeline("translation_vi_to_zh", model="Save_model/VietnamesetoChinese")
# #Mô hình sang tiếng Thổ nhỉ kì
# translator_Turkish = pipeline("translation_vi_to_tr", model="Save_model/VietnamesetoTurkish")


# context = "Tôi đang học NLP và tôi muốn dịch một đoạn văn bản tiếng Việt sang Trung Quốc"
# result = translator_Chinese(context)
# print(result[0]['translation_text'])