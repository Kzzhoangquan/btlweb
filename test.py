# from fuzzywuzzy import process  # type: ignore
# import mysql.connector
# conn=mysql.connector.connect(user='root',password='123456',host='localhost')
# #tao database
# code ='CREATE SCHEMA `btlweb` ;'
# #tao bang nguoidung
# code1='CREATE TABLE `btlweb`.`nguoidung` (`userid` INT AUTO_INCREMENT NOT NULL,`username` VARCHAR(45) NOT NULL,`pass` VARCHAR(45) NOT NULL, PRIMARY KEY (`userid`));'
# #tao bang cau hoi
# code3='CREATE TABLE `btlweb`.`nganhangcauhoi` (`cauhoi_id` INT AUTO_INCREMENT NOT NULL,`mamon` VARCHAR(45) NOT NULL,`tenmon` VARCHAR(45) NOT NULL,`question` VARCHAR(255) NOT NULL,`option1` VARCHAR(255) NOT NULL,`option2` VARCHAR(255) NOT NULL,`option3` VARCHAR(255) NOT NULL, `option4` VARCHAR(255) NOT NULL,`correctAnswer` VARCHAR(45) NOT NULL,PRIMARY KEY (`cauhoi_id`));'

# # code4="INSERT INTO `btlweb`.`nguoidung` (`userid`, `username`, `pass`) VALUES ('1', 'admin@123.com', '123456');"
# code5="INSERT INTO `btlweb`.`nguoidung` ( `username`, `pass`) VALUES ('quan', '1);"
# a='kzzhoangquan@gmail.com'
# b='6'
# code4="INSERT INTO `btlweb`.`nguoidung` (`username`, `pass`) VALUES (%s, %s);"
# cursor=conn.cursor()
# # mycursor.execute("UPDATE btlweb.nguoidung SET pass=(%s) WHERE userid = (%s)",(b,a))

# cursor.execute(code1)
# conn.commit()


# # db.commit()


from pyvi import ViTokenizer # type: ignore
import re


def tienxuly(document):
    document = ViTokenizer.tokenize(document)
    # đưa về lower
    document = document.lower()
    # xóa các ký tự không cần thiết
    document = re.sub(r'[^\s\wáàảãạăắằẳẵặâấầẩẫậéèẻẽẹêếềểễệóòỏõọôốồổỗộơớờởỡợíìỉĩịúùủũụưứừửữựýỳỷỹỵđ_]',' ',document)
    # xóa khoảng trắng thừa
    document = re.sub(r'\s+', ' ', document).strip()
    return document


def tienxuly1(document):
    # Tách từ bằng biểu thức chính quy
    document = re.findall(r'\b\w+\b', document)
    # Đưa về lower
    document = [word.lower() for word in document]
    # Loại bỏ các ký tự không mong muốn và dấu câu
    document = [re.sub(r'[^\w\s]', '', word) for word in document]
    # Xóa khoảng trắng thừa
    document = ' '.join(document).strip()
    return document

print(tienxuly("cach     de hoc html hieu qua rr ê  ê"))
print(tienxuly1("cach     de hoc html hieu qua rr ê  ê"))