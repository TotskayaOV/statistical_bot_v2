from PIL import Image

from config import name_tables

def save_one_image(result_list: list, str_obj: str):
    """
    Image.new('RGB', (ширина, высота, (фон))
    :return: boolean:
                True - файл с данными создан
                False - данных за дату нет
    """
    file_label = list(name_tables.keys())
    check_size = sum(result_list)
    if check_size:
        for i in range(len(result_list)):
            if result_list[i] == 1:
                img_ch = Image.open(f'./cred/{file_label[i]}-{str_obj}.jpg')
                img_size = img_ch.size
        if check_size == 1:
            new_im = Image.new('RGB', (img_size[0], img_size[1]), (0, 0, 0))
            new_im.paste(img_ch, (0, 0))
        elif check_size == 4 or check_size == 2:
            new_im = Image.new('RGB', (2 * img_size[0], check_size//2 * img_size[1]), (0, 0, 0))
            param2 = 0
            for i in range(len(result_list)):
                if result_list[i] == 1:
                    img_ran = Image.open(f'./cred/{file_label[i]}-{str_obj}.jpg')
                    if param2 < 2:
                        new_im.paste(img_ran, (img_size[0] * param2, 0))
                        param2 +=1
                    else:
                        new_im.paste(img_ran, (img_size[0] * (param2//3), img_size[1]))
                        param2 += 1
        else:
            new_im = Image.new('RGB', (3 * img_size[0], check_size//2 * img_size[1]), (0, 0, 0))
            param2 = 1
            for i in range(len(result_list)):
                if result_list[i] == 1:
                    img_ran = Image.open(f'./cred/{file_label[i]}-{str_obj}.jpg')
                    if param2 < 3:
                        new_im.paste(img_ran, (img_size[0] * (param2 // 2), 0))
                        param2 += 1
                    elif param2 == 3:
                        new_im.paste(img_ran, (img_size[0] * 2, 0))
                        param2 += 1
                    else:
                        new_im.paste(img_ran, (img_size[0] * (param2 // 5), img_size[1]))
                        param2 += 4
        new_im.save(f"./cred/merged_images-{str_obj}.png", "PNG")
        return True
    else:
        return False