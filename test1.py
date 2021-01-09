# import StemmerFactory class
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory

# create stemmer
factory = StemmerFactory()
stemmer = factory.create_stemmer()

jawab = 'ya'
# stemming process
while (True):
    kalimat = input("Masukan Kata atau kalimat yang akan anda distemming : ")

    output  = stemmer.stem(kalimat)
# output   = stemmer.stem(sentence)

    print("Kata Sebelum di Stemming: " + kalimat)   
    print("Kata Setelah di Stemming: " + output)

    jawab = input("Coba Kalimat / Kata Lain??? [ya/tidak]  ")
    if jawab == 'tidak':
        print("Terima Kasih Telah Mencoba")
        break


