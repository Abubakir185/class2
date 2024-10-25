class Book:
    def __init__(self, nomi, muallifi, janri, nusxalar_soni):
        self.nomi = nomi
        self.muallifi = muallifi
        self.janri = janri
        self.nusxalar_soni = nusxalar_soni
    
    def get_copy(self, olingan_nusxalar_soni):
        self.nusxalar_soni -= olingan_nusxalar_soni

    def return_book(self, qaytarilgan_kitob_soni):
        self.nusxalar_soni += qaytarilgan_kitob_soni



atomic_habbits = Book("Atomic habbits", "James Clear", "None", 100)
to_kill_a_mockingbird = Book("To Kill a Mockingbird", "Harper Lee", "Tarixiy drama, ijtimoiy adabiyot", 10)

to_kill_a_mockingbird.get_copy(5)

print(to_kill_a_mockingbird.nusxalar_soni)

atomic_habbits.get_copy(2)

print(atomic_habbits.nusxalar_soni)