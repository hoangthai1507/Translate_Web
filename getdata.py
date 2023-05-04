import requests
from bs4 import BeautifulSoup
from PIL import Image
from io import BytesIO
 
def get_title(url):
    # Gửi yêu cầu HTTP đến trang web

    response = requests.get(url)

    # Lấy HTML của trang web
    html = response.text

    # Phân tích HTML bằng BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')

    # Tìm tất cả các thẻ h3 chứa tiêu đề trên trang
    titles = soup.find_all('h3')

    titles_list = []
    for title in titles:
        titles_list.append(title.text)
    titles_list = [s.replace('\n', '') for s in titles_list]
    for i in range(len(titles_list)):
        titles_list[i] = titles_list[i].strip()
    return titles_list

#Lấy link title từ tên của title
def get_link_by_title(title, url):
    # Gửi yêu cầu HTTP đến trang web

    response = requests.get(url)

    # Lấy HTML của trang web
    html = response.text

    # Phân tích HTML bằng BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')

    # Tìm tất cả các thẻ a chứa tiêu đề trên trang
    links = soup.find_all('a', {'title': title})

    # Kiểm tra xem có tìm thấy liên kết không
    if len(links) == 0:
        print('Không tìm thấy liên kết cho tiêu đề này')
    else:
        # Trả về liên kết đầu tiên tìm được
        return links[0]['href']
    


def get_main_image_vnexpress(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    img_tag = soup.find('img', {'class': 'lazy'})
    img_link = img_tag['data-src']
    return img_link


def get_caption_image(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    image_caption = soup.find('p', {'class': 'Image'}).text.strip()       
    return image_caption


def get_content(url):

    # Lấy nội dung của trang web
    response = requests.get(url)
    html_content = response.content

    # Phân tích cú pháp HTML
    soup = BeautifulSoup(html_content, 'html.parser')
    # Lấy phần tử p  cí class description
    description =soup.find(['p'], class_= 'description')
    # Lấy tất cả các phần tử p và figure có class là Normal
    normal_elements = soup.find_all(['p', 'figure'], class_='Normal')

    # In ra nội dung của các phần tử đó
    content = []
    if description:
        content.append(description.text.strip())
    for i in normal_elements:
        content.append(i.text.strip())
    return content


def get_tag(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    meta = soup.find('meta', attrs={'name': 'tt_list_folder_name'})

    if meta:
        content = meta.get('content')
        return content
    else:
        return None