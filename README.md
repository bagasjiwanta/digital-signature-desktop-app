# digital-signature-desktop-app

Digital signature implementation using self-built RSA and SHA3. 

Built using Python (PyQT, Pycryptodome).

## RSA Generator
![image](https://user-images.githubusercontent.com/68982753/234836547-3aeada30-bfc7-41b9-9469-4c3056de7bb6.png)

The program generates 256 bit public key and private key to a certain folder. The public and private key are separated to 2 files. 
To generate large primes, the program uses low primality check and miller rabin primality test to reduce the non-prime chance significantly.
The public key is saved to a file named `public_key.pub` with `n,e` format
![image](https://user-images.githubusercontent.com/68982753/234842801-6e09b50c-d17f-4fe2-b56a-cb73c104c87b.png)

The public key is saved to a file named `private_key.pri` with `n,d` format
![image](https://user-images.githubusercontent.com/68982753/234843175-a5d225b9-6fd4-4147-ad3a-4302c371efe7.png)

n, d, and e are the products of RSA

## Digital signture
![image](https://user-images.githubusercontent.com/68982753/234837177-fd158486-86f5-4654-8b44-8188205197ab.png)

### Signing text files (File txt)
![image](https://user-images.githubusercontent.com/68982753/234840051-8c48b53e-e990-4568-90ac-ceee374324f6.png)

When signing text files, the signature are embedded to the end of the file with a custom `<ds>{signature}</ds>` tag. 
Digital signatures are created by encrypting the hash with the previously generated private key. 

### Signing general files (File lain)
![image](https://user-images.githubusercontent.com/68982753/234840082-b72c6cf7-25ef-45ff-9aee-64add962369b.png)

When signin a general file (could be PDF, Images, Videos, etc.), the program outputs the digital signature into a separate text file.

![image](https://user-images.githubusercontent.com/68982753/234840014-d0ce120c-6a08-4ff1-b78b-8391fe07672a.png)

## Verifying Digital Signatures

### Verifying signed text files
![image](https://user-images.githubusercontent.com/68982753/234840924-eca533fe-463d-417c-8400-c4b08d7abfad.png)

Public key and the text file are needed. 
The verifying process starts with finding the signature in the custom `<ds>{signature}</ds>` tag in the text file.
Then, the signature is decrypted with the imported public key. 
The decrypted signature is then compared to the SHA3 hash of the file

### Verifying signed general files
![image](https://user-images.githubusercontent.com/68982753/234841523-b59bf903-b34d-45f1-b9a1-4e07c7d66c6a.png)

In addition to the public key and the original file, the sign file created before is also needed. 
The verifying process starts with finding the signature within the custom tags in the sign file. 
Then, the signature is decyrpted with the imported public key.
The decrypted signature is then compared to the SHA3 has of the original file

## Errors
The program could detect 2 types of error when verifying:

- signature corrupted / not found. This happens when the tags are formed incorrectly or missing
![image](https://user-images.githubusercontent.com/68982753/234843564-1ad2ab41-49db-47ca-87a3-cd7f8aa754e2.png)

- File changed. This happens when the file (text or general file) is altered
![image](https://user-images.githubusercontent.com/68982753/234843586-73e9c028-0804-4e54-a309-9cf0c56f1315.png)
