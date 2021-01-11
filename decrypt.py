import io
from base64 import b64encode, b64decode
import hashlib
from Cryptodome.Cipher import AES
import os
from Cryptodome.Random import get_random_bytes
from os import urandom #to generate random values for iv
from io import BufferedReader
from hashlib import pbkdf2_hmac #hashing algos to generate secure key

from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from PIL import ImageSequence
import numpy
import time
import scipy.misc
start_time = time.time()

file_path = "02ee87e2-2868-11ea-b4c8-525400a64f50_v1.enc"
file_path1 = "6e921f57-6831-11ea-bb7d-b4b52f90fbe7_v1_problemative.enc"
base_key = "356erger6ujdfyuskuinmh"
salt = "UXUmNxJkajvsRtOvdeaarrfvzDfkDXYj"
salt1 = "C8FC7DEF947172736721C5D01C91AEE8"

action = "dec"

def watermark_text(photo, output_image_path, text):

    font = ImageFont.truetype(r'Roboto-Bold.ttf', 36)
    im = photo

    numpy_arr = []
    i=0
    for page in ImageSequence.Iterator(im):
        i = i+1
        draw = ImageDraw.Draw(im)
        draw.text((10, 10), text, font=font, fill="black")
        image = numpy.array(page)
        numpy_arr.append(image)

    
    im1 = Image.fromarray(numpy_arr[0])
    im2 = Image.fromarray(numpy_arr[1])
    print(im1.size)
    im1 = im1.resize((768,1024),Image.ANTIALIAS)
    im2 = im2.resize((768,1024),Image.ANTIALIAS)
    # im1.save(output_image_path+".tif", save_all=True, append_images=[im2], optimize=True, quality=10)
    im1.save(output_image_path+".tif", save_all=True, append_images=[im2], compression='tiff_lzw')
    print("---watermak function %s seconds ---" % (time.time() - start_time))


def decrypt(enc_dict):
    # decode the dictionary entries from base64
    salt = enc_dict['salt']
    cipher_text = enc_dict['cipher_text']
    nonce = enc_dict['nonce']
    tag = enc_dict['tag']
    password = enc_dict['password']
    file_path = enc_dict['file_path']
    

    #generte hashed secret key
    private_key = pbkdf2_hmac(
        hash_name='sha1',
        password=password.encode(), 
        salt=nonce, #iv is used as salt in java code
        iterations=65536, #iteration count
        dklen=32
    )
    
    try:


        # create the cipher config
        cipher = AES.new(private_key, AES.MODE_GCM, nonce=nonce)
        # decrypt the cipher text
        decrypted = cipher.decrypt_and_verify(cipher_text, tag)

        file_name = os.path.splitext(file_path)
        print("Writing Decrypted File " + file_name[0] + " .tiff")

        # crete image io
        image = Image.open(io.BytesIO(decrypted))
        print("---decrypt function %s seconds ---" % (time.time() - start_time))
        watermark_text(image, file_name[0], "XER-WER-1212312312312")


    except Exception as error:
        print("exception on decrypt()")
        print(error)
    


if action == "dec":
    print("Start Decrypting Image....... " + file_path);

    in_file = open(file_path, "rb") # opening for [r]eading as [b]inary
    encrypted_file = in_file.read() # if you only wanted to read 512 bytes, do .read(512)
    in_file.close()
    print("---open encrypt file %s seconds ---" % (time.time() - start_time))
    
    #generate 12 byte random number for iv
    iv = encrypted_file[4:16]

    enc_dict = {
        'salt': salt,
        'cipher_text': encrypted_file[16:-16],
        'nonce': iv,
        'tag': encrypted_file[-16::],
        'password': base_key+salt,
        'file_path': file_path
    }

    decrypt_val = decrypt(enc_dict)



print("---end program %s seconds ---" % (time.time() - start_time))
# code = """[4, 2, 3, 1, 5].sort()"""

# execution_time = timeit.timeit(code, number=1)

# print(execution_time)

