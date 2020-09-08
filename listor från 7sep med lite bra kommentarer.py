import random

#  ord = ["klubben", "tröjan", "Hammerfall", "mora"

ord_byte = ["Thanos", "Spiderman", "Snickar Hasse", "Batwoman", "lappen", "Batman", "Roadrunner", "Superman", "Cyote",
            "Ironman",
            "Megaman", "Doomslayer", "Ricardo milos"]
print(f"{ord_byte[random.randint(0, 12)]} har även vid tidigare tillfällen stöttat {ord_byte[random.randint(0, 12)]} "
      f"från Dalarna")

print(f"Bland annat har {ord_byte[random.randint(0, 13)]} gjort en låt åt {ord_byte[random.randint(0, 12)]}. "
      f"Nu är det dags igen.")

print(f"{ord_byte[random.randint(0, 12)]} har plockat fram en t-shirt, föreställande musikanternas maskot"
      
      f" {ord_byte[random.randint(0, 12)]} iförd {ord_byte[random.randint(0, 12)]} IK-kläder.")

print(f"{ord_byte[random.randint(0, 12)]} kommer finnas i 250 exemplar och kostar 249 kronor styck. "
      f"Eftersom alla intäkter oavkortat går till {ord_byte[random.randint(0, 13)]} så 62 250 kronor om alla säljs.")

print(f"Sångaren {ord_byte[random.randint(0, 12)]} är uppvuxen i Mora. "
      f"— Min förhoppning är också att vara på {ord_byte[random.randint(0, 12)]} någon dag under kommande säsong för "
      f"signering,"
      f" säger {ord_byte[random.randint(0, 12)]} i en kommentar på klubbens hemsida.")

# len() betyder längden på en lista

# ramdom.choise() väljer slumpvis något i ett spann av flera saker. tex i en lista
# list = ["1", "2", "3"] så väljer random.choise() slumpvis något av dessa alternativ.
# det gör att man inte behöver ha koll på listans längs eller vilket nummer saker har i listan.


# nedanför är ett exempel på en string som har flera rader
# man måste ge den en variabel för att kunna använda den

s = """ ("Hammerfall har även vid tidigare tillfällen stöttat hockeyklubben från Dalarna. "
    "Bland annat har man gjort en låt åt hockeyklubben. Nu är det dags igen. Bandet har plockat fram en t-shirt, 
    föreställande musikanternas maskot Hector iförd Mora IK-kläder.
Tröjan kommer finnas i 250 exemplar och kostar 249 kronor styck. Eftersom alla intäkter oavkortat går till klubben så 62 
250 kronor om alla säljs.
Sångaren Joacim Cans är uppvuxen i Mora. 
— Min förhoppning är också att vara på plats någon dag under kommande säsong för signering, säger han i en kommentar på 
klubbens hemsida.")
"""












