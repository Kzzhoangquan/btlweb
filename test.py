from fuzzywuzzy import process  # type: ignore
import mysql.connector
db=mysql.connector.connect(user='root',password='123456',host='localhost')
#tao database
code ='CREATE SCHEMA `btlweb` ;'
#tao bang nguoidung
code1='CREATE TABLE `btlweb`.`nguoidung` (`userid` INT AUTO_INCREMENT NOT NULL,`username` VARCHAR(45) NOT NULL,`pass` VARCHAR(45) NOT NULL, PRIMARY KEY (`userid`));'
#tao bang cau hoi
code3='CREATE TABLE `btlweb`.`nganhangcauhoi` (`cauhoi_id` INT AUTO_INCREMENT NOT NULL,`mamon` VARCHAR(45) NOT NULL,`tenmon` VARCHAR(45) NOT NULL,`question` VARCHAR(255) NOT NULL,`option1` VARCHAR(255) NOT NULL,`option2` VARCHAR(255) NOT NULL,`option3` VARCHAR(255) NOT NULL, `option4` VARCHAR(255) NOT NULL,`correctAnswer` VARCHAR(45) NOT NULL,PRIMARY KEY (`cauhoi_id`));'

# code4="INSERT INTO `btlweb`.`nguoidung` (`userid`, `username`, `pass`) VALUES ('1', 'admin@123.com', '123456');"
code5="INSERT INTO `btlweb`.`nguoidung` ( `username`, `pass`) VALUES ('quan', '1);"
a='kzzhoangquan@gmail.com'
b='6'
code4="INSERT INTO `btlweb`.`nguoidung` (`username`, `pass`) VALUES (%s, %s);"
cursor=db.cursor()
# mycursor.execute("UPDATE btlweb.nguoidung SET pass=(%s) WHERE userid = (%s)",(b,a))
cursor.execute("SELECT DISTINCT tenmon FROM btlweb.nganhangcauhoi")
res=cursor.fetchall()
print(res)
all_names=[str(row[0]) for row in res]
    # Sử dụng fuzzy matching để tìm các tên gần giống
similar_names = process.extract('b', all_names, limit=1)
print(f"Có phải bạn muốn làm bài trắc nghiệm của môn học: '{similar_names[0][0]}'. Bạn hãy nhập lại tên môn để làm nhé")

# db.commit()