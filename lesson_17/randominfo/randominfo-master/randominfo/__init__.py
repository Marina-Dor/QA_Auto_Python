from __future__ import unicode_literals

import csv
import glob
import shutil
import sys
import pytz

from datetime import datetime, timezone
from fileinput import filename
from math import ceil
from os import W_OK, access
from os.path import abspath, dirname, join, split
from random import choice, randint, randrange, sample
from PIL import Image, ImageDraw, ImageFont

sys.path.append("/randominfo/")

__title__ = 'randominfo'
__version__ = '2.0.2'
__author__ = 'Bhuvan Gandhi'
__license__ = 'MIT'


def full_path(filename):
    return abspath(join(dirname(__file__), filename))


class Person:
    def __init__(self, gender=None):
        self.gender = gender
        self.first_name = self.get_first_name()
        self.last_name = self.get_last_name()
        self.full_name = self.first_name + " " + self.last_name
        self.birthdate = self.get_birthdate()
        self.phone = self.get_phone_number()
        self.email = self.get_email()
        self.gender = self.get_gender(self.first_name)
        self.country = self.get_country()
        self.paswd = self.random_password()
        self.hobbies = self.get_hobbies()
        self.address = self.get_address()
        self.custom_attr = {}

    def set_attr(self, attr_name, value=None):
        if attr_name.isalnum():
            if attr_name[0].isalpha():
                self.custom_attr[attr_name] = value
                print("Attribute '" + str(attr_name) + "' added.")
            else:
                raise ValueError("First character of attribute must be an alphabet.")
        else:
            raise ValueError("Attribute name only contains alphabets and digits.")

    def get_attr(self, attr_name):
        if attr_name.isalnum():
            if attr_name[0].isalpha():
                if attr_name in self.custom_attr.keys():
                    return self.custom_attr[attr_name]
                else:
                    raise AttributeError("Specified attribute is not exists.")
            else:
                raise ValueError("First character of attribute must be an alphabet.")
        else:
            raise ValueError("Attribute name only contains alphabets and digits.")

    def get_details(self):
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "full_name": self.full_name,
            "birthdate": self.birthdate,
            "gender": self.gender,
            "email": self.email,
            "phone": self.phone,
            "paswd": self.paswd,
            "country": self.country,
            "hobbies": self.hobbies,
            "address": self.address,
            "other_attr": self.custom_attr
        }

    @staticmethod
    def get_id(length=6, seq_number=None, step=1, prefix=None, postfix=None):
        generated_id = ""
        if seq_number is None:
            for _ in range(length):
                generated_id += str(randint(0, 9))
        else:
            if type(seq_number).__name__ != 'int' or type(step).__name__ != 'int':
                raise TypeError("Sequence number must be an integer.")
            else:
                generated_id = str(seq_number + step)
        if prefix is not None:
            prefix += generated_id
            generated_id = prefix
        if postfix is not None:
            generated_id += postfix
        return generated_id

    @staticmethod
    def get_first_name(gender=None):
        first_name_file = csv.reader(open(full_path('data.csv'), 'r'))
        filtered_data = []
        if gender is None:
            for data in first_name_file:
                if data[0] != '':
                    filtered_data.append(data)
        else:
            if gender.lower() == "male":
                for data in first_name_file:
                    if data[0] != '':
                        if data[2] == "male":
                            filtered_data.append(data)
            elif gender.lower() == "female":
                for data in first_name_file:
                    if data[0] != '':
                        if data[2] == "female":
                            filtered_data.append(data)
            else:
                raise ValueError("Enter gender male or female.")
        return choice(filtered_data)[0]

    @staticmethod
    def get_last_name():
        last_name_file = csv.reader(open(full_path('data.csv'), 'r'))
        filtered_data = []
        for data in last_name_file:
            if data[1] != '':
                filtered_data.append(data[1])
        return choice(filtered_data)

    @staticmethod
    def get_gender(first_name):
        first_name_file = csv.reader(open(full_path('data.csv'), 'r'))
        gender = ""
        for data in first_name_file:
            if data[0] != '' and data[0] == first_name:
                gender = data[2]
                break
        return gender

    @staticmethod
    def get_country(first_name=None):
        country_file = csv.reader(open(full_path('data.csv'), 'r'))
        country = ""
        if first_name is not None:
            for data in country_file:
                if data[0] != '' and data[0] == first_name:
                    country = data[3]
                    break
            if country == "":
                print("Specified user data is not available. Tip: Generate random country.")
        else:
            filtered_data = []
            for data in country_file:
                if data[12] != '':
                    filtered_data.append(data[12])
            country = choice(filtered_data)
        return country

    def get_full_name(self, gender=None):
        return self.get_first_name(gender) + " " + self.get_last_name()

    @staticmethod
    def get_otp(length=6, digit=True, alpha=True, lowercase=True, uppercase=True):
        lower_chars = "qwertyuioplkjhgfdsazxcvbnm"
        upper_chars = "QWERTYUIOPLKJHGFDSAZXCVBNM"
        digs = "0123456789"
        chars = ""
        otp = ""
        if digit is not False or alpha is not False:
            if digit is True:
                chars += digs
            if alpha is True:
                if lowercase is True:
                    chars += lower_chars
                if uppercase is True:
                    chars += upper_chars
            for _ in range(length):
                otp += str(chars[randint(0, len(chars) - 1)])
            return otp
        else:
            raise ValueError("From parameters 'digit' and 'alpha' anyone must be True.")

    @staticmethod
    def get_formatted_datetime(out_format, str_date, str_format="%d-%m-%Y %H:%M:%S"):
        return datetime.strptime(str_date, str_format).strftime(out_format)

    def get_email(self, person=None):
        domains = ["gmail", "yahoo", "hotmail", "express", "yandex", "nexus", "online",
                   "omega", "institute", "finance", "company", "corporation", "community"]
        extensions: list[str] = ['com', 'in', 'jp', 'us', 'uk', 'org', 'edu', 'au', 'de', 'co',
                                 'me', 'biz', 'dev', 'ngo', 'site', 'xyz', 'zero', 'tech']

        if person is None:
            person = Person()

        c = randint(0, 2)
        dmn = '@' + choice(domains)
        ext = choice(extensions)

        if c == 0:
            email = (person.first_name +
                     self.get_formatted_datetime("%Y", person.birthdate, "%d %b, %Y") +
                     dmn + "." + ext)
        elif c == 1:
            email = (person.last_name +
                     self.get_formatted_datetime("%d", person.birthdate, "%d %b, %Y") +
                     dmn + "." + ext)
        else:
            email = (person.first_name +
                     self.get_formatted_datetime("%y", person.birthdate, "%d %b, %Y") +
                     dmn + "." + ext)
        return email

    @staticmethod
    def random_password(length=8, special_chars=True, digits=True):
        spec_chars = ['!', '@', '#', '$', '%', '^', '&', '*']
        alpha = "QWERTYUIOPLKJHGFDSAZXCVBNMmnbvcxzasdfghjklpoiuytrewq"
        spec_char_len = dig_char_len = 0
        chars = ""
        if special_chars is True:
            spec_char_len = randint(1, ceil(length / 4))
            for _ in range(spec_char_len):
                chars += choice(spec_chars)
        if digits is True:
            dig_char_len = randint(1, ceil(length / 3))
            for _ in range(dig_char_len):
                chars += str(randint(0, 9))
        for _ in range(length - (dig_char_len + spec_char_len)):
            chars += choice(alpha[randint(0, len(alpha) - 1)])

        password = ''.join(sample(chars, len(chars)))
        return password

    @staticmethod
    def get_phone_number(country_code=True):
        phone = ""
        if country_code is True:
            country_codes = [91, 144, 141, 1, 44, 86, 52, 61, 32, 20, 33, 62, 81, 31, 7]
            phone = "+"
            phone += str(choice(country_codes))
            phone += " "
        for i in range(0, 10):
            if i == 0:
                phone += str(randint(6, 9))
            else:
                phone += str(randint(0, 9))
        return phone

    @staticmethod
    def get_alphabetic_profile_img(char, file_path, img_name, char_color=None, bg_color=None):
        chars = "qwertyuioplkjhgfdsazxcvbnmQAZXSWEDCVFRTGBNHYUJMKLIOP0123456789 ,.+=-_()[]{}"
        if all((c in chars) for c in img_name):
            if access(dirname(file_path), W_OK):
                if char_color is not None:
                    if not char_color.isalpha():
                        raise ValueError("Character color must be a name of color.")
                if bg_color is not None:
                    if not bg_color.isalpha():
                        raise ValueError("Background color must be a name of color.")
                char = char[:1].upper()
                if bg_color is None:
                    colors = ['red', 'green', 'royalblue', 'violet', 'pink', 'indigo', 'grey', 'yellowgreen', 'teal']
                    bg_color = choice(colors)
                if char_color is None:
                    char_color = (40, 40, 40)
                img = Image.new('RGB', (512, 512), color=bg_color)
                d = ImageDraw.Draw(img)
                font = ImageFont.truetype("Candara.ttf", 280)
                d.text((170, 140), char, fill=char_color, font=font)
                file_path = file_path + "\\" + str(img_name) + ".jpg"
                img.save(file_path)
            else:
                raise OSError("Invalid or insufficient privileges for specified file path.")
        else:
            raise OSError("Invalid image name. "
                          "Image name must contains character including digits, "
                          "alphabets, white space, dot, comma, ( ) [ ] { } _ + - =.")
        return file_path

    @staticmethod
    def get_face_profile_img(file_path, img_name, gender=None):
        dir_name, file_name = split(abspath(__file__))
        chars = "qwertyuioplkjhgfdsazxcvbnmQAZXSWEDCVFRTGBNHYUJMKLIOP0123456789 ,.+=-_()[]{}"
        if all((c in chars) for c in img_name):
            if access(dirname(file_path), W_OK):
                if gender is None:
                    orig_file = choice(glob.glob(dir_name + "\\images\\people\\*.jpg"))
                elif gender.lower() == "female":
                    orig_file = choice(glob.glob(dir_name + "\\images\\people\\female_*.jpg"))
                elif gender.lower() == "male":
                    orig_file = choice(glob.glob(dir_name + "\\images\\people\\male_*.jpg"))
                else:
                    return ValueError("Invalid gender. It must be male or female.")
                return shutil.copy(orig_file, file_path + "\\" + str(img_name) + ".jpg")
            else:
                raise OSError("Invalid or insufficient privileges for specified file path.")
        else:
            raise OSError("Invalid image name. "
                          "Image name must contains character including digits, alphabets, "
                          "white space, dot, comma, ( ) [ ] { } _ + - =.")

    start_range = datetime(1970, 1, 1, 0, 0, 0, 0, pytz.UTC)
    end_range = datetime.today()

    @staticmethod
    def get_today(_format="%d-%m-%Y %H:%M:%S"):
        return datetime.today().strftime(_format)

    @staticmethod
    def get_date(tstamp=None, _format="%d %b, %Y", start_range=None, end_range=None):
        if tstamp is None:
            start_ts = start_range.timestamp()
            end_ts = datetime.timestamp(end_range)
            tstamp = randrange(int(start_ts), int(end_ts))
        else:
            if type(tstamp).__name__ != 'int':
                raise ValueError("Timestamp must be an integer.")
        return datetime.fromtimestamp(tstamp, tz=timezone.utc).strftime(_format)

    @staticmethod
    def get_birthdate(start_age=None, end_age=None, _format="%d %b, %Y"):
        start_range = datetime.today()
        end_range = datetime(1970, 1, 1, 0, 0, 0, 0, pytz.UTC)
        if start_age is not None:
            if type(start_age).__name__ != 'int':
                raise ValueError("Starting age value must be integer.")
        if end_age is not None:
            if type(end_age).__name__ != 'int':
                raise ValueError("Ending age value must be integer.")
        if start_age is not None and end_age is not None:  # If both are given in arg
            if start_age >= end_age:
                raise ValueError("Starting age must be less than ending age.")
            else:
                start_range = datetime(datetime.now().year - start_age, 12, 31, 23, 59, 59, 0, pytz.UTC)
                end_range = datetime(datetime.now().year - end_age, 1, 1, 0, 0, 0, 0, pytz.UTC)
        elif start_age is not None or end_age is not None:  # If anyone is given in arg
            age_year = start_age if start_age is not None else end_age
            start_range = datetime(datetime.now().year - age_year, 12, 31, 23, 59, 59, 0, pytz.UTC)
            end_range = datetime(datetime.now().year - age_year, 1, 1, 0, 0, 0, 0, pytz.UTC)
        else:
            pass
        start_ts = start_range.timestamp()
        end_ts = end_range.timestamp()
        return datetime.fromtimestamp(randrange(int(end_ts), int(start_ts))).strftime(_format)

    @staticmethod
    def get_address():
        full_addr = []
        addr_param = ['street', 'landmark', 'area', 'city', 'state', 'country', 'pincode']
        for i in range(5, 12):
            addr_file = csv.reader(open(full_path('data.csv'), 'r'))
            all_addresses = []
            for addr in addr_file:
                try:
                    if addr[i] != '':
                        all_addresses.append(addr[i])
                except IndexError:
                    pass
            full_addr.append(choice(all_addresses))
        full_addr = dict(zip(addr_param, full_addr))
        return full_addr

    @staticmethod
    def get_hobbies():
        hobbies_file = csv.reader(open(full_path('data.csv'), 'r'))
        all_hobbies = []
        for data in hobbies_file:
            if data[4] != '':
                all_hobbies.append(data[4])
        hobbies = []
        for _ in range(1, randint(2, 6)):
            hobbies.append(choice(all_hobbies))
        return hobbies


'''
REFERENCE:
http://www.first-names-meanings.com/country-indian-names.html
https://www.familyeducation.com/baby-names/browse-origin/surname/indian
https://thispersondoesnotexist.com/
https://en.wikipedia.org/wiki/List_of_hobbies
'''
