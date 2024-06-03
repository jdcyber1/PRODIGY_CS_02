def process_image(path, key, mode):
    try:
        # print path of image file and key that we are using
        print('The path of file :', path)
        print('Key for {} :'.format(mode), key)

        # open file for reading purpose
        with open(path, 'rb') as fin:
            # storing image data in variable "image"
            image = fin.read()

        # converting image into byte array to perform encryption/decryption easily on numeric data
        image = bytearray(image)

        # performing XOR operation on each value of bytearray
        for index, values in enumerate(image):
            image[index] = values ^ key

        # opening file for writing purpose
        with open(path, 'wb') as fin:
            # writing encrypted/decrypted data in image
            fin.write(image)

        print('{} Done...'.format(mode.capitalize()))

    except Exception as e:
        print('Error caught:', str(e))

# Take path of image as input
path = input('Enter the path of the image file: ')

# Take key as input
key = int(input('Enter key for encryption/decryption of image: '))

# Ask the user whether to encrypt or decrypt
mode = input('Enter "encrypt" to encrypt the image or "decrypt" to decrypt the image: ').strip().lower()

if mode in ['encrypt', 'decrypt']:
    process_image(path, key, mode)
else:
    print('Invalid mode. Please enter either "encrypt" or "decrypt".')
